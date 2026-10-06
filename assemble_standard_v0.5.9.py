#!/usr/bin/env python3
import os
import re
import glob
from pathlib import Path

VERSION = "v0.5.9"

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

# Manifest of Figures to inject per sub-section (from auto_build_visuals)
SECTION_FIGURES = {
    "1.1": [
        ("fig_1_1a_elec_consumption_trends.png", "Figure 1.1a: Regional Electricity Consumption Projections vs. Quinte West Site Loads"),
        ("fig_1_1b_bess_thermal_runaway.png", "Figure 1.1b: Four-Stage Lithium-Ion BESS Thermal Runaway and Early-Warning Mitigation Architecture"),
        ("fig_1_1c_diurnal_load_curve.png", "Figure 1.1c: 24-Hour Diurnal Electricity Demand Curve: Baseload vs. Spatio-Temporal Load-Shifting"),
        ("fig_1_1d_scope_emissions_health.png", "Figure 1.1d: Data Center Scope 1, 2, and 3 Emissions Profile and Public Health Trajectory"),
        ("fig_1_1e_site_aerial_comparison.png", "Figure 1.1e: Side-by-Side Geospatial Comparison of 7 Riverside Drive and 920 Trenton-Frankford Road")
    ],
    "1.2": [
        ("fig_1_2a_coloedr_pricing_flowchart.png", "Figure 1.2a: Multi-Tenant ColoEDR Supply-Function Bidding and Price Responsive Load (PRL) Flowchart"),
        ("fig_1_2b_cooling_energy_donut.png", "Figure 1.2b: Breakdown of Data Center Electricity Consumption and Cooling Efficiency Savings"),
        ("fig_1_2c_jurisdictional_comparison.png", "Figure 1.2c: Jurisdictional Grid Planning Comparison: Alberta, Ontario, and Quinte West")
    ],
    "1.3": [
        ("fig_1_3a_ontario_generation_donut.png", "Figure 1.3a: Ontario IESO Bulk Electricity Generation Mix Feeding the Quinte West Corridor"),
        ("fig_1_3b_substation_schematic.png", "Figure 1.3b: Substation Step-Down Network Schematic and Thermal Capacity Limits"),
        ("fig_1_3c_outage_vulnerability_map.png", "Figure 1.3c: Winter Storm Overhead Line Vulnerability and Outage Hotspot Map for Frankford and Batawa")
    ],
    "1.4": [
        ("fig_1_4a_grid_upgrade_costs.png", "Figure 1.4a: Capital Expenditure Ranges for Quinte West Grid Infrastructure Upgrades ($ Millions)"),
        ("fig_1_4b_solar_vs_grid_expansion.png", "Figure 1.4b: Economic Comparison of a 50 MW Solar Farm vs. 50 MW Traditional Grid Expansion"),
        ("fig_1_4c_health_land_footprint.png", "Figure 1.4c: Health and Environmental Externalities of Fossil/Diesel Grid Expansion vs. 100% Renewable Integration")
    ],
    "1.5": [
        ("fig_1_5a_ontario_playbook_pillars.png", "Figure 1.5a: Ontario's Data Centre Playbook Three-Pillar Architecture and Provincial Governance Override"),
        ("fig_1_5b_global_policy_matrix.png", "Figure 1.5b: International Legislative and Efficiency Matrix Comparing Global Data Center Frameworks")
    ],
    "1.6.1": [
        ("fig_1_6_1a_saputo_enhanced_map.png", "Figure 1.6.1a: Enhanced Site Map of 7 Riverside Drive (Saputo) with SM-14 Rezoning and Trenton WTP Callouts"),
        ("fig_1_6_1b_saputo_timeline.png", "Figure 1.6.1b: Site Profile and Historical Timeline of 7 Riverside Drive from Saputo Closure to Post-October 2026 Deferral")
    ],
    "1.6.2": [
        ("fig_1_6_2a_electrical_routing_map.png", "Figure 1.6.2a: Local Electrical Routing Map Showing Elexicon Energy Service Zone, Hydro One Feeders, and Trent Corridor"),
        ("fig_1_6_2b_capacity_deficit_chart.png", "Figure 1.6.2b: Substation Thermal Capacity Deficit vs. Conventional and Hyperscale AI Data Center Loads")
    ],
    "1.7.1": [
        ("fig_1_7_1a_sonoco_floodplain_cross_section.png", "Figure 1.7.1a: Lower Trent Conservation Floodplain Map (Sheet 112) and Elevation Cross-Section"),
        ("fig_1_7_1b_firstblock_heat_and_noise.png", "Figure 1.7.1b: FirstBlock 33 MW Circular Waste-Heat Recovery Schematic and Acoustic Comparison Against NPC-300 Limits")
    ],
    "1.7.2": [
        ("fig_1_7_2a_sonoco_substation_feeder_map.png", "Figure 1.7.2a: Substation and Feeder Map Plotting 44 kV Sydney TS-M1 Feeders, 5 Bernard Long Rd, and Harder Drive Substation"),
        ("fig_1_7_2b_vibroacoustic_coupling.png", "Figure 1.7.2b: Vibroacoustic Coupling Diagram Showing Low-Frequency (<100 Hz) dBC Resonance vs. Municipal dBA Bylaws")
    ],
    "2.1": [
        ("fig_2_1a_trenton_waterways_enhanced_map.png", "Figure 2.1a: Enhanced Waterway Map of Quinte West Labeling Locks 1–7, Bay of Quinte Estuary, Dams, and Water Soldier Zones"),
        ("fig_2_1b_trent_severn_photos_panel.png", "Figure 2.1b: Visual Reference Panel: Trent-Severn Lockmaster's House, Trent Port Marina, and Invasive Water Soldier"),
        ("fig_2_1c_elorca_merger_chart.png", "Figure 2.1c: Organizational Merger Chart Showing the 2027 Consolidation into ELORCA")
    ],
    "2.2": [
        ("fig_2_2a_conservation_areas_map.png", "Figure 2.2a: Lower Trent Watershed Conservation Areas: Trenton Greenbelt, Bleasdell Boulder, and Sager Conservation Area"),
        ("fig_2_2b_black_carbon_emissions.png", "Figure 2.2b: 2024 Canadian Inventory Comparison of Provincial Black Carbon and Fine Particulate Emissions")
    ],
    "2.3": [
        ("fig_2_3a_source_water_ipz_map.png", "Figure 2.3a: Source Water Protection Map Plotting Trenton and Bayside WTP Intakes and IPZ-1, IPZ-2, and IPZ-3 Buffers"),
        ("fig_2_3b_dual_wtp_schematic.png", "Figure 2.3b: Dual Water Treatment Process Schematic Comparing the Trenton and Bayside Water Treatment Plants")
    ],
    "2.4": [
        ("fig_2_4a_hydrological_block_diagram.png", "Figure 2.4a: Hydrological Block Diagram Illustrating Flow from Canadian Shield Highlands to the Bay of Quinte"),
        ("fig_2_4b_water_depletion_pie_bar.png", "Figure 2.4b: Data Center Direct vs. Indirect Water Footprint and Annual Subbasin Depletion Rates")
    ],
    "2.5": [
        ("fig_2_5a_species_at_risk_panel.png", "Figure 2.5a: Field Reference Panel of Four Quinte West Species at Risk: Massasauga, Blanding's Turtle, Sturgeon, and Salmon"),
        ("fig_2_5b_early_warning_monitoring_arch.png", "Figure 2.5b: Multi-Sensor Real-Time Environmental Early-Warning Architecture for Brownfield Data Center Sites")
    ],
    "2.6": [
        ("fig_2_6a_regulatory_approval_flowchart.png", "Figure 2.6a: Municipal and Provincial Regulatory Approval Flowchart for Data Center Proposals in Quinte West")
    ],
    "2.7": [
        ("fig_2_7a_wildlife_status_gis_map.png", "Figure 2.7a: GIS Wildlife Concentration and Conservation Status Rank (S1–S3) Map of Quinte West"),
        ("fig_2_7b_pollinator_biodiversity_bar.png", "Figure 2.7b: Comparative Pollinator and Biodiversity Trajectory: Restored Greenbelt vs. Unbuffered Perimeter")
    ],
    "2.8": [
        ("fig_2_8a_apiary_emf_buffer_map.png", "Figure 2.8a: Quinte West Apiary and Pollinator Connectivity Map with 500 m EMF and 200 m Zoning Setback Buffers"),
        ("fig_2_8b_honeybee_emf_vibration_pathway.png", "Figure 2.8b: Biological Pathway of 50/60 Hz ELF-EMF and Mechanical Vibration on Honeybee Colonies")
    ],
    "3.1": [
        ("fig_3_1a_cooling_water_pue_chart.png", "Figure 3.1a: Stacked Bar and PUE Line Chart Comparing Open-Loop, Closed-Loop, and Hybrid Cooling for a 200 MW Load"),
        ("fig_3_1b_cooling_cutaway_comparison.png", "Figure 3.1b: Engineering Comparison of an Open-Loop Evaporative Tower vs. Closed-Loop Direct-to-Chip Cooling with Rainwater Tank")
    ],
    "3.2": [
        ("fig_3_2a_hydrogeological_cross_section.png", "Figure 3.2a: Hydrogeological Cross-Section Comparing Open-Loop Aquifer Cone-of-Depression vs. Closed-Loop Glycol Leaching"),
        ("fig_3_2b_water_scale_comparison.png", "Figure 3.2b: Scale Comparison of Data Center Water Consumption Metrics From Single AI Training Runs to Regional Aquifers")
    ],
    "3.3": [
        ("fig_3_3a_surge_power_comparison.png", "Figure 3.3a: Multi-Metric Comparison of Diesel Generators, BESS, and Solar PV / ORC Systems"),
        ("fig_3_3b_site_microgrid_schematics.png", "Figure 3.3b: Proposed Hybrid Microgrid Schematics for 7 Riverside Drive and 920 Trenton-Frankford Road")
    ],
    "3.4": [
        ("fig_3_4a_canada_emissions_benchmarks.png", "Figure 3.4a: 2024 Canadian Emissions Inventory Benchmarks (NOx, PM2.5, Black Carbon) and SCR/DPF Controls"),
        ("fig_3_4b_atmospheric_deposition_diagram.png", "Figure 3.4b: Atmospheric Deposition Pathway of Diesel Exhaust Plumes on the Trent River Watershed and Wetlands")
    ],
    "3.5.1": [
        ("fig_3_5_1a_storage_and_biodegradation.png", "Figure 3.5.1a: Projected Diesel and Propylene Glycol Storage Volumes and Soil Biodegradation Curve"),
        ("fig_3_5_1b_csa_double_walled_tank.png", "Figure 3.5.1b: Engineering Cross-Section of a CSA-Compliant Double-Walled Storage Tank with Secondary Containment")
    ],
    "3.5.2": [
        ("fig_3_5_2a_diesel_toxicity_diagram.png", "Figure 3.5.2a: Terrestrial and Aquatic Toxicity Pathway of a Bulk Diesel Fuel Spill (10–100 mg/L)"),
        ("fig_3_5_2b_diesel_spill_trajectory_map.png", "Figure 3.5.2b: Simulated 5,500-Gallon Diesel Spill Trajectory Map from 7 Riverside Drive and 920 Trenton-Frankford Road")
    ],
    "3.5.3": [
        ("fig_3_5_3a_pg_spill_oxygen_depletion.png", "Figure 3.5.3a: Trent River Propylene Glycol Spill Map and 48-Hour Dissolved Oxygen Depletion Curve (<2.0 mg/L Hypoxia)"),
        ("fig_3_5_3b_pg_vs_eg_comparison.png", "Figure 3.5.3b: Toxicological and Biochemical Oxygen Demand Comparison of Propylene Glycol vs. Ethylene Glycol")
    ],
    "3.6": [
        ("fig_3_6a_ansi_species_disruption.png", "Figure 3.6a: Sensory and Habitat Disruption Matrix for Key Trent River ANSI Species")
    ],
    "3.7": [
        ("fig_3_7a_shepherd_bee_emf_chart.png", "Figure 3.7a: Bar Chart with Error Bars Illustrating Shepherd et al. (2018) Honeybee Learning Drop (-27.97%) Under 100 uT EMF"),
        ("fig_3_7b_emf_distance_decay_shielding.png", "Figure 3.7b: EMF Distance-Decay and Shielding Attenuation Diagram Comparing 132–400 kV Lines, Data Center Equipment, and Buffers")
    ],
    "3.8": [
        ("fig_3_8a_four_pathway_ecological_matrix.png", "Figure 3.8a: Four-Pathway Ecological Impact Matrix Summarizing Habitat Loss, Water/Energy Demand, Noise, and Light Pollution"),
        ("fig_3_8b_cooling_tech_dual_axis.png", "Figure 3.8b: Dual-Axis Bar Chart Contrasting Daily Water Use and Energy Use Across Four Cooling Architectures")
    ],
    "3.9": [
        ("fig_3_9a_international_regulatory_scorecard.png", "Figure 3.9a: International Regulatory Scorecard Comparing Canada's RDDP Against the EU Green Deal, US EPA, and China")
    ],
    "4.1": [
        ("fig_4_1_dba_vs_dbc.png", "Figure 4.1: Low-Frequency Attenuation Gap Between dBA and dBC Weighting Networks")
    ],
    "6.2": [
        ("fig_6_2_mpac_tax_split.png", "Figure 6.2: MPAC Capital Valuation Split: Exempt Server/Chiller Machinery (80–90%) vs. Taxable Shell (10–20%)")
    ],
    "7.1": [
        ("fig_7_1_labor_disparity_and_mw_ratios.png", "Figure 7.1: Capital-to-Labor Mismatch: Temporary Construction Trades vs. Permanent Operational Headcount")
    ]
}

