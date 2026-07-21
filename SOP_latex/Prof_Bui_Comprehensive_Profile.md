# Professor Van-Hai Bui - Research Summary

## Overview
**Professor Van-Hai Bui** is an Assistant Professor in the Department of Electrical and Computer Engineering (ECE) at the University of Michigan-Dearborn (joined August 2023). He leads a research group focused on energy systems, smart grids, and artificial intelligence.

## Main Research Themes
1. **Energy Management Systems (EMS) & Smart Grids:** Developing operational and control strategies for energy systems and smart grids.
2. **Microgrids:** Operation, control, and optimization of renewable-integrated microgrids.
3. **Artificial Intelligence & Deep Reinforcement Learning:** Applying machine learning, safe reinforcement learning, and large language models (LLMs) to power and energy systems for improved control, resilience, and efficiency.
4. **Peer-to-Peer Electricity Markets & Demand Response:** Exploring fairness shaping, behavioral insights, and consumer engagement in modern energy systems.
5. **Power Systems Resilience:** Enhancing the robustness of power systems, battery management systems, and data centers against disruptions.

## Recent Key Publications (2024 - 2026)
1. **Jadhav, S., Sevak, B., & Bui, V.-H.** "Scalable fairness shaping with LLM-guided multi-agent reinforcement learning for peer-to-peer electricity markets." *Utilities Policy* (2026).
2. **Vu, D. D., Hussain, A., Vu, D.-M., Zhang, X., & Bui, V.-H.** "Designing effective demand response: A review of behavioral insights, consumer engagement, and operational strategies in energy systems." *Energy Research & Social Science*, 131, 104474 (2026).
3. **Bui, V.-H., Mohammadi, S., Das, S., Hussain, A., Hollweg, G. V., & Su, W.** "A critical review of safe reinforcement learning strategies in power and energy systems." *Engineering Applications of Artificial Intelligence*, 143, 110091 (2025).
4. **Hollweg, G. V., Singh Chawda, G., Chaturvedi, S., Bui, V.-H., & Su, W.** "Optimization Techniques for Low-Level Control of DC–AC Converters in Renewable-Integrated Microgrids: A Brief Review." *Energies*, 18(6), 1429 (2025).

## Active Grants & Funding
Dr. Bui has been involved in several funded research projects addressing power systems resilience, data center energy management, and battery management systems. His lab supports both graduate and undergraduate students in these domains.
# Deep Dive Research: Prof. Van-Hai Bui (2024-2026)

## 1. Key Recent Papers (2024-2026)

Based on recent queries from the OpenAlex database, Prof. Van-Hai Bui’s latest research heavily focuses on integrating cutting-edge Artificial Intelligence (specifically Large Language Models and Reinforcement Learning) into smart grids, energy management, and peer-to-peer (P2P) trading. 

**Paper 1: FairMarket-RL: LLM-driven fairness shaping in multi-agent energy trading for smart distribution grids (2026)**
* **DOI:** https://doi.org/10.1016/j.tej.2026.107548
* **Abstract Summary:** Proposes a novel hybrid framework combining Large Language Models (LLMs) with Reinforcement Learning (RL) to enable fairness-aware P2P trading agents. The LLM acts as a real-time fairness critic (evaluating Fairness-To-Buyer and Fairness-Between-Sellers) and shapes the reward for Independent Proximal Policy Optimization (IPPO) agents, replacing brittle rule-based constraints.

**Paper 2: Fine-tuned large language models as surrogate schedulers for smart building energy management (2026)**
* **DOI:** https://doi.org/10.1016/j.enbuild.2026.117588
* **Abstract Summary:** Explores using fine-tuned LLMs as decision surrogates for Mixed-Integer Linear Programming (MILP)-based energy management in Net-Zero Energy Buildings (NZEBs). MILP-generated optimal schedules are used to supervise the LLM to predict distributed generation dispatch, ESS charging, and HVAC set-points, significantly reducing online computational burdens.

**Paper 3: XRL-LLM: Explainable Reinforcement Learning Framework for Voltage Control (2026)**
* **DOI:** https://doi.org/10.3390/en19071789
* **Abstract Summary:** Addresses the "black-box" nature of RL in power systems by introducing a framework that generates natural language explanations for RL control decisions. It uses KernelSHAP combined with an LLM grounded in power systems physics to explain PPO agent decisions for coordinating capacitor banks and tap changers to prevent voltage violations.

**Paper 4: Scalable Impedance Identification of Diverse IBRs via Cluster-Specialized Neural Networks (2026)**
* **DOI:** https://doi.org/10.48550/arxiv.2603.23203
* **Abstract Summary:** Proposes a scalable framework for impedance identification of Inverter-Based Resources (IBRs) using K-means clustering and specialized Feed-Forward Neural Networks (FNNs).

