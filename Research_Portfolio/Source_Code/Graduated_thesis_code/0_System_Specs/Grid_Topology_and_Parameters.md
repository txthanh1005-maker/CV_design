# Microgrids System Characteristics Summary

This P2P Energy Trading system consists of 1 Main Grid (MG0) and 4 Microgrids (MG1-MG4).

## 1. MG1 (Heaviest Load)
- **Size:** 36 Nodes.
- **Load:** ~6266 kWh/day (Peak: ~337 kW).
- **DERs:** PV at {3, 10, 12, 14, 26, 36} (max 61 kW/node); Wind at {32} (max 164 kW); DG at {5}; BESS at {19}.
- **P2P Links:** MG1(N15) <-> MG4(N14); MG1(N31) <-> MG3(N2).
- **Topology Paths:**
  - 1-2-3
  - 1-4-5-6-9-10
  - 1-4-5-6-7-8
  - 1-4-5-11-12
  - 1-4-5-11-13-14
  - 1-4-5-11-13-15-18-19-33-34
  - 1-4-5-11-13-15-18-19-33-35-36
  - 1-4-5-11-13-15-18-19-20-21
  - 1-4-5-11-13-15-18-19-20-22-23
  - 1-4-5-11-13-15-18-19-20-22-24-25-26
  - 1-4-5-11-13-15-18-19-20-22-24-27-28
  - 1-4-5-11-13-15-18-19-20-22-24-27-29-30-31-32
  - 1-4-5-11-13-15-16-17

## 2. MG2 (Solar Only)
- **Size:** 30 Nodes.
- **Load:** ~5847 kWh/day (Peak: ~315 kW).
- **DERs:** PV at {14, 19, 28, 30} (max 61 kW/node); No Wind; DG at {10}; BESS at {20}.
- **P2P Links:** MG2(N15) <-> MG3(N17); MG2(N11) <-> MG4(N35).
- **Topology Paths:**
  - 1-2-3-4-5
  - 1-2-3-6-7-8
  - 1-2-3-6-7-9-10-20-21-22
  - 1-2-3-6-7-9-10-20-21-23-24
  - 1-2-3-6-7-9-10-20-21-23-25-26
  - 1-2-3-6-7-9-10-20-21-23-25-27-28
  - 1-2-3-6-7-9-10-20-21-23-25-27-29-30
  - 1-2-3-6-7-9-10-11-12-13-14
  - 1-2-3-6-7-9-10-11-15-16-17-18-19

## 3. MG3 (Compact & Low Load)
- **Size:** 21 Nodes.
- **Load:** ~2458 kWh/day (Peak: ~140 kW).
- **DERs:** PV at {2, 8, 11, 15} (max ~41 kW/node); Wind at {1} (max ~109 kW); DG at {9}; BESS at {12}.
- **P2P Links:** MG3(N2) <-> MG1(N31); MG3(N17) <-> MG2(N15); MG3(N16) <-> MG4(N30). Acts as an intermediary coordinator and potential main power exporter due to low load vs high generation.
- **Topology Paths:**
  - 1-2-3-4-5
  - 1-2-3-4-6-7-8
  - 1-2-9-10-11
  - 1-2-9-12-13-14-15
  - 1-2-9-12-16-17-18-19-20-21

## 4. MG4 (Heavy Traditional Generation)
- **Size:** 35 Nodes.
- **Load:** ~5433 kWh/day (Peak: ~299 kW).
- **DERs:** PV at {18, 20, 27, 29}; No Wind; 2 DGs at {22, 34}; BESS at {8}.
- **P2P Links:** MG4(N14) <-> MG1(N15); MG4(N30) <-> MG3(N16); MG4(N35) <-> MG2(N11).
- **Topology Paths:**
  - 0-1-6
  - 0-1-2-5
  - 0-1-2-3-4
  - 0-1-7-8-9
  - 0-1-7-8-10-11-12
  - 0-1-7-8-10-11-13
  - 0-1-7-8-14-19-20-21-22-23-24
  - 0-1-7-8-14-19-20-21-22-25-26-27
  - 0-1-7-8-14-19-20-21-22-25-28-35
  - 0-1-7-8-14-19-20-21-22-25-28-34
  - 0-1-7-8-14-19-20-21-22-25-28-29-30-31-32-33
  - 0-1-7-8-14-15-16-18
  - 0-1-7-8-14-15-16-17

## Key Insights
1. **Strategic Imbalance:** MG1/MG2 have high loads; MG3 has low load but high renewables. This imbalance perfectly motivates the ADMM-based P2P trading.
2. **MG4's Role:** With two DGs and no wind, MG4 can ramp up traditional generation during high P2P prices to export or self-supply.
3. **Mesh Topology:** The P2P links between MGs create a mesh structure rather than a star, improving reliability but adding complexity to the ADMM dual variable ($\lambda$) updates.