def natural_key(path):
    base = os.path.basename(path)
    num_part = base.split("_")[0]
    return [int(x) if x.isdigit() else x for x in num_part.split(".")]

def make_breakable_filename(fname):
    """Inserts zero-width spaces after underscores, hyphens, and slashes so Typst wraps cleanly without overflowing."""
    return fname.replace("_", "_\u200b").replace("-", "-\u200b").replace("/", "/\u200b")

def extract_audit_trail(text):
    """
    Extracts the raw Audit Trail table and formats it as an indented, page-breakable ledger
    with soft wrapping points on all filenames and paths to prevent table collisions.
    """
    smap = {}
    if "## Verified Raw Evidence Audit Trail" not in text:
        return text, smap, ""

    parts = text.split("## Verified Raw Evidence Audit Trail", 1)
    body = parts[0]
    audit_raw = parts[1]

    audit_norm = re.sub(r'\|\s*\|\s*(\d+)\s*\|', r'|\n| \1 |', audit_raw)
    ledger_items = []

    for line in audit_norm.splitlines():
        line_s = line.strip()
        m = re.match(r'^\|\s*(\d+)\s*\|\s*`?([^`|]+?)`?\s*\|\s*`?([^`|]+?)`?\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|?$', line_s)
        if m:
            idx, fname, archive, page, excerpt = (
                m.group(1).strip(),
                m.group(2).strip(),
                m.group(3).strip(),
                m.group(4).strip(),
                m.group(5).strip()
            )
            w_fname = make_breakable_filename(fname)
            w_arch = make_breakable_filename(archive)
            smap[idx] = f"Source #{idx}: {w_fname} ({w_arch}), Page/Loc: {page}"

            clean_excerpt = re.sub(r'[#`<>\[\]|*]', ' ', excerpt)
            clean_excerpt = " ".join(clean_excerpt.split())
            ledger_items.append(
                f"{idx}. **{w_fname}**\n"
                f"   - **Archive:** `{w_arch}` | **Page / Location:** `{page}`\n"
                f"   - **Verbatim Extract:** \"{clean_excerpt}\""
            )

    return body, smap, "\n\n".join(ledger_items)

