# Professor Wencong Su - Research Summary

## Overview
**Professor Wencong Su** is a leading figure in the Department of Electrical and Computer Engineering (ECE) at the University of Michigan-Dearborn. His research operates at the highly critical intersection of advanced optimization, power systems operations, electrified transportation, and applied artificial intelligence. Recently, he has heavily pioneered the use of Large Language Models (LLMs) to solve classic power system optimization problems, such as Economic Dispatch, marking a paradigm shift in how electrical distribution systems are managed.

## Main Research Themes
1. **Applied Generative AI in Power Systems:** Utilizing Large Language Models (LLMs) to function as interpretable surrogate schedulers and to solve complex Economic Dispatch (ED) problems using natural language processing and evolutionary prompting.
2. **Microgrid Architecture & Resilience:** Deploying optimization techniques (MPC, LMI) for converter control and stochastic methods to optimize microgrid design and black-start operations.
3. **Electrified Transportation (EVs):** Analyzing the grid stability impacts (voltage violations, distribution infrastructure constraints) of megawatt-scale charging for medium and heavy-duty electric vehicles (MHDEVs).
4. **Data Analytics in Energy Demand:** Developing real-time data drift detection frameworks to maintain the accuracy of energy demand forecasting models in shifting markets.

## Recent Key Publications (2024 - 2026)
1. **"Fine-Tuned Large Language Models as Surrogate Schedulers for Smart Building Energy Management."** *Energy and Buildings* (2026).
2. **"Real-Time Data Drift Detection in Energy Demand Using Efficient Change-Point Analysis."** *The Journal of Engineering* (2026).
3. **"Large Language Models for Solving Economic Dispatch Problem."** *2025 IEEE Energy Conversion Conference and Expo (ECCE)* (2025).
4. **"Impact of Medium and Heavy-Duty Electric Vehicle Electrification on Distribution System Stability."** *IEEE/AIAA Transportation Electrification Conference (ITEC)* (2025).
5. **"Optimization Techniques for Low-Level Control of DC–AC Converters in Renewable-Integrated Microgrids: A Brief Review."** *Energies* (2025).
6. **"Engineering Microgrids Amid the Evolving Electrical Distribution System."** *Energies* (2024).

---

# Deep Dive Research: Prof. Wencong Su (2024-2026)

## 1. Key Recent Papers (2024-2026)

Dr. Su's recent works demonstrate a bold step away from traditional mathematical solvers toward LLM-driven optimization, while still maintaining deep roots in grid stability (EV charging, Microgrid Converters).

**Paper 1: Large Language Models for Solving Economic Dispatch Problem (2025)**
* **Abstract Summary:** Explores using off-the-shelf LLMs to solve the Economic Dispatch (ED) problem. Instead of explicit mathematical models, it uses few-shot learning and evolutionary prompting to guide the LLM to output optimized generation dispatch vectors.

**Paper 2: Fine-Tuned Large Language Models as Surrogate Schedulers (2026)**
* **Abstract Summary:** Bridges the gap between opaque "black-box" machine learning and transparent energy management by fine-tuning LLMs to handle multi-objective optimization constraints as "surrogate schedulers."

**Papers 4 & 5: Microgrid Control & EV Grid Stability (2025)**
* **Abstract Summary:** Highlights advanced low-level control strategies (Model Predictive Control - MPC) for DC-AC converters in renewable microgrids. Additionally, it investigates grid stability and voltage violations on the IEEE 33-bus system caused by heavy-duty EV charging.

---

## 2. Addressing the "LLM Gap": Why Thanh is the Perfect "Ground Truth" Generator

While Prof. Su is pushing the boundaries of using LLMs for Economic Dispatch and Energy Scheduling, LLMs are fundamentally text-prediction models. To fine-tune an LLM to act as a "Surrogate Scheduler" (Paper 2) or solve Economic Dispatch (Paper 1), Prof. Su needs massive amounts of **mathematically perfect training data**. 

* **The Ground Truth Engine:** An LLM cannot "learn" to solve Economic Dispatch without seeing millions of perfectly solved optimization scenarios. Thanh is an expert in exact mathematical optimization (ADMM, SOCP, MILP) using Python and Pyomo. Thanh can architect the "Ground Truth Generator"—the automated, deterministic systems that generate the massive, flawless datasets required to fine-tune Prof. Su's LLMs.
* **Physics-Informed Safety Filters:** Just like the strategy with Prof. Hong, an LLM might generate a dispatch vector that looks good but violates AC power flow limits. Thanh's graduation thesis on microgrid resilience and MPC is the exact skill needed to build "Safety Filters" that project the LLM's answers into a safe, physically verifiable region (SOCP relaxation constraints).

---

## 3. What Prof. Su Can Teach Thanh

1. **Large Language Models (LLMs) in Engineering:** Prof. Su is actively researching Prompt Engineering, Few-Shot Learning, and Fine-tuning for LLMs applied to power systems. Thanh will learn how to bridge his mathematical code (Python/Pyomo) with AI APIs (OpenAI, HuggingFace) to create hybrid solvers.
2. **Distribution System Impact Analysis (EVs):** Thanh's work has mostly focused on internal microgrid trading. Prof. Su can teach him how to model massive external shocks to the distribution system, such as Megawatt-scale Electric Vehicle charging stations, using IEEE benchmark systems (e.g., IEEE 33-bus).
3. **Translating Algorithms to Real-World Schedulers:** Moving from theoretical ADMM convergence to deploying an AI "Surrogate Scheduler" for Smart Buildings, learning how end-users interact with energy management systems via natural language.

---

## 4. Suitability for Thanh's Ph.D. Goals

**Verdict: Exceptional Fit for the "AI-Optimization" Bridge.**

Thanh's stated Ph.D. goal is to *"resolve the trade-off between computational tractability and physical grid security"* by architecting Physics-Informed AI frameworks. Prof. Su's work on LLMs (which are extremely fast but physically oblivious) and Economic Dispatch is the exact embodiment of this trade-off. 

If Thanh is co-advised by Prof. Bui (Reinforcement Learning) and Prof. Su (LLMs / Optimization), he will sit at the very center of UM-Dearborn's AI-Grid ecosystem. Prof. Su provides the direct application (Economic Dispatch, EV impact), while Thanh provides the rigorous mathematical bedrock to ensure these AI models don't crash the grid.

---

## 5. What Thanh Can Contribute (The Pragmatic Value of a Fresh Undergrad)

1. **Massive Synthetic Data Generation (MILP/ADMM):** To teach an LLM how to schedule energy, you first need to generate millions of edge-case scenarios (weather changes, EV surges, line faults) and solve them perfectly using classical math. Thanh can write the highly parallelized Pyomo/Gurobi scripts to generate this "Ground Truth" data pipeline.
2. **Microgrid Optimization Integration:** Prof. Su is looking at advanced control (MPC) for DC-AC converters in microgrids (Paper 4). Thanh just finished an entire graduation thesis on MPC for microgrid resilience and power routing. He can immediately contribute to Prof. Su's microgrid engineering projects (Paper 3).
3. **Rigorous Validation & Debugging:** When Prof. Su's LLM outputs a generation dispatch vector that causes a voltage violation on the IEEE 33-bus system (Paper 5), Thanh has the AC-OPF knowledge to mathematically trace *why* the voltage dropped and write the constraint to penalize the LLM during fine-tuning.
