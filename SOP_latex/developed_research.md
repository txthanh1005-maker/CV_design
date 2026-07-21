# The Evolution of My Research

## Phase 1: JST Student Forum
- **Core Methodology:** Mixed-Integer Linear Programming (MILP) combined with Demand Response (DR).
- **Scope:** Single lumped node.
- **Objective:** 24-hour load shifting.
- **Limitation:** Too simplistic, ignored grid topology and multi-agent interactions.

## Phase 2: ICGEA International Conference
- **Core Methodology:** MILP + ADMM + Game Theory.
- **Scope:** Decomposed the IEEE 123-bus system into 4 autonomous microgrids.
- **Objective:** Peer-to-peer (P2P) trading of Active Power (P) with data privacy (ADMM) and profit allocation (Game Theory).
- **Limitation:** Ignored physical grid physics (Voltage, Reactive Power, Losses).

## Phase 3: Graduation Thesis (The Breakthrough)
- **Core Methodology:** SOCP Convex Relaxation + ATC (Analytical Target Cascading) + MPC (Model Predictive Control).
- **Scope:** Full physical grid simulation with real-time response.
- **Upgrades from ICGEA:**
  - Added Reactive Power (Q), Voltage (V), and Network Losses to simulate realistic power flows.
  - Implemented Load Shedding and Renewable Energy curtailment constraints to prevent fictitious currents (I ảo) inherent in cone relaxation.
  - Replaced ADMM with ATC to handle fault responses across the entire grid.
  - Wrapped the entire model in MPC to achieve real-time control.
- **Ultimate Goal:** **Resilience** - ensuring the grid can react and survive faults optimally.

## Future Goal (Ph.D. Focus)
- **Limitation of Phase 3:** MPC has limited horizon visibility and forecasting capabilities.
- **Vision:** Integrate AI (Deep Learning / Reinforcement Learning) to enhance forecasting, predict faults before they happen, and look much further into the future to push grid resilience to the next level.
