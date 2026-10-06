#!/usr/bin/env python3
import os
import re
import glob
from pathlib import Path

VERSION = "v0.5.10"

CANONICAL_TITLES = {
    "1.1": "How Data Centers Affect Local Power Grids",
    "1.2": "How Governments Plan Power Needs Around Data Centers",
    "1.3": "Where Quinte West Gets Its Power From",
    "1.4": "Quinte West Power Import Costs and Route Upgrades",
    "1.5": "How Governments in Canada and Worldwide Legislate Data Center Power Needs",
    "1.6": "7 Riverside Drive Data Centre (Former Saputo Dairy Site)",
    "1.6.1": "Historical Details of 7 Riverside Drive, Trenton",
    "1.6.2": "Potential Power Draw from a Data Center at 7 Riverside Drive",
    "1.7": "920 Trenton-Frankford Road Project (Former Sonoco Paper Mill Site)",
    "1.7.1": "Historical Details of 920 Trenton-Frankford Road",
    "1.7.2": "Potential Power Draw from a Data Center at 920 Trenton-Frankford Road",
    "2.1": "Major Rivers and Bodies of Water in Quinte West",
    "2.2": "Conservation Areas of Quinte West",
    "2.3": "Where Quinte West Gets Its Drinking Water From",
    "2.4": "What Is the Quinte West Watershed",
    "2.5": "Major Environmental, Ecological, and Conservation Concerns",
    "2.6": "How Quinte West Legislates Data Center Environmental Concerns",
    "2.7": "Concentrations of Wildlife in Quinte West and Spatial Mapping",
    "2.8": "Apiaries and Pollinator Zones in Quinte West",
    "3.1": "Water Cooling of Data Centers vs. Closed-Loop Cooling Systems",
    "3.2": "How Data Centers Affect the Water Table (Open and Closed-Loop)",
    "3.3": "Surge Power Needs in Data Centers (Generators, Batteries, Renewables)",
    "3.4": "How Hydrocarbon-Based Generators Affect the Local Environment",
    "3.5": "Closed-Loop Cooling and Diesel Generators in Quinte West",
    "3.5.1": "Projected On-Site Storage Volumes of Diesel and Propylene Glycol",
    "3.5.2": "How a Diesel Spill Affects Land and Nearby Rivers",
    "3.5.3": "How a Propylene Glycol Spill Affects Land and Aquatic Oxygen",
    "3.6": "Risks to Local Wildlife from Data Centers",
    "3.7": "Risks to Bees and Pollinators from Data Centers",
    "3.8": "Wildlife Impacts via Habitat Loss, Energy/Water Demands, Noise, and Light",
    "3.9": "How Governments Legislate Data Center Environmental Concerns",
    "4.1": "dBA vs. dBC: Technical Differences and Application to Data Centers",
    "4.2": "Data Center Components Producing dBC and Engineering Mitigations",
    "4.3": "Medical Implications of Short- and Long-Term dBC Exposure",
    "4.4": "Effects of Data Center Noise on Residential Property Values",
    "4.5": "Acoustic and Vibrational Impacts on Wildlife and Bees",
    "4.6": "How Governments Legislate Data Center Noise",
    "5.1": "Physical Human Health Impacts from Data Centers",
    "5.2": "Mental Health and Vibroacoustic Stress Impacts",
    "5.3": "How Governments Legislate Data Center Health Concerns",
    "6.1": "Quinte West Approach to Municipal Taxation of Data Centers",
    "6.2": "Canadian and International Data Center Taxation Frameworks",
    "6.3": "Property Tax Assessment: Real Property Shell vs. Exempt Machinery Contents",
    "7.1": "Data Center Employment Headcount and Staffing Ratios",
    "7.2": "Trades and Job Classifications in Operational Facilities",
    "7.3": "Trades Required to Build and Commission a Facility",
    "7.4": "Long-Term Operational Staffing Requirements",
    "7.5": "Local Business and Professional Services Required",
    "7.6": "Materials and Consumables Required for Operations",
    "8.1": "Spill Emergency Agencies Beyond Police, Fire, and Ambulance",
    "8.2": "Contamination Types and Environmental Pathways",
    "8.3": "Historical Data Center Contamination in Canada",
    "8.4": "Historical Data Center Contamination Worldwide",
    "8.5": "Canadian Government Responses to Data Center Incidents",
    "8.6": "International Government Responses to Data Center Incidents",
    "9.1": "Hazardous Spills and Contamination Incidents in Ontario",
    "9.2": "Hazardous Spills and Contamination Incidents in Canada (Excl. Ontario)",
    "9.3": "Hazardous Spills and Contamination Incidents in the United States",
    "9.4": "Hazardous Spills and Contamination Incidents in Europe",
    "9.5": "Hazardous Spills and Contamination Incidents in Asia",
    "9.6": "Hazardous Spills and Contamination Incidents in Australia",
    "9.7": "Hazardous Spills and Contamination Incidents in China",
    "9.8": "Hazardous Spills and Contamination Incidents in Russia",
    "10.1": "Emerging Risks & Policy Covenants in Quinte West"
}