def extract_references_section(body, smap):
    pattern = re.compile(
        r'(?im)^#{1,4}\s*(?:\d+(?:\.\d+)*\.?\s*)?(?:Section\s+\d+\s*[:\-–\.]\s*)?References\s*$'
    )
    m = pattern.search(body)
    if not m:
        return body, ""

    main_body = body[:m.start()].rstrip()
    refs_raw = body[m.end():].strip()

    refs_raw = re.sub(r'(?im)^\s*\*?\*?Word\s+Count\s*:.*$', '', refs_raw)
    refs_raw = re.sub(r'(?m)^---\s*$', '', refs_raw).strip()
    refs_raw = re.sub(r'(?m)^(\s*)\^\[\s*(\d+)\s*\]\^?\s*[:\-]?\s*', r'\1- **[Source #\2]:** ', refs_raw)
    refs_raw = re.sub(r'(?m)^(\s*)\^(\d+)\s*[:\.]?\s*', r'\1- **[Source #\2]:** ', refs_raw)
    refs_raw = re.sub(r'(?m)^(\s*)\[\^(\d+)\]:\s*', r'\1- **[Source #\2]:** ', refs_raw)
    refs_raw = re.sub(r'\^\[([^\]]+)\]\^?', r'(\1)', refs_raw)
    refs_raw = re.sub(r'(?<![\w`])\^(\d{1,2})(?![\d\[\w])', r'[Source #\1]', refs_raw)
    refs_raw = re.sub(r'\^(?=[\.\,;:\s\)]|$)', '', refs_raw)

    refs_raw = re.sub(
        r'\b([a-zA-Z0-9]+_[a-zA-Z0-9_\-\.]+)\b',
        lambda match: make_breakable_filename(match.group(1)),
        refs_raw
    )
    return main_body, refs_raw

