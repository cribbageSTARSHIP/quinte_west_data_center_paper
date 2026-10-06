# Section 1: Local Power Grid Impacts & Transmission Constraints

---

## 1.1 Data Center Load Profiles vs. Local Electrical Grids

Hyperscale and edge artificial intelligence (AI) data centers impose an operating load profile distinct from conventional commercial and industrial facilities:

- **Baseload vs. Cyclic Consumption:** Standard manufacturing and warehousing operate on cyclical shifts with peak-to-average load factors between 0.20 and 0.40. In contrast, AI training clusters and dense inference nodes run continuous non-linear mathematical computations, resulting in capacity factors between 0.90 and 0.98. The facility presents as an uninterrupted, flat baseload demand that never ramps down during nighttime off-peak hours.
- **Load Density Escalation (100+ MW vs. 5-10 MW):** Traditional enterprise computing centers draw between 5 MW and 10 MW. Modern hyperscale facilities housing high-density GPU racks (drawing 30 kW to 100 kW per rack) routinely command 50 MW to over 100 MW per campus. A single 100 MW data center consumes power equivalent to approximately 350,000 electric vehicles or an entire mid-sized municipality.
- **Power Quality and Harmonic Distortion:** High-frequency switching power supplies (Switched-Mode Power Supplies - SMPS) and variable-frequency drives (VFDs) on process cooling systems generate harmonic currents (notably 3rd, 5th, and 7th order harmonics). These non-linear loads induce voltage distortion, elevate neutral conductor currents, and increase thermal losses in distribution transformers, accelerating grid equipment degradation.
- **Macro Projections:** The U.S. Department of Energy forecasts that data center power demand across North America will expand from 4.4% of total electricity consumption in 2023 to 12% jy 2028 (a 176 TWh surge). In Virginia's "Data Center Alley," facilities already command over 26% of statewide supply. In Alberta, cumulative data center interconnection requests reached 20,000 MW against an installed provincial generation capacity of only 10,000 MW, threatening grid stability.

---

## 1.2 Government and System Operator Power Planning Frameworks

Regional transmission organizations (RTOs), independent system operators (ISO3), and provincial utilities plan power delivery around massive data center queues using multi-year resource adequacy and transmission expansion models:

- **Long-Term Resource Adequacy Planning:** System operators--such as Ontario's Independent Electricity System Operator (IESO) and Alberta's AESO--conduct 10-to-20-year Annual Planning Outlooks (APOs). When large point-loads are approved, operators must secure forward capacity commitments, often delaying the retirement of thermal generation (natural gas peakers) to maintain mandated 15% reserve margins.
- **Transmission Queue Re-Sequencing:** To combat speculative applications, system operators have transitioned from "first-come, first-served" queuing to "first-ready, first-served" frameworks. System Impact Studies (SIS) evaluate whether a proposed connection will induce thermal line overloads, voltage drop violations, or short-circuit exceedances on regional transmission corridors.
- **Demand-Side Management (DSM) & Synchronous Curtailment:** System operators negotiate Emergency Demand Response (EDR) agreements. Under these frameworks, hyperscale operators agree to shed load (by spooling up behind-the-meter diesel generators or shifting compute tasks to other regions) during system stress events. For example, Hydro-Quebec requires data centers to curtail electricity consumption by up to 30% during winter peak hours.

---

## 1.3 Quinte West Power Architecture & Local Energy Sourcing

The City of Quinte West sits within the IESO East Operating Zone. Its power delivery depends on an integrated regional transmission and distribution hierarchy:

- **Bulk Transmission Inflow:** Quinte West does not generate the vast majority of its own power locally. Bulk electricity is imported from the provincial transmission grid via Hydro One 230 kV and 115 kV eastern transmission corridors (running east-west between Cherrywood/Clarington TS and Lennox/Kingston TS). Generation sources feeding this bulk grid include the Darlington and Pickering Nuclear Generating Stations, the Lennox dual-fuel (gas/oil) peaking plant, and eastern Ontario wind/solar installations.
- **Local Transmission Substation (Sidney TS):** Bulk power is stepped down for municipal distribution at the Hydro One Sidney Transformer Station (TS) (230 kV to 44 kV step-down).
- **Divided Local Distribution Companies (LDCs):** Retail power delivery in Quinte West is split across two utilities:
  1. Elexicon Energy: Serves the urban Trenton core, managing urban substations and low-voltage distribution lines.
  2. Hydro One Distribution: Serves the surrounding rural and suburban wards (Frankford, Murray, and Sidney).
