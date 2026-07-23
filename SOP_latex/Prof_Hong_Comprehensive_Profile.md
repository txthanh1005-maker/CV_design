# Professor Junho Hong - Research Summary

## Overview
**Professor Junho Hong** is an Associate Professor in the Department of Electrical and Computer Engineering (ECE) at the University of Michigan-Dearborn. He leads a research group focused on the cybersecurity of energy delivery systems, cyber-physical systems (CPS), and power grid control and protection. Prior to academia, he served as a Senior Research Scientist at ABB Inc., directing cyber-physical security for power grid control and utility communications.

## Main Research Themes
1. **Cybersecurity for Energy Delivery Systems:** Developing frameworks and intrusion detection systems to secure digital substations (IEC 61850), microgrids, and HVDC systems against cyber threats.
2. **Artificial Intelligence in Power System Protection:** Applying Generative AI (GenAI), Large Language Models (LLMs), and Task-Oriented Dialogue (ToD) systems to automate anomaly detection in power grids.
3. **Physics-Informed Machine Learning:** Integrating real-world physical constraints and context-aware models into machine learning algorithms to detect False Data Injection Attacks (FDIA) and ensure safe operations.
4. **Cyber-Physical Systems (CPS) & Tele-driving:** Securing communication channels and detecting anomalies in remote operations (like tele-operated driving) using context-aware algorithms.

## Recent Key Publications (2024 - 2026)
1. **Hong, J., et al.** "Cybersecurity Enhancement in Digital Substations: Hidden Markov Model-Based Smart Cyber Switching and Threat Response." *IEEE Access* (2025).
2. **Ghosh, S., Zaboli, A., Hong, J., & Kwon, J.** "A Physics-Informed Context-Aware Approach for Anomaly Detection in Tele-driving Operations Under False Data Injection Attacks." *IEEE Access* (2025).
3. **Zaboli, A., Choi, S. L., & Hong, J.** "Leveraging Conversational Generative AI for Anomaly Detection in Digital Substations." *2025 IEEE Power & Energy Society General Meeting (PESGM)* (2025).
4. **Zaboli, A., Kasimalla, S. R., Park, K., Hong, Y., & Hong, J.** "A Comprehensive Review of Behind-the-Meter Distributed Energy Resources Load Forecasting." *Energies* (2024).
5. **Hong, J., et al.** "ChatGPT and Other Large Language Models for Cybersecurity of Power Systems." *2024 IEEE PESGM* (2024).
6. **Hong, J., et al.** "Cybersecurity of Autonomous Vehicles: A Systematic Literature Review of Adversarial Attacks and Defense Models." *IEEE Open Journal of Vehicular Technology* (2023).

## Active Grants & Funding
Dr. Hong is actively funded (PI/Co-PI) for projects involving RT-LAB-based distributed resource modeling, machine learning for power system protection, and cyber resilience for substation automation. He was recently promoted to Associate Professor (2024) and serves as an Associate Editor for *IEEE Access*.

---

# Deep Dive Research: Prof. Junho Hong (2024-2026)

## 1. Key Recent Papers (2024-2026)

Based on recent queries, Prof. Junho Hong’s latest research heavily focuses on integrating cutting-edge Artificial Intelligence (specifically Generative AI, LLMs, and Physics-Informed ML) into cybersecurity for power systems and cyber-physical systems.

**Paper 1: A Physics-Informed Context-Aware Approach for Anomaly Detection in Tele-driving Operations Under False Data Injection Attacks (2025)**
* **Abstract Summary:** Proposes a physics-informed, context-aware approach designed to detect anomalies in cyber-physical systems (specifically tele-operated driving) under the threat of False Data Injection Attacks (FDIA). The study emphasizes that merely protecting communication channels is insufficient; the system must understand the underlying physics to detect when malicious data is injected to manipulate physical operations.

**Paper 2: Leveraging Conversational Generative AI for Anomaly Detection in Digital Substations (2025)**
* **Abstract Summary:** Addresses critical challenges of cybersecurity in digital substations by proposing an innovative task-oriented dialogue (ToD) system for anomaly detection (AD) in multicast messages (GOOSE and SV datasets). By leveraging generative artificial intelligence (GenAI), the framework demonstrates superior error reduction, scalability, and adaptability compared with traditional human-in-the-loop (HITL) processes.

**Paper 3: Cybersecurity Enhancement in Digital Substations: Hidden Markov Model-Based Smart Cyber Switching (2025)**
* **Abstract Summary:** Proposes a coordinated defense mechanism using a Hidden Markov Model (HMM) for threat detection in IEC 61850 digital substations. It introduces "Smart Cyber Switching" to transfer logic from a compromised physical IED to a digital twin-based virtual replica to maintain operational continuity during a cyberattack.

**Paper 4: A Comprehensive Review of Behind-the-Meter Distributed Energy Resources Load Forecasting (2024)**
* **Abstract Summary:** Published in *Energies*, this paper provides a deep dive into the models, challenges, and emerging technologies (especially machine learning) for load forecasting in behind-the-meter Distributed Energy Resources (DERs). This verifies Dr. Hong's strong continued involvement in microgrid analytics and distributed energy management, beyond just cybersecurity.