---

## 2. Mapping Thanh's Background to Prof. Bui's Research

Thanh's core background in classical and distributed optimization (MILP, ADMM, SOCP, MPC) is the exact foundational prerequisite for Prof. Bui's current AI-driven trajectory.

* **MILP Background ↔ LLM Surrogate Schedulers (Paper 2):** Prof. Bui is training AI to act as a "surrogate" for MILP. To do this, you need massive, high-quality, mathematically sound datasets generated by MILP models. Thanh's expertise in formulating MILP for microgrids/energy management makes him perfectly suited to build these complex ground-truth models, ensuring the data fed to the AI is robust under all operational constraints.
* **ADMM Background ↔ P2P Energy Trading & MARL (Paper 1):** Thanh's knowledge of distributed optimization via ADMM provides a mathematically proven baseline for P2P trading. He can use this to compare against or hybridize with Prof. Bui's Multi-Agent RL (MARL) approaches. ADMM guarantees convergence, while MARL offers real-time adaptability—combining the two (e.g., using ADMM to pre-train or guide MARL) is a very strong research angle.
* **SOCP / MPC Background ↔ Voltage Control & Safe RL (Paper 3):** Prof. Bui is using Proximal Policy Optimization (PPO) for voltage control. Thanh’s background in SOCP (Optimal Power Flow) and MPC provides the strict physical constraints (e.g., ANSI C84.1 voltage limits) needed to keep these RL agents safe. Thanh can contribute by developing "Safe RL" or Model-Based RL algorithms where MPC acts as a safety shield for the RL exploration.

---

## 3. What Prof. Bui Can Teach Thanh

Joining Prof. Bui's lab would allow Thanh to bridge the gap between classical power system operations and state-of-the-art AI. Specifically, Thanh will learn:

1. **Applied Reinforcement Learning (RL / MARL):** Transitioning from deterministic solvers (MPC/MILP) to stochastic, learning-based agents (PPO, IPPO) that can handle real-time uncertainties in smart grids without heavy online computation.
2. **LLM Integration in Cyber-Physical Systems:** Prof. Bui is at the frontier of using LLMs not just for text, but as *critics, schedulers, and explainers* in engineering control loops. Thanh will learn how to fine-tune open-source models and engineer domain-specific prompts for power systems.
3. **Explainable AI (XAI):** Learning tools like KernelSHAP and combining them with physics-informed models to build trust in AI among grid operators—a major hurdle in modern grid modernization.

---

## 4. Suitability for Thanh's Ph.D. Goals

**Verdict: Highly Suitable.**

Thanh aims to solve modern grid stability and energy management issues. Prof. Bui’s lab represents the natural evolution of Thanh's current skill set. In the AI era, researchers who *only* know ML often fail to respect grid physics, while researchers who *only* know optimization struggle with computational scaling. 

Because Thanh already possesses deep knowledge of the rigorous physical and mathematical models (MILP, SOCP, ADMM), he is the ideal candidate to adopt Prof. Bui's advanced AI methodologies. He won't just be treating the grid as a black-box data problem; he will be able to build **Physics-Informed AI** and **Safe RL** systems. This combination of deep optimization theory and cutting-edge GenAI/RL application is highly lucrative for both high-impact academic publications and industry R&D roles.

---

## 5. What Thanh Can Contribute (The Pragmatic Value of a Fresh Undergrad)

As a fresh graduate applying for a Ph.D., Thanh's core value to Prof. Bui is not in instantly solving the lab's hardest theoretical problems, but in providing **high-output "coding & simulation stamina"** to accelerate the lab's publication rate. Professors have ideas; Ph.D. students execute them. Thanh is the ideal execution engine for the following reasons:

1. **The "Simulation Workhorse" for AI Models:** Prof. Bui’s LLM and RL algorithms require massive, perfectly constrained physical environments to train on. Thanh already possesses the coding stamina and Pyomo/MILP background to build these complex IEEE multi-microgrid environments. He can take Prof. Bui's high-level AI ideas and grind through the coding to produce the rigorous simulations needed for top-tier papers.
2. **Independence & Paper Drafting:** A professor's biggest bottleneck is students who need constant hand-holding. Thanh's undergraduate track record (learning SOCP, ADMM, and Game Theory independently) proves he can read literature, synthesize equations, and most importantly, help draft papers without waiting for step-by-step instructions. 
3. **Debugging the "Math-to-AI" Interface:** When AI models fail in power grids, it's usually because they violate physical constraints. Thanh doesn't just know how to run Python scripts; he understands the underlying AC power flow physics. He can independently debug why an RL agent is causing voltage violations and apply mathematical constraints to fix it, saving the professor hours of troubleshooting.