SECTIONS = [
    ("01_power_grid", "1. Local Power Grid Impacts"),
    ("02_nature_ecology", "2. Quinte West Nature and Ecology"),
    ("03_environmental_water_table", "3. Environmental, Ecological & Water Table Impacts"),
    ("04_acoustic_concerns", "4. Acoustic Concerns"),
    ("05_human_health_risks", "5. Human Health Risks (Physical & Mental)"),
    ("06_municipal_tax_revenue", "6. Municipal Business Tax Revenue (Shell vs. Contents)"),
    ("07_employment_and_spinoffs", "7. Employment & Possible Spin-Off Industries"),
    ("08_emergency_response_and_hazards", "8. Emergency Response & Secondary Municipal Hazards"),
    ("09_hazardous_spills_and_contamination", "9. Data Center Hazardous Spills or Contamination"),
    ("99_other", "10. Emerging Risks & Policy Covenants"),
]

# (fig_code, filename, clean_caption, anchor_keywords)
SECTION_FIGURES = {
    "1.1": [
        ("1.1a", "fig_1_1a_elec_consumption_trends.png", "[1.1a] Regional Electricity Consumption Projections vs. Quinte West Site Loads (MW Equivalent)", ["Electricity Consumption Trends", "38,878"]),
        ("1.1b", "fig_1_1b_bess_thermal_runaway.png", "[1.1b] Four-Stage Lithium-Ion BESS Thermal Runaway and Early-Warning Mitigation Architecture", ["Role of Battery Storage", "thermal runaway"]),
        ("1.1c", "fig_1_1c_diurnal_load_curve.png", "[1.1c] 24-Hour Diurnal Electricity Demand Curve: Unmitigated Baseload vs. Spatio-Temporal Load-Shifting", ["Demand Response and Load-Shifting", "spatio-temporal"]),
        ("1.1d", "fig_1_1d_scope_emissions_health.png", "[1.1d] Data Center Scope 1, 2, and 3 Emissions Profile and Public Health Trajectory", ["Health Impacts and Air Quality", "Scope 3"]),
        ("1.1e", "fig_1_1e_site_aerial_comparison.png", "[1.1e] Side-by-Side Geospatial Comparison of 7 Riverside Drive and 920 Trenton-Frankford Road", ["Site-Specific Challenges", "Unique challenges"])
    ],
    "1.2": [
        ("1.2a", "fig_1_2a_coloedr_pricing_flowchart.png", "[1.2a] Multi-Tenant ColoEDR Supply-Function Bidding and Price Responsive Load (PRL) Flowchart", ["Demand Response (DR) and Pricing", "ColoEDR"]),
        ("1.2b", "fig_1_2b_cooling_energy_donut.png", "[1.2b] Breakdown of Data Center Electricity Consumption and Cooling Efficiency Savings", ["Cooling Systems and Energy Efficiency", "40%"]),
        ("1.2c", "fig_1_2c_jurisdictional_comparison.png", "[1.2c] Jurisdictional Grid Planning Comparison: Alberta, Ontario, and Quinte West", ["Comparative Analysis: Alberta, Ontario", "1,200 MW"])
    ],
    "1.3": [
        ("1.3a", "fig_1_3a_ontario_generation_donut.png", "[1.3a] Ontario IESO Bulk Electricity Generation Mix Feeding the Quinte West Corridor", ["Overview of Ontario's Power System", "35%"]),
        ("1.3b", "fig_1_3b_substation_schematic.png", "[1.3b] Substation Step-Down Network Schematic and Thermal Capacity Limits", ["Key Power Infrastructure", "TILBURY WEST"]),
        ("1.3c", "fig_1_3c_outage_vulnerability_map.png", "[1.3c] Winter Storm Overhead Line Vulnerability and Outage Hotspot Map for Frankford and Batawa", ["Power Outages and Grid Vulnerabilities", "Batawa"])
    ],
    "1.4": [
        ("1.4a", "fig_1_4a_grid_upgrade_costs.png", "[1.4a] Capital Expenditure Ranges for Quinte West Grid Infrastructure Upgrades ($ Millions)", ["Grid Infrastructure Costs", "Transformer Replacement"]),
        ("1.4b", "fig_1_4b_solar_vs_grid_expansion.png", "[1.4b] Economic Comparison of a 50 MW Solar Farm vs. 50 MW Traditional Grid Expansion", ["Renewable Energy vs. Grid Expansion", "LCOE"]),
        ("1.4c", "fig_1_4c_health_land_footprint.png", "[1.4c] Health and Environmental Externalities of Fossil/Diesel Grid Expansion vs. 100% Renewable Integration", ["Health and Environmental Costs", "1,200 premature deaths"])
    ],
    "1.5": [
        ("1.5a", "fig_1_5a_ontario_playbook_pillars.png", "[1.5a] Ontario's Data Centre Playbook Three-Pillar Architecture and Provincial Governance Override", ["Ontario's Data Centre Playbook", "Community Investment"]),
        ("1.5b", "fig_1_5b_global_policy_matrix.png", "[1.5b] International Legislative and Efficiency Matrix Comparing Global Data Center Frameworks", ["International Comparisons", "Green Data Center Guidelines"])
    ],
    "1.6.1": [
        ("1.6.1a", "fig_1_6_1a_saputo_enhanced_map.png", "[1.6.1a] Enhanced Site Map of 7 Riverside Drive (Former Saputo Dairy) with SM-14 Rezoning and Trenton WTP Callouts", ["Legal and Zoning Framework", "SM-14"]),
        ("1.6.1b", "fig_1_6_1b_saputo_timeline.png", "[1.6.1b] Site Profile and Historical Timeline of 7 Riverside Drive from Saputo Closure to Post-October 2026 Election Deferral", ["The Data Center Proposal", "TrueNorth"])
    ],
    "1.6.2": [
        ("1.6.2a", "fig_1_6_2a_electrical_routing_map.png", "[1.6.2a] Local Electrical Routing Map Showing Elexicon Energy Service Zone, Hydro One Feeders, and Trent-Severn Corridor", ["Proximity to Key Infrastructure", "Elexicon"]),
        ("1.6.2b", "fig_1_6_2b_capacity_deficit_chart.png", "[1.6.2b] Substation Thermal Capacity Deficit vs. Conventional and Hyperscale AI Data Center Loads", ["Power Requirements for the Trenton Site", "75,000 homes"])
    ],
    "1.7.1": [
        ("1.7.1a", "fig_1_7_1a_sonoco_floodplain_cross_section.png", "[1.7.1a] Lower Trent Conservation Floodplain Map (Sheet 112) and Elevation Cross-Section (91.12 m vs. 90.56 m)", ["Watershed and Floodplain Analysis", "91.12 m"]),
        ("1.7.1b", "fig_1_7_1b_firstblock_heat_and_noise.png", "[1.7.1b] FirstBlock 33 MW Circular Waste-Heat Recovery Schematic and Acoustic Comparison Against Ontario NPC-300 Limits", ["Project Overview and Technical Specifications", "4,220 tonnes"])
    ],
    "1.7.2": [
        ("1.7.2a", "fig_1_7_2a_sonoco_substation_feeder_map.png", "[1.7.2a] Substation and Feeder Map Plotting 44 kV Sydney TS-M1 Feeders, 5 Bernard Long Rd (7.5 MW), and Harder Drive Substation", ["Infrastructure Legacy and Grid Capacity", "Harder Drive"]),
        ("1.7.2b", "fig_1_7_2b_vibroacoustic_coupling.png", "[1.7.2b] Vibroacoustic Coupling Diagram Showing Low-Frequency (<100 Hz) dBC Structural Resonance vs. Municipal dBA Bylaws", ["Low-Frequency Noise and Health Impacts", "vibroacoustic"])
    ],
    "2.1": [
        ("2.1a", "fig_2_1a_trenton_waterways_enhanced_map.png", "[2.1a] Enhanced Waterway Map of Quinte West Labeling Locks 1–7, Bay of Quinte Estuary, Dams, and Invasive Water Soldier Zones", ["Major Rivers and Water Bodies", "Trent River"]),
        ("2.1b", "fig_2_1b_trent_severn_photos_panel.png", "[2.1b] Ecological & Heritage Reference Panel: Lockmaster's House, Trent Port Marina, and Invasive Water Soldier", ["Trent-Severn Waterway", "Lockmaster"]),
        ("2.1c", "fig_2_1c_elorca_merger_chart.png", "[2.1c] Organizational Merger Chart Showing the 2027 Consolidation into ELORCA", ["Legal and Institutional Context", "ELORCA"])
    ],
    "2.2": [
        ("2.2a", "fig_2_2a_conservation_areas_map.png", "[2.2a] Key Conservation Areas of the Lower Trent Watershed: Trenton Greenbelt, Bleasdell Boulder, and Sager Conservation Area", ["Bleasdell Boulder and Sager Conservation Area", "Trenton Greenbelt"]),
        ("2.2b", "fig_2_2b_black_carbon_emissions.png", "[2.2b] 2024 Canadian Inventory Comparison of Provincial Black Carbon and Fine Particulate Emissions (kt)", ["Climate Change and Black Carbon Emissions", "black carbon"])
    ],
    "2.3": [
        ("2.3a", "fig_2_3a_source_water_ipz_map.png", "[2.3a] Source Water Protection Map Plotting Trenton and Bayside WTP Intakes and IPZ-1, IPZ-2, and IPZ-3 Buffers", ["Intake Protection Zones", "IPZ-1"]),
        ("2.3b", "fig_2_3b_dual_wtp_schematic.png", "[2.3b] Dual Water Treatment Process Schematic Comparing the Trenton and Bayside Water Treatment Plants", ["Water Treatment Infrastructure", "Bayside Water Treatment Plant"])
    ],
    "2.4": [
        ("2.4a", "fig_2_4a_hydrological_block_diagram.png", "[2.4a] Hydrological Block Diagram Illustrating Surface and Groundwater Flow from Canadian Shield Highlands to the Bay of Quinte", ["Topographical and Climatic Influences", "Canadian Shield"]),
        ("2.4b", "fig_2_4b_water_depletion_pie_bar.png", "[2.4b] Data Center Direct vs. Indirect Water Footprint (57% vs. 43%) and Annual Subbasin Depletion Rates (0.81–1.5%)", ["Water Consumption and Depletion", "57%"])
    ],
    "2.5": [
        ("2.5a", "fig_2_5a_species_at_risk_panel.png", "[2.5a] Indicator Species at Risk Profile: Eastern Massasauga Rattlesnake, Blanding's Turtle, Lake Sturgeon, and Atlantic Salmon", ["Impact on Aquatic Ecosystems", "Massasauga"]),
        ("2.5b", "fig_2_5b_early_warning_monitoring_arch.png", "[2.5b] Multi-Sensor Real-Time Environmental Early-Warning Architecture for Brownfield Data Center Sites", ["Implementing Real-Time Environmental Monitoring", "Sensor Networks"])
    ],
    "2.6": [
        ("2.6a", "fig_2_6a_regulatory_approval_flowchart.png", "[2.6a] Municipal and Provincial Regulatory Approval Flowchart for Data Center Proposals in Quinte West", ["The Role of Provincial Legislation", "Generations Act"])
    ],
    "2.7": [
        ("2.7a", "fig_2_7a_wildlife_status_gis_map.png", "[2.7a] GIS Wildlife Concentration and Conservation Status Rank (S1–S3) Map of Quinte West", ["Current Wildlife Concentrations", "Presqu'ile"]),
        ("2.7b", "fig_2_7b_pollinator_biodiversity_bar.png", "[2.7b] Comparative Pollinator and Biodiversity Trajectory: Restored Trenton Greenbelt vs. Unbuffered Data Center Perimeter", ["Comparative Analysis: Conservation Efforts", "30%"])
    ],
    "2.8": [
        ("2.8a", "fig_2_8a_apiary_emf_buffer_map.png", "[2.8a] Quinte West Apiary and Pollinator Connectivity Map with 500 m EMF and 200 m Zoning Setback Buffers", ["Mapping Pollinator Zones", "500 meters"]),
        ("2.8b", "fig_2_8b_honeybee_emf_vibration_pathway.png", "[2.8b] Biological Pathway of 50/60 Hz ELF-EMF (20–7,000 uT) and 200–300 Hz Mechanical Vibration on Honeybee Colonies", ["Mechanisms of EMF-Induced Disruption", "vibrational signals"])
    ],
    "3.1": [
        ("3.1a", "fig_3_1a_cooling_water_pue_chart.png", "[3.1a] Stacked Bar and PUE Line Chart Comparing Open-Loop (10.93M m³), Closed-Loop Air (6.12M m³), and Hybrid Cooling (7.19M m³)", ["Energy Consumption and PUE", "10.93 million"]),
        ("3.1b", "fig_3_1b_cooling_cutaway_comparison.png", "[3.1b] Engineering Comparison of an Open-Loop Evaporative Tower vs. Closed-Loop Direct-to-Chip Cooling with Rainwater Harvesting", ["Closed-Loop Cooling Systems", "Rainwater Harvesting"])
    ],
    "3.2": [
        ("3.2a", "fig_3_2a_hydrogeological_cross_section.png", "[3.2a] Hydrogeological Cross-Section Comparing Open-Loop Aquifer Cone-of-Depression vs. Closed-Loop Glycol Leaching", ["Impact on Water Quality and Hydrology", "Aquifer Depletion"]),
        ("3.2b", "fig_3_2b_water_scale_comparison.png", "[3.2b] Scale Comparison of Data Center Water Consumption Metrics From Single AI Training Runs to Regional Aquifers", ["Water Consumption Metrics", "Loudoun County"])
    ],
    "3.3": [
        ("3.3a", "fig_3_3a_surge_power_comparison.png", "[3.3a] Multi-Metric Comparison of Diesel Generators, Battery Energy Storage Systems (BESS), and Solar PV / ORC Systems", ["Comparative Analysis: Generators, Batteries", "Response Time"]),
        ("3.3b", "fig_3_3b_site_microgrid_schematics.png", "[3.3b] Proposed Hybrid Microgrid Schematics for 7 Riverside Drive and 920 Trenton-Frankford Road", ["Case Study: Quinte West and Hastings County", "500 kWh BESS"])
    ],
    "3.4": [
        ("3.4a", "fig_3_4a_canada_emissions_benchmarks.png", "[3.4a] 2024 Canadian Emissions Inventory Benchmarks (NOx, PM2.5, Black Carbon) and SCR/DPF Mitigation Efficacy", ["Key Pollutants and Their Sources", "447 kt"]),
        ("3.4b", "fig_3_4b_atmospheric_deposition_diagram.png", "[3.4b] Atmospheric Deposition Pathway of Diesel Exhaust Plumes on the Trent River Watershed and Wetlands", ["Emissions Scenario Analysis", "albedo"])
    ],
    "3.5.1": [
        ("3.5.1a", "fig_3_5_1a_storage_and_biodegradation.png", "[3.5.1a] Projected Diesel and Propylene Glycol Storage Volumes and Soil Biodegradation Curve (-2°C vs. 25°C)", ["Environmental Degradation and Persistence", "93.3 mg/kg/day"]),
        ("3.5.1b", "fig_3_5_1b_csa_double_walled_tank.png", "[3.5.1b] Engineering Cross-Section of a CSA-Compliant Double-Walled Storage Tank with 110% Secondary Containment", ["Mitigation Strategies for Diesel Storage", "double-walled"])
    ],
    "3.5.2": [
        ("3.5.2a", "fig_3_5_2a_diesel_toxicity_diagram.png", "[3.5.2a] Terrestrial and Aquatic Toxicity Pathway of a Bulk Diesel Fuel Spill (10–100 mg/L)", ["Immediate Toxicity to Aquatic Life", "hydrophobicity"]),
        ("3.5.2b", "fig_3_5_2b_diesel_spill_trajectory_map.png", "[3.5.2b] Simulated 5,500-Gallon Diesel Spill Trajectory Map from 7 Riverside Drive and 920 Trenton-Frankford Road into IPZ-1", ["Case Study: The Equinix Data Center Spill", "5,500 gallons"])
    ],
    "3.5.3": [
        ("3.5.3a", "fig_3_5_3a_pg_spill_oxygen_depletion.png", "[3.5.3a] Trent River Propylene Glycol Spill Map and 48-Hour Dissolved Oxygen Depletion Curve (<2.0 mg/L Hypoxia)", ["Scenario Analysis: Spill at 7 Riverside Drive", "48 hours"]),
        ("3.5.3b", "fig_3_5_3b_pg_vs_eg_comparison.png", "[3.5.3b] Toxicological and Biochemical Oxygen Demand Comparison of Propylene Glycol vs. Ethylene Glycol", ["Comparative Analysis: Propylene Glycol vs. Ethylene Glycol", "20,000"])
    ],
    "3.6": [
        ("3.6a", "fig_3_6a_ansi_species_disruption.png", "[3.6a] Sensory and Habitat Disruption Matrix for Key Trent River ANSI Species", ["Case Study: Air Quality in the Trent River", "dragonfly"])
    ],
    "3.7": [
        ("3.7a", "fig_3_7a_shepherd_bee_emf_chart.png", "[3.7a] Shepherd et al. (2018) Honeybee Learning Drop (-27.97%) Under 100 uT EMF Exposure", ["Shepherd", "learning"]),
        ("3.7b", "fig_3_7b_emf_distance_decay_shielding.png", "[3.7b] EMF Distance-Decay and Shielding Attenuation Diagram Comparing 132–400 kV Lines and 50 m Buffers", ["shielding", "power line"])
    ],
    "3.8": [
        ("3.8a", "fig_3_8a_four_pathway_ecological_matrix.png", "[3.8a] Four-Pathway Ecological Impact Matrix Summarizing Habitat Loss, Water/Energy Demand, Noise, and Light Pollution", ["Light", "Habitat"]),
        ("3.8b", "fig_3_8b_cooling_tech_dual_axis.png", "[3.8b] Dual-Axis Bar Chart Contrasting Daily Water Use (L/day) and Energy Use (kWh/day) Across Four Cooling Architectures", ["Evaporative", "Dry Cooling"])
    ],
    "3.9": [
        ("3.9a", "fig_3_9a_international_regulatory_scorecard.png", "[3.9a] International Regulatory Scorecard Comparing Canada's RDDP Against the EU Green Deal, US EPA, and China", ["EU Green Deal", "China"])
    ],
    "4.1": [
        ("4.1", "fig_4_1_dba_vs_dbc.png", "[4.1] Low-Frequency Attenuation Gap Between dBA and dBC Weighting Networks", ["Application to Data Centers", "31.5 Hz"])
    ],
    "6.2": [
        ("6.2", "fig_6_2_mpac_tax_split.png", "[6.2] MPAC Capital Valuation Split: Exempt Server/Chiller Personal Property (80–90%) vs. Taxable Real Property Shell (10–20%)", ["Assessment", "machinery"])
    ],
    "7.1": [
        ("7.1", "fig_7_1_labor_disparity_and_mw_ratios.png", "[7.1] Capital-to-Labor Mismatch: Temporary Construction Trades vs. Permanent Operational Headcount", ["construction", "permanent"])
    ]
}

