
"""
[Semantic Metadata]
- Implements: Tập lệnh chính thực thi chương trình, cấu hình dữ liệu và điều phối các hàm khởi tạo mô hình tối ưu cho lưới điện/P2P.
- Related_to_Paper: Emergency_Sharing_Plan
"""

# %% [Phần 0: Chạy cái này một lần duy nhất]
#! Khai báo thư viện 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import sys

import pyomo.environ as pe
import pyomo.opt as po
from pyomo.environ import *
from pyomo.environ import value as py_value, Constraint
from pyomo.core.expr.visitor import identify_variables

import logging
logging.getLogger('pyomo.core').setLevel(logging.ERROR)
from pyomo.environ import Constraint, value as py_value
from pyomo.environ import SolverStatus, TerminationCondition

print ("Start the program")
#! Khai báo hàm 
import build_model
from build_model import build_microgrid_model
from build_model import solve_microgrid_model
from build_model import ATC_Global_model
from build_model import Result_print
from build_model import build_coordinator_model
from Function import S_base, create_graph_separate_MG_trading, load_trading_network, print_line_data
from Function import scale_power

mg_configs = {
        1: {
            'number_of_node': 36,
            # 'list_PV': {3, 8, 10, 12, 14, 26, 36},
            'list_PV': {3, 10, 12, 14, 26, 36},
            'list_Wind': {32},
            'list_BESS': {19},
            'list_DG': {5},
            'grid_trading_limit_max':150,
            'grid_trading_limit_min':-150
        },
        2: {
            'number_of_node': 30,
            'list_PV': {14, 19, 28, 30},
            'list_Wind': {},
            'list_BESS': {20},
            'list_DG': {10},
            'grid_trading_limit_max':1500,
            'grid_trading_limit_min':-1500
        },
        3: {
            'number_of_node': 21,
            'list_PV': {2, 8, 11, 15},
            'list_Wind': {1},
            'list_BESS': {12},
            'list_DG': {9},
            'grid_trading_limit_max':150,
            'grid_trading_limit_min':-150
        },
        4: {
            # Dữ liệu trích xuất từ code MG4
            'number_of_node': 35,          # number_of_node4
            'list_PV': {18, 20, 27,29},       # list_PV
            'list_Wind': {},               # list_Wind (Rỗng)
            'list_BESS': {8},              # list_BESS
            'list_DG': {22},               #          
            'grid_trading_limit_max':150,
            'grid_trading_limit_min':-150 # limit_buy_sell_form_grid (tham số 2)
        }
    } 
trading_limit = {
    0:0* scale_power / S_base,
    1:0* scale_power / S_base,
    2:0* scale_power/ S_base,
    3:0* scale_power / S_base,
    4:0* scale_power / S_base
}

# %%
#! BASE
export_limit = 5000
from build_model import Base_model
model_MG_base, trading_line = Base_model(mg_configs, trading_limit, export_limit)
# %%
#! ACCIDENT MODEL
export_limit = 5000
from build_model import accident_model

# 1. Chỉ bị mất lưới chính từ t=14 đến t=18 cho MG1 và MG2
fault_configs_single = {
    1: [{'start_time': 13, 'end_time': 16, 'type': 'pv_loss', 'severity': 0.0}],
    2: [{'start_time': 15, 'end_time': 20, 'type': 'grid_loss', 'severity': 0.0}],
    3: [],
    4: []
}

# 2. Các lỗi xảy ra tuần tự (Cascading): Mất lưới chính từ t=8 đến t=14 ở MG1, MG2. 
# Sau đó sụt giảm cực đoan quang năng (PV loss) từ t=10 đến t=14. Đánh đúng vào đỉnh phát PV.
fault_configs_cascading = {
    1: [        
        {'start_time': 9, 'end_time': 15, 'type': 'grid_loss', 'severity': 0.0},
        {'start_time': 11, 'end_time': 15, 'type': 'pv_loss', 'severity': 0.0}],
    2: [
        {'start_time': 9, 'end_time': 15, 'type': 'grid_loss', 'severity': 0.0},
        {'start_time': 11, 'end_time': 15, 'type': 'pv_loss', 'severity': 0.0}  
    ],
    3: [],
    4: []
}
# 3. Mất PV của MG1 trong giờ cao điểm RE (High RE Penetration: t=10 đến t=14)
fault_configs_pv_mg1_high_re = {
    1: [{'start_time': 10, 'end_time': 14, 'type': 'pv_loss', 'severity': 0.0}],
    2: [],
    3: [],
    4: []
}

# Gán biến kích hoạt chính để test các kịch bản (Comment các tùy chọn khác lại)
fault_configs = fault_configs_cascading 
# %%
#! ATC GLOBAL MODEL
export_limit = 5000
trading_limit_p2p = {
    0: 150 * scale_power / S_base,
    1: 150 * scale_power / S_base,
    2: 150 * scale_power / S_base,
    3: 150 * scale_power / S_base,
    4: 150 * scale_power / S_base
}
import sys
original_stdout = sys.stdout
with open("Emergency_Sharing_Plan/ATC_output.md", "w", encoding="utf-8") as f:
    sys.stdout = f
    print("# Báo cáo quá trình hội tụ ATC Day-Ahead\n")
    print("```text")
    model_MG_atc, trading_line, history_r, history_s, history_rho, lamda = ATC_Global_model(mg_configs, export_limit, trading_limit_p2p)
    Result_print(model_MG_atc, export_limit, trading_line)
    print("```")
sys.stdout = original_stdout
print(">> ATC run completed. Detailed results at: Emergency_Sharing_Plan/ATC_output.md")

# %%
#! RUN FULL MPC SIMULATION
from build_model import run_MPC_simulation

H = 5

print(f"\n--- RUNNING FULL MPC SIMULATION (Rolling Horizon) WITH H={H} ---")

warm_start_data = {}
for MG in {1, 2, 3, 4}:
    for node in model_MG_atc[MG].node_has_trade:
        for t in range(24):
            warm_start_data[(MG, node, t)] = {
                'lamda': py_value(model_MG_atc[MG].lamda_ATC[node, t]),
                'P_target': py_value(model_MG_atc[MG].P_target[node, t]),
                'P_trade': py_value(model_MG_atc[MG].P_trade[node, t])
            }

model_MG_mpc, trading_line_mpc = run_MPC_simulation(
    mg_configs=mg_configs, 
    export_limit=export_limit, 
    trading_limit_p2p=trading_limit_p2p, 
    H=H, 
    model_MG_atc=model_MG_atc, 
    fault_configs=fault_configs,
    perfect_foresight=False,
    warm_start_data=warm_start_data
)
# %%
from Function import print_result, create_graph_separate_MG_trading, create_graph_separate_MG_Q, S_base, scale_power
for MG in {1, 2, 3, 4}:
    print(f"--- RESULTS FOR MG{MG} IN MPC ---")
    print_result(model_MG_mpc[MG], MG)
    create_graph_separate_MG_trading(model_MG_mpc[MG], export_limit * scale_power / S_base, trading_line_mpc, MG, model_da=model_MG_atc[MG])
    create_graph_separate_MG_Q(model_MG_mpc[MG], export_limit * scale_power / S_base, trading_line_mpc, MG, model_da=model_MG_atc[MG])

print("--- FULL MPC SIMULATION COMPLETED ---")

# %%