global_endnote_counter = 0

def convert_inline_citations_to_endnotes(body, smap):
    global global_endnote_counter
    paper_endnotes = []
    body = re.sub(r'(?im)^\s*\*?\*?Word\s+Count\s*:.*$', '', body)

    for m in re.finditer(r'(?m)^\s*(?:\[\^(\d+)\]:|\^\[\s*(\d+)\s*\]\^?\s*:)\s*(.+)$', body):
        idx = m.group(1) or m.group(2)
        desc = m.group(3).strip()
        if idx and idx not in smap:
            smap[idx] = f"Source #{idx}: {desc}"

    body = re.sub(r'(?m)^(\s*)\^\[\s*(\d+)\s*\]\^?\s*[:\-]\s*', r'\1- **[Source #\2]:** ', body)
    body = re.sub(r'(?m)^(\s*)\[\^(\d+)\]:\s*', r'\1- **[Source #\2]:** ', body)

    def add_endnote(text_desc):
        global global_endnote_counter
        global_endnote_counter += 1
        en_id = global_endnote_counter
        paper_endnotes.append(f"{en_id}. {text_desc}")
        return f"^\\[{en_id}\\]^"

    def resolve_nums_to_endnote(nums):
        resolved = [smap.get(n, f"Source #{n} (See Verified Raw Evidence Audit Trail)") for n in nums]
        return add_endnote("; ".join(resolved))

    def expand_num_tokens(s):
        nums = []
        for part in re.split(r'[,;&]+', s):
            rm = re.search(r'(\d+)\s*[\-–]\s*(\d+)', part)
            if rm:
                start, end = int(rm.group(1)), int(rm.group(2))
                if 1 <= start <= end <= 30:
                    nums.extend([str(i) for i in range(start, end + 1)])
                    continue
            for n in re.findall(r'\d+', part):
                if 1 <= int(n) <= 30:
                    nums.append(n)
        return nums

    def repl_full_inline(match):
        inner = match.group(1).strip()
        trailing = match.group(2) or ""
        nums = re.findall(r'#(\d+)', inner) + re.findall(r'\d+', trailing)
        if nums:
            seen = []
            for n in nums:
                if n not in seen and 1 <= int(n) <= 30:
                    seen.append(n)
            if seen and all(n in smap for n in seen):
                return resolve_nums_to_endnote(seen)
        return add_endnote(inner)

    body = re.sub(r'\^\[([^\]]*[Ss]ource[^\]]*)\](\[\d+\])?', repl_full_inline, body)

    def repl_bracketed(match):
        inner = match.group(1).strip()
        cleaned = re.sub(r'(?i)\bsources?\b|\bfile\b|[\[\]#:]', '', inner).strip()
        nums = expand_num_tokens(cleaned)
        if nums and re.fullmatch(r'[\d\s,;&\-–]+', cleaned):
            return resolve_nums_to_endnote(nums)
        return add_endnote(inner)

    body = re.sub(r'\^\[([^\]]+)\]\^?', repl_bracketed, body)
    body = re.sub(r'\[\^([^\]]+)\](?!:)', repl_bracketed, body)

    def repl_source_phrase(match):
        inner = match.group(1)
        nums = expand_num_tokens(inner)
        if nums:
            return resolve_nums_to_endnote(nums)
        return match.group(0)

    body = re.sub(
        r'\(\s*[Ss]ources?\s+((?:\[\d+\]|#\d+|\d+)(?:\s*[,;&\-–]\s*(?:\[\d+\]|#\d+|\d+))*)\s*\)',
        repl_source_phrase,
        body
    )
    body = re.sub(
        r'(?<![\w])(?:[Ss]ources?)\s+((?:\[\d+\]|#\d+)(?:\s*[,;&\-–]\s*(?:\[\d+\]|#\d+))*)',
        repl_source_phrase,
        body
    )

    def repl_bracket_chain(match):
        chain = match.group(0)
        nums = [n for n in re.findall(r'\d+', chain) if 1 <= int(n) <= 30]
        if nums:
            return resolve_nums_to_endnote(nums)
        return chain

    body = re.sub(r'(?:\[\d{1,2}\]\s*){2,}', repl_bracket_chain, body)

    def repl_bare_caret(match):
        num = match.group(1)
        if 1 <= int(num) <= 30:
            return resolve_nums_to_endnote([num])
        return match.group(0)

    body = re.sub(r'(?<![\w`])\^(\d{1,2})(?![\d\[\w\^])', repl_bare_caret, body)
    body = re.sub(r'\^(?=[\.\,;:\s\)]|$)', '', body)
    return body, paper_endnotes