**Paper 5: Cybersecurity of Autonomous Vehicles: A Systematic Literature Review (2023)**
* **Abstract Summary:** Explores the cybersecurity landscape of cyber-physical systems, categorizing complex attack vectors targeting AI-driven perception and decision-making systems in autonomous vehicles and connected infrastructure.

---

## 2. Addressing the "Cybersecurity Gap": Why Thanh is the Missing Puzzle Piece

At first glance, Prof. Hong's heavy focus on "Cybersecurity" might seem daunting since Thanh has no background in IT security, cryptography, or network firewalls. **However, this is precisely why Thanh is extremely valuable to Prof. Hong's lab.** 

When hackers attack a power grid (e.g., False Data Injection Attacks - FDIA), their goal is to alter sensor data to make the grid physically collapse. A pure IT cybersecurity expert or pure AI model looks at the data as just "numbers." They struggle to detect sophisticated attacks because they don't understand the physical rules governing those numbers. 

Thanh does not need to know cryptography; he provides the **"Physics Engine"**.
* **SOCP/MPC as the Ultimate Lie Detector (Paper 1):** Prof. Hong is building "Physics-Informed" AI anomaly detection. If a hacker injects false voltage data, Thanh's background in AC-OPF and SOCP can mathematically prove that the injected data violates Kirchhoff's laws or line thermal limits. Thanh's optimization models act as the ultimate "lie detector" for the AI.
* **From IT Security to OT Resilience:** Thanh’s thesis on using MPC to coordinate emergency microgrid power exchanges is fundamentally about "Operational Technology (OT) Resilience." When the cyber-defense fails, the grid must still physically survive. Thanh knows how to route power and shed loads dynamically to keep the grid alive during an attack. 

By combining Thanh’s physical resilience (power routing) with Hong’s cyber resilience (anomaly detection), they create a holistic *Cyber-Physical Co-Resilience* framework.

---

## 3. What Prof. Hong Can Teach Thanh

Joining Prof. Hong's lab as a co-advisor or collaborator would allow Thanh to bridge the gap between deterministic power system operations and advanced cybersecurity. Specifically, Thanh will learn:

1. **Cyber-Physical Systems (CPS) Threat Modeling:** Learning how vulnerabilities in communication layers (IEC 61850 protocols, GOOSE/SV messaging) affect the physical grid variables he is already familiar with.
2. **Generative AI & LLMs in Engineering:** Prof. Hong is at the frontier of using GenAI and Task-Oriented Dialogue (ToD) systems for anomaly detection. Thanh will learn how to fine-tune open-source LLMs to read and interpret real-time substation data.
3. **Hardware-in-the-Loop (HIL) Simulation:** Prof. Hong heavily utilizes RT-LAB for real-time distributed resource modeling. Thanh will learn to deploy his theoretical optimization models (ADMM, MPC) onto industrial-grade real-time simulators, elevating his research from pure software simulations to hardware-validated implementations.

---

## 4. Suitability for Thanh's Ph.D. Goals

**Verdict: Highly Complementary.**

Thanh aims to solve modern grid stability issues and architect Physics-Informed AI frameworks. Prof. Hong’s lab provides the perfect "Security and Real-time Implementation" complement to Prof. Bui's "Markets and RL" focus. Because Thanh already possesses deep knowledge of rigorous physical models (MILP, SOCP), he is the ideal candidate to help Prof. Hong inject physical realities into cybersecurity AI. This combination of optimization theory and cyber-physical security is highly lucrative for both academic roles and R&D positions at National Labs (e.g., NREL, PNNL).

---

## 5. What Thanh Can Contribute (The Pragmatic Value of a Fresh Undergrad)

As a fresh graduate applying for a Ph.D., Thanh's core value to Prof. Hong is providing **rigorous mathematical modeling and power physics expertise** to ground the lab's AI security models.

1. **The "Physics Engine" for AI Security Models:** Prof. Hong’s GenAI and Physics-Informed ML algorithms require perfectly constrained physical environments to train and detect anomalies. Thanh possesses the coding stamina (Python, Pyomo) and mathematical background (SOCP, AC-OPF) to build these complex multi-microgrid environments. He can formulate the ground-truth physical equations that the AI uses to verify if an incoming signal is a cyberattack (FDIA) or a normal grid disturbance.
2. **Real-time Optimization Implementation:** Thanh's experience with Model Predictive Control (MPC) means he understands dynamic, rolling-horizon optimization. He can take Prof. Hong's high-level security detection ideas and implement the subsequent control actions—writing the code that tells the grid *how* to physically isolate a compromised node or re-route power in real-time.
3. **Bridging the IT-OT Gap:** When a cybersecurity AI model fails to detect an attack, it is often because it doesn't understand the physical correlation between buses. Thanh understands the underlying AC power flow physics and can independently debug the data, acting as the crucial translator between pure cybersecurity algorithms and grid physics.