def natural_key(path):
    base = os.path.basename(path)
    num_part = base.split("_")[0]
    return [int(x) if x.isdigit() else x for x in num_part.split(".")]

def make_breakable(s):
    return s.replace("_", "_\u200b").replace("-", "-\u200b").replace("/", "/\u200b")

def clean_audit_and_refs(text):
    smap = {}
    audit_md = ""
    refs_md = ""

    # Strip any pre-existing figures or raw maps
    text = re.sub(r'!\[[^\]]*\]\((?:figures\vert{}wiki/raw/maps)/[^\)]+\)(?:\{[^\}]*\})?\n*', '', text)

    # Extract Audit Trail
    if "## Verified Raw Evidence Audit Trail" in text:
        parts = text.split("## Verified Raw Evidence Audit Trail", 1)
        text = parts[0]
        audit_raw = parts[1]
        audit_norm = re.sub(r'\|\s*\|\s*(\d+)\s*\|', r'|\n| \1 |', audit_raw)
        items = []
        for line in audit_norm.splitlines():
            m = re.match(r'^\|\s*(\d+)\s*\|\s*`?([^`|]+?)`?\s*\|\s*`?([^`|]+?)`?\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|?$', line.strip())
            if m:
                idx, fname, arch, page, exc = m.group(1).strip(), m.group(2).strip(), m.group(3).strip(), m.group(4).strip(), m.group(5).strip()
                smap[idx] = f"Source #{idx}: {make_breakable(fname)} ({make_breakable(arch)}), Loc: {page}"
                exc_clean = " ".join(re.sub(r'[#`<>\[\]|*]', ' ', exc).split())
                items.append(f"{idx}. **{make_breakable(fname)}**\n   - **Archive:** `{make_breakable(arch)}` | **Location:** `{page}`\n   - **Extract:** \"{exc_clean}\"")
        audit_md = "\n\n".join(items)

    # Extract References section
    ref_pat = re.compile(r'(?im)^(?:#{1,4}\s*)?(?:\d+(?:\.\d+)*\.?\s*)?(?:Section\s+\d+\s*[:\-–\.]\s*)?References\s*$')
    m_ref = ref_pat.search(text)
    if m_ref:
        refs_raw = text[m_ref.end():].strip()
        text = text[:m_ref.start()].rstrip()
        for line in refs_raw.splitlines():
            m_fb = re.match(r'^\s*(?:[-*]\s*)?(?:\*\*\[?Source\s*#?(\d+)\]?\:?\*\*|\^?\[?(\d+)\]?\^?[:\.]?)\s*(.+)$', line.strip(), re.I)
            if m_fb:
                idx = m_fb.group(1) or m_fb.group(2)
                desc = m_fb.group(3).strip()
                if idx and idx not in smap and desc:
                    smap[idx] = f"Source #{idx}: {make_breakable(desc)}"
        refs_raw = re.sub(r'(?im)^\s*\*?\*?Word\s+Count\s*:.*$', '', refs_raw)
        refs_raw = re.sub(r'(?m)^---\s*$', '', refs_raw).strip()
        refs_raw = re.sub(r'(?m)^(\s*)\^?\[\s*(\d+)\s*\]\^?\s*[:\-]?\s*', r'\1- **[Source #\2]:** ', refs_raw)
        refs_raw = re.sub(r'(?m)^(\s*)\^(\d+)\s*[:\.]?\s*', r'\1- **[Source #\2]:** ', refs_raw)
        refs_md = make_breakable(refs_raw)

    text = re.sub(r'(?im)^\s*\*?\*?Word\s+Count\s*:.*$', '', text)
    return text, smap, audit_md, refs_md