master_body_lines = []
all_endnotes_sections = []
all_references_sections = []
all_audit_sections = []

# Load QR verification block to place right before Endnotes
verification_path = os.path.join("papers", "00_source_verification.md")
traceability_block = ""
if os.path.exists(verification_path):
    with open(verification_path, "r", encoding="utf-8") as vf:
        traceability_block = vf.read().strip() + "\n\n"

for folder, sec_title in SECTIONS:
    sec_path = os.path.join("papers", folder)
    if not os.path.exists(sec_path):
        continue
    files = sorted(glob.glob(os.path.join(sec_path, "*.md")), key=natural_key)
    if not files:
        continue

    master_body_lines.append(f"\n# {sec_title}\n")

    for fpath in files:
        fname = os.path.basename(fpath)
        raw_req_id = fname.split("_")[0]

        # Re-number 99.x to 10.x
        if raw_req_id.startswith("99."):
            req_id = "10." + raw_req_id[3:]
        elif raw_req_id == "99":
            req_id = "10"
        else:
            req_id = raw_req_id

        with open(fpath, "r", encoding="utf-8") as f:
            raw_text = f.read()

        body_no_audit, smap, audit_ledger_md = extract_audit_trail(raw_text)
        body_clean, refs_md = extract_references_section(body_no_audit, smap)

        lines = body_clean.splitlines(keepends=True)
        norm_lines = []
        title_found = False
        paper_title = fname.replace(".md", "").replace("_", " ")

        for line in lines:
            m = re.match(r'^(#{1,6})\s+(.*)$', line.strip())
            if m:
                hashes, htext = m.group(1), m.group(2).strip()
                htext = re.sub(r'\*\*(.*?)\*\*', r'\1', htext)

                if not title_found:
                    htext = re.sub(r'^(?:Intelligence|Technical)?\s*Requirement\s+[0-9\.]+\s*[:\-–]\s*', '', htext, flags=re.I)
                    htext = re.sub(r'^[0-9\.]+\s*[:\-–]?\s*', '', htext)
                    paper_title = htext
                    norm_lines.append(f"\n## {req_id} {paper_title}\n")
                    title_found = True
                else:
                    htext = re.sub(r'^Section\s+\d+\s*[:\-–\.]\s*', '', htext, flags=re.I)
                    htext = re.sub(r'^\d+(?:\.\d+)*\.?\s+', '', htext)
                    if len(hashes) <= 2:
                        norm_lines.append(f"\n### {htext}\n")
                    else:
                        norm_lines.append(f"\n#### {htext}\n")
            else:
                norm_lines.append(line)

        if not title_found:
            norm_lines.insert(0, f"\n## {req_id} {paper_title}\n")

        paper_body_str = "".join(norm_lines)

        # Inject matching figures if present in figures/
        figs = SECTION_FIGURES.get(req_id, [])
        for fig_file, caption in figs:
            if os.path.exists(os.path.join("figures", fig_file)) and fig_file not in paper_body_str:
                paper_body_str += f"\n\n![{caption}](figures/{fig_file}){{width=88%}}\n\n"

        paper_body_endnoted, paper_endnotes = convert_inline_citations_to_endnotes(paper_body_str, smap)

        master_body_lines.append(paper_body_endnoted)
        master_body_lines.append("\n\n")

        if paper_endnotes:
            all_endnotes_sections.append(
                f"\n### {req_id} {paper_title}\n\n" + "\n".join(paper_endnotes) + "\n"
            )
        if refs_md:
            all_references_sections.append(
                f"\n### {req_id} {paper_title}\n\n{refs_md}\n"
            )
        if audit_ledger_md:
            all_audit_sections.append(
                f"\n### {req_id} {paper_title}\n\n{audit_ledger_md}\n"
            )

# BACK-MATTER STANDARD:
# 1. Evidentiary Traceability & Source Repository (Directly before Endnotes)
# 2. # Endnotes
# 3. # Consolidated References
# 4. # Verified Raw Evidence Audit Trail (Moved to after Endnotes and References as breakable ledgers)
rear_matter = [
    "\n\n# Evidentiary Traceability & Source Repository\n\n",
    traceability_block.replace("# Evidentiary Traceability & Source Repository", "").strip() + "\n\n",
    "\n\n# Endnotes\n\n",
    *all_endnotes_sections,
    "\n\n# Consolidated References\n\n",
    *all_references_sections,
    "\n\n# Verified Raw Evidence Audit Trail\n\n",
    *all_audit_sections,
]

assembled_path = f"assembled_assessment_{VERSION}.md"
with open(assembled_path, "w", encoding="utf-8") as out:
    out.writelines(master_body_lines)
    out.writelines(rear_matter)

print(f"✓ Built {assembled_path}:")
print("  - 'Evidentiary Traceability & Source Repository' locked directly ahead of # Endnotes.")
print("  - 'Verified Raw Evidence Audit Trail' formatted as breakable ledgers and moved after Endnotes.")
print(f"  - Total Endnotes compiled: {global_endnote_counter}")