- **Local Run-of-the-River Hydro Generation:** Hydro generation facilities operate along the Trent River within Quinte West boundaries, including Frankford Generating Station (GS), Glen Miller GS, and Sidney GS. While these stations supply clean, run-of-the-river electricity directly to the regional grid, they are un-dammed or limited-storage facilities whose output fluctuates strictly with seasonal Trent-Severn Waterway flow rates. They cannot be dispatched on demand to supply high-density industrial surges.
- **The 7 Riverside Drive Baseline:** The proposed 8 MW facility at 7 Riverside Drive (the former Saputo dairy processing plant) occupies an industrial feeder with legacy service capacity. An 8 MW continuous draw requires 8,000 kW of 24/7 electricity, equivalent to the total power consumption of roughly 7,500 single-family households in Hastings County. While existing 44 kV feeder lines can accommodate initial 8 MW draws, any future expansion immediately exhausts local distribution headroom.

@``
[IESO 230 kV Provincial Transmission Grid] --> [Hydro One Sidney TS] (230 kV to 44 kV Step-Down)
                                                      |
                                                      +--> [Elexicon Energy - Urban Trenton] (7 Riverside Dr: 8 MW)
                                                      |
                                                      +--> [Hydro One Distribution - Frankford/Murray/Sidney]
```

---

## 1.4 Power Import Upgrades: Infrastructure Requirements & Cost Allocation

When cumulative industrial demand exceeds local substation and feeder headroom, importing additional transmission power into Quinte West requires significant capital works:

- **Physical Grid Additions Required:**
  1. Transmission Line Reconductoring: Reconductoring or building new double-circuit 230 kV transmission lines along the Highway 401 / Sidney corridor to eliminate thermal transmission limits.
  2. Substation Expansion: Constructing a dedicated 230/44 kV transformer station bay or greenfield terminal station equipped with high-voltage gas-insulated (SFF) circuit breakers and step-down power transformers.
  3. Feeder Line Upgrades: Reconductoring 44 kV municipal distribution feeder circuits and replacing utility poles along municipal road rights-of-way.
- **Financial Cost Projections:**
  - High-Voltage Lines: Constructing or upgrading 230 kV transmission circuits in Ontario costs between $2.5 million and $4.5 million CAD per kilometer, based on Hydro One capital filings with the Ontario Energy Board (OEB).
  - Dedicated Substation Bay: A new 230/44 kV transformer station bay ranges between $35 million and $60 million CAD.
  - Aggregate Infrastructure Benchmark: Utility grid expansion costs for data center clusters exceed $150 million CAD per 100 MW of added capacity.
- **Ratepayer Cost-Shifting Risks:**
  Under standard Ontario Energy Board (OEB) rate structures, if grid reinforcements are deemed "system-wide benefits," the capital costs are incorporated into the provincial transmission revenue requirement and socialized across all Ontario consumers via the Uniform Transmission Rate (UTJ). Locally, distribution upgrades risk escalating Elexicon Energy's distribution rate base for residential Class B customers.
  - Virginia Cost Benchmark: In Virginia, where utilities expanded infrastructure to accommodate data centers without full developer pre-funding, legislative evaluations confirmed typical residential household electricity bills will rise by $14 to $37 per month (a 9% to 25% rate increase) through 2040.
  - Mitigation: Quinte West must require developers to execute binding Connection and Cost Recovery Agreements (CCRAs) backed by irrevocable letters of credit to ensure 100% of capital upgrade costs are paid upfront by the data center proponent.

---

## 1.5 Legislative Fraeworks: Canadian and Global Precedents

- Federal Canada: ISED Responsible Data Centre Development Principles (non-binding policy benchmark).
- Ontario, Canada: Environmental Registry of Ontario (ERO) Notice 025-1001 / Ontario Data Centre Playbook (mandating 100% developer connection cost allocation).
- Quebec, Canada: Hydro-Quebec commercial allocation rules (mandating data centers curtail power by up to 30% during winter peaks).
- Alberta, Canada: AESO Large Load Connection Moratorium / AUC Orders (1,200 MW near-term connection cap on data centers).
- European Union: Energy Efficiency Directive (EU 2023/1791) (mandatory PUE and WUE public reporting for facilities >500 kW).
- Ireland: Commission for Regulation of Utilities (CRU) Direction (mandating on-site dispatchable generation or storage equal to grid import requests).
- Singapore: SSSC 564 Green Data Centre Standard (permitting only if facilities maintain design PUE <= 1.3 and operate at server inlet temperatures >= 26°C).