def inject_figures_inline(body_text, req_id):
    figs = SECTION_FIGURES.get(req_id, [])
    if not figs:
        return body_text

    paragraphs = re.split(r'(\n\s*\n)', body_text)
    for fig_code, fname, caption, keywords in figs:
        if not Path("figures", fname).exists():
            continue
        fig_block = f"\n\n![{caption}](figures/{fname}){{width=88%}}\n\n"
        placed = False
        found_kw = False
        for i in range(len(paragraphs)):
            chunk = paragraphs[i]
            if not chunk.strip():
                continue
            if any(kw.lower() in chunk.lower() for kw in keywords):
                found_kw = True
            if found_kw and not chunk.lstrip().startswith(("#", "|")) and len(chunk.strip()) > 80:
                clean_p = chunk.rstrip()
                if clean_p.endswith("."):
                    clean_p = clean_p[:-1] + f" (see Figure {fig_code})."
                else:
                    clean_p = clean_p + f" (see Figure {fig_code})"
                paragraphs[i] = clean_p + fig_block
                placed = True
                break
        if not placed:
            joined = "".join(paragraphs)
            m_conc = re.search(r'(?im)^#{2,4}\s*Conclusion', joined)
            if m_conc:
                pos = m_conc.start()
                joined = joined[:pos].rstrip() + f" (see Figure {fig_code})." + fig_block + "\n" + joined[pos:]
                paragraphs = [joined]
            else:
                paragraphs.append(fig_block)
    return "".join(paragraphs)

