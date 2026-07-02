# Literature Review: Result Visualization and Base Cases for Networked Microgrids MPC

This document outlines the standard practices found in IEEE and ScienceDirect literature for visualizing results and establishing benchmarks (base cases) in the context of Model Predictive Control (MPC) and Peer-to-Peer (P2P) trading for networked microgrids.

## 1. Standard Result Graphs and Plots

To effectively demonstrate algorithm efficiency, resilience, and economic benefits, literature typically employs the following types of visualizations:

### 1.1. BESS State of Charge (SOC) Trajectories
- **Purpose:** Demonstrates the dynamic management of energy storage under uncertainty.
- **Visual Style:** Line graphs showing the SOC (%) over the 24-hour simulation period (or across the emergency horizon).
- **Key Observation:** Shows how the MPC pre-charges batteries before a fault (if predicted) and optimally discharges them during the fault to minimize load shedding.

### 1.2. P2P Power Flow and Trading Volumes
- **Purpose:** Highlights the cooperative energy exchange between the networked microgrids.
- **Visual Style:** 
  - Stacked area charts or bar charts showing the imported/exported power for each microgrid.
  - Network graphs (nodes and edges) showing the topology and average power flow direction.
- **Key Observation:** Proves that microgrids with surplus energy (e.g., high PV generation) actively support those experiencing deficits or faults.

### 1.3. Load Shedding Profiles
- **Purpose:** Illustrates system resilience and prioritization during emergency/fault scenarios.
- **Visual Style:** Stacked bar charts distinguishing between **Critical Load Shedding** and **Normal Load Shedding** over time.
- **Key Observation:** Confirms that the control strategy correctly sacrifices normal loads to maintain power to critical loads during contingencies.

### 1.4. Power Balance (Generation vs. Demand)
- **Purpose:** Shows how total generation (PV, Wind, BESS discharge, Grid import) perfectly matches total consumption (Load, BESS charge, Grid export, Load shedding).
- **Visual Style:** Stacked bar charts where positive values represent generation and negative values represent consumption.

### 1.5. Algorithm Convergence (ATC / ADMM)
- **Purpose:** Proves the computational efficiency and stability of the distributed algorithm.
- **Visual Style:** Line graphs plotting the residual error (primal/dual residuals) or objective value against the number of iterations.
- **Key Observation:** Demonstrates that the distributed P2P trading algorithm (e.g., Analytical Target Cascading - ATC) converges quickly within an acceptable tolerance.

---

## 2. Common Base Cases (Benchmarks)

Authors establish "Base Cases" to quantify the improvements (e.g., cost savings, resilience) brought by their proposed framework. The typical benchmarks are:

### 2.1. Isolated Operation Mode (No P2P Trading)
- **Description:** Each microgrid operates independently and relies solely on its own distributed energy resources (DERs) and the main grid.
- **What it proves:** Highlights the economic and resilience benefits of **Networked/P2P** cooperation. The comparison usually shows higher operating costs and more load shedding in the isolated case.

### 2.2. Static Day-Ahead Optimization (No Rolling Horizon / No MPC)
- **Description:** The system schedules resources 24 hours in advance based on forecasts, without updating the schedule in real-time as uncertainties or faults occur.
- **What it proves:** Highlights the benefit of the **Rolling Horizon / MPC** approach. The static model typically fails or incurs massive penalties when a sudden fault occurs, whereas MPC dynamically adjusts.

### 2.3. Centralized Control
- **Description:** A single central controller has perfect information about all microgrids and solves the global optimization problem.
- **What it proves:** Used as a baseline to evaluate the **Distributed Algorithm (ATC/ADMM)**. The goal is to show that the distributed approach achieves near-identical results (small Optimality Gap) while preserving data privacy and reducing single points of failure.

### 2.4. Perfect Foresight (Deterministic Oracle)
- **Description:** An ideal scenario where the controller knows the exact future realization of renewables, loads, and faults over the entire horizon.
- **What it proves:** Establishes the theoretical "best possible" outcome (lower bound on cost). Comparing the MPC performance against Perfect Foresight yields the **Optimality Gap**, proving the MPC robustly handles uncertainty.

---

## 3. Recommendations for the Current Project

Based on the survey of standard literature, the following action items are recommended for the "P2P_trading_withQV_MG1234" project:

1. **Implement the Perfect Foresight Benchmark:** As outlined in Task 3, running a deterministic simulation assuming the fault is known day-ahead will provide a strong baseline to calculate the Optimality Gap.
2. **Implement an Isolated Base Case:** To explicitly prove the value of P2P links, run the MPC algorithm with P2P capacities forced to 0, and compare the load shedding volumes.
3. **Core Visualizations to Build:**
   - **SOC Trajectories:** One plot per microgrid over 24h.
   - **Power Balance & P2P Flow:** Stacked bar charts per microgrid showing internal generation vs. P2P exchange.
   - **Load Shedding:** A clear comparative bar chart showing shed power during the fault phase (e.g., t=12 to t=23).
   - **Convergence Tracking:** A plot of ATC iterations during a critical emergency hour to show speed of convergence.