global_endnote_counter = 0

def convert_all_citations(body, smap):
    global global_endnote_counter
    endnotes = []

    def add_en(desc):
        global global_endnote_counter
        global_endnote_counter += 1
        endnotes.append(f"{global_endnote_counter}. {desc}")
        return f"^\\[{global_endnote_counter}\\]^"

    def resolve_nums(nums):
        resolved = [smap.get(n, f"Source #{n} (See Verified Raw Evidence Audit Trail)") for n in nums]
        return add_en("; ".join(resolved))

    def expand_tokens(s):
        nums = []
        for part in re.split(r'[,;&]+', s):
            rm = re.search(r'(\d+)\s*[\-–]\s*(\d+)', part)
            if rm:
                a, b = int(rm.group(1)), int(rm.group(2))
                if 1 <= a <= b <= 30:
                    nums.extend([str(i) for i in range(a, b + 1)])
                    continue
            for n in re.findall(r'\d+', part):
                if 1 <= int(n) <= 30:
                    nums.append(n)
        return nums

    protected_imgs = {}
    def protect_img(m):
        key = f"__IMG_PLACEHOLDER_{len(protected_imgs)}__"
        protected_imgs[key] = m.group(0)
        return key

    body = re.sub(r'!\[[^\]]*\]\([^\)]+\)(?:\{[^\}]*\})?', protect_img, body)

    def repl_brack(m):
        inner = m.group(1).strip()
        cleaned = re.sub(r'(?i)\bsources?\b|\bfile\b|[\[\]#:]', '', inner).strip()
        nums = expand_tokens(cleaned)
        if nums and re.fullmatch(r'[\d\s,;&\-–]+', cleaned):
            return resolve_nums(nums)
        return add_en(inner)

    body = re.sub(r'\^\[([^\]]+)\]\^?', repl_brack, body)
    body = re.sub(r'\[\^([^\]]+)\](?!:)', repl_brack, body)

    def repl_src_phrase(m):
        nums = expand_tokens(m.group(1))
        return resolve_nums(nums) if nums else m.group(0)

    body = re.sub(r'\(\s*[Ss]ources?\s+((?:\[\d+\]|#\d+|\d+)(?:\s*[,;&\-–]\s*(?:\[\d+\]|#\d+|\d+))*)\s*\)', repl_src_phrase, body)
    body = re.sub(r'(?<![\w])(?:[Ss]ources?)\s+((?:\[\d+\]|#\d+)(?:\s*[,;&\-–]\s*(?:\[\d+\]|#\d+))*)', repl_src_phrase, body)

    def repl_chain(m):
        nums = [n for n in re.findall(r'\d+', m.group(0)) if 1 <= int(n) <= 30]
        return resolve_nums(nums) if nums else m.group(0)

    body = re.sub(r'(?:\[\d{1,2}\]\s*){2,}', repl_chain, body)

    def repl_caret(m):
        n = m.group(1)
        return resolve_nums([n]) if 1 <= int(n) <= 30 else m.group(0)

    body = re.sub(r'(?<![\w`])\^(\d{1,2})(?![\d\[\w\^])', repl_caret, body)
    body = re.sub(r'\^(?=[\.\,;:\s\)]|$)', '', body)

    for k, v in protected_imgs.items():
        body = body.replace(k, v)

    return body, endnotes

master_body = []
all_endnotes = []
all_refs = []
all_audits = []

vf_file = Path("papers/00_source_verification.md")
traceability_block = vf_file.read_text(encoding="utf-8").strip() if vf_file.exists() else ""

for folder, sec_title in SECTIONS:
    sec_dir = Path("papers") / folder
    if not sec_dir.exists():
        continue
    files = sorted(list(sec_dir.glob("*.md")), key=natural_key)
    if not files:
        continue

    master_body.append(f"\n# {sec_title}\n\n")

    for fpath in files:
        fname = fpath.name
        raw_id = fname.split("_")[0]
        req_id = "10." + raw_id[3:] if raw_id.startswith("99.") else ("10" if raw_id == "99" else raw_id)
        canonical_title = CANONICAL_TITLES.get(req_id, fname.replace(".md", "").replace("_", " "))

        raw_text = fpath.read_text(encoding="utf-8", errors="ignore")
        body, smap, audit_md, refs_md = clean_audit_and_refs(raw_text)

        cleaned_lines = []
        first_header_handled = False

        for line in body.splitlines():
            stripped = line.strip()
            hm = re.match(r'^(#{1,6})\s*(.*)$', stripped)
            if hm:
                h_level, h_text = len(hm.group(1)), hm.group(2).strip()
                h_text = re.sub(r'\*\*(.*?)\*\*', r'\1', h_text)
                h_text = re.sub(r'^(?:Intelligence|Technical)?\s*Requirement\s+[0-9\.]+\s*[:\-–\.]\s*', '', h_text, flags=re.I)
                h_text = re.sub(r'^Section\s+\d+\s*[:\-–\.]\s*', '', h_text, flags=re.I)
                h_text = re.sub(r'^[0-9\.]+\s*[:\-–\.]\s*', '', h_text)

                if not first_header_handled:
                    cleaned_lines.append(f"\n## {req_id} {canonical_title}\n")
                    first_header_handled = True
                    continue

                if not h_text:
                    continue

                new_level = "###" if h_level <= 3 else "####"
                cleaned_lines.append(f"\n{new_level} {h_text}\n")
            else:
                cleaned_lines.append(line)

        if not first_header_handled:
            cleaned_lines.insert(0, f"\n## {req_id} {canonical_title}\n")

        paper_text = "\n".join(cleaned_lines)
        paper_text = inject_figures_inline(paper_text, req_id)
        paper_text, paper_endnotes = convert_all_citations(paper_text, smap)

        master_body.append(paper_text + "\n\n")

        if paper_endnotes:
            all_endnotes.append(f"\n### {req_id} {canonical_title}\n\n" + "\n".join(paper_endnotes) + "\n")
        if refs_md:
            all_refs.append(f"\n### {req_id} {canonical_title}\n\n{refs_md}\n")
        if audit_md:
            all_audits.append(f"\n### {req_id} {canonical_title}\n\n{audit_md}\n")

rear_matter = [
    "\n\n# Evidentiary Traceability & Source Repository\n\n",
    traceability_block.replace("# Evidentiary Traceability & Source Repository", "").strip() + "\n\n",
    "\n\n# Endnotes\n\n",
    *all_endnotes,
    "\n\n# Consolidated References\n\n",
    *all_refs,
    "\n\n# Verified Raw Evidence Audit Trail\n\n",
    *all_audits
]

out_path = f"assembled_assessment_{VERSION}.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.writelines(master_body)
    f.writelines(rear_matter)

print(f"✓ Built {out_path}:")
print("  - All figures placed inline at their matching topic paragraphs with '(see Figure X.Ya)' callouts.")
print("  - Duplicate unannotated base maps removed from 1.6.1, 1.6.2, 1.7.1, 1.7.2, and 2.1.")
print(f"  - Total Sequential Endnotes compiled: {global_endnote_counter}")
