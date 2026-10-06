import os
import re
import json
import time
import subprocess
from datetime import datetime

BASE_DIR = "/workspace"
PAPERS_DIR = os.path.join(BASE_DIR, "papers")
INDEX_FILE = os.path.join(BASE_DIR, "raw_search_index/raw_corpus_index.json")
LOG_FILE = os.path.join(BASE_DIR, "line_item_engine.log")

os.makedirs(PAPERS_DIR, exist_ok=True)

def log(msg):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as lf:
        lf.write(line + "\n")

log("Loading master raw corpus index...")
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    corpus = json.load(f)
log(f"Successfully loaded {len(corpus)} searchable pages/chunks across all archives.")

REQUIREMENTS = [
    # 1. Local Power Grid Impacts
    {"id": "1.1", "section": "01_power_grid", "slug": "how_data_centers_affect_local_power_grids", "title": "How Data Centers Affect Local Power Grids", "terms": ["power grid", "baseload", "megawatt", "load factor", "substation", "capacity factor", "harmonic distortion", "transformer"]},
    {"id": "1.2", "section": "01_power_grid", "slug": "how_governments_plan_power_needs", "title": "How Governments and System Operators Plan Power Needs Around Data Centers", "terms": ["system operator", "IESO", "AESO", "PJM", "resource adequacy", "transmission planning", "curtailment", "demand response", "interconnection queue"]},
    {"id": "1.3", "section": "01_power_grid", "slug": "where_quinte_west_gets_its_power", "title": "Where Quinte West Gets Its Power Sourcing and Local Infrastructure", "terms": ["Quinte West", "Hydro One", "Elexicon", "Sidney Transformer", "Trent River", "Frankford GS", "Glen Miller", "230 kV", "44 kV"]},
    {"id": "1.4", "section": "01_power_grid", "slug": "quinte_west_power_import_costs_and_sources", "title": "Quinte West Power Import Needs, Source Corridors, and Capital Upgrade Costs", "terms": ["transmission upgrade", "cost per kilometer", "substation cost", "ratepayer", "OEB", "Class A", "Class B", "cost-shifting", "Virginia electricity bill"]},
    {"id": "1.5", "section": "01_power_grid", "slug": "legislation_data_center_power_needs", "title": "How Governments in Canada and Globally Legislate Data Center Power Needs", "terms": ["ISED", "Data Centre Playbook", "Hydro-Quebec", "curtailment", "AESO moratorium", "Energy Efficiency Directive", "Ireland CRU", "Singapore"]},
    {"id": "1.6.1", "section": "01_power_grid", "slug": "7_riverside_dr_historical_details", "title": "Historical Details and Site Evolution of 7 Riverside Drive (Former Saputo Dairy)", "terms": ["7 Riverside", "Saputo", "Trenton", "dairy", "water intake", "ammonia", "planning", "rezoning", "D09/T09/26"]},
    {"id": "1.6.2", "section": "01_power_grid", "slug": "7_riverside_dr_potential_power_draw", "title": "Potential Power Draw and Electrical Grid Headroom Impact of 7 Riverside Drive", "terms": ["7 Riverside", "8 MW", "power draw", "continuous", "Sidney TS", "feeder", "households", "Class A", "thermal loading"]},
    {"id": "1.7.1", "section": "01_power_grid", "slug": "920_trenton_frankford_rd_historical_details", "title": "Historical Details and Site Evolution of 920 Trenton Frankford Road (Former Sonoco Paper Mill)", "terms": ["920 Trenton Frankford", "Sonoco", "paper mill", "Glen Miller", "All Season Fencing", "FirstBlock", "Trinity Smart Farms", "greenhouse"]},
    {"id": "1.7.2", "section": "01_power_grid", "slug": "920_trenton_frankford_rd_potential_power_draw", "title": "Potential Power Draw and Thermal Energy Dynamics at 920 Trenton Frankford Road", "terms": ["920 Trenton Frankford", "18 MW", "power draw", "substation", "thermal heat", "vertical farm", "Heat Connect", "household equivalent"]},

    # 2. Quinte West Nature and Ecology
    {"id": "2.1", "section": "02_nature_ecology", "slug": "major_rivers_and_waterbodies", "title": "Major Rivers and Bodies of Water in Quinte West", "terms": ["Trent River", "Bay of Quinte", "Murray Canal", "Cold Creek", "Oak Lake", "Trent-Severn", "hydrology", "flow rate"]},
    {"id": "2.2", "section": "02_nature_ecology", "slug": "conservation_areas_of_quinte_west", "title": "Conservation Areas and Protected Ecological Reserves in Quinte West", "terms": ["Lower Trent Conservation", "Murray Marsh", "Sager", "Bleasdell Boulder", "Goodrich-Loomis", "wetland complex", "habitat area"]},
    {"id": "2.3", "section": "02_nature_ecology", "slug": "where_quinte_west_gets_drinking_water", "title": "Where Quinte West Gets Its Drinking Water (Intake Locations and Infrastructure)", "terms": ["drinking water", "Trenton Water Treatment Plant", "Bayside", "Frankford", "surface intake", "IPZ-1", "IPZ-2", "Clean Water Act"]},
    {"id": "2.4", "section": "02_nature_ecology", "slug": "the_quinte_west_watershed", "title": "The Quinte West Watershed Architecture and Hydrological Vulnerabilities", "terms": ["watershed", "Lower Trent", "subwatershed", "drainage basin", "runoff", "water table", "alluvial", "groundwater recharge"]},
    {"id": "2.5", "section": "02_nature_ecology", "slug": "major_environmental_and_conservation_concerns", "title": "Major Environmental, Ecological, and Conservation Concerns in Quinte West", "terms": ["Area of Concern", "Bay of Quinte", "phosphorus", "algal blooms", "hypoxia", "eutrophication", "thermal pollution", "remedial action plan"]},
    {"id": "2.6", "section": "02_nature_ecology", "slug": "how_quinte_west_legislates_environmental_concerns", "title": "How Quinte West Legislates Data Center Environmental Concerns", "terms": ["Official Plan", "Site Plan Control", "zoning bylaw", "Lower Trent Conservation", "O. Reg. 41/24", "Planning Act", "environmental impact study"]},
    {"id": "2.7", "section": "02_nature_ecology", "slug": "wildlife_concentrations_and_corridors", "title": "Concentrations of Wildlife, Species at Risk, and Habitat Corridors in Quinte West", "terms": ["wildlife", "Blanding's turtle", "waterfowl", "migratory", "species at risk", "Murray Marsh", "riparian corridor", "spawning", "walleye"]},
    {"id": "2.8", "section": "02_nature_ecology", "slug": "apiaries_and_pollinator_zones", "title": "Apiaries, Commercial Beekeeping, and Pollinator Corridors in Quinte West", "terms": ["apiary", "beekeeping", "honeybee", "Apis mellifera", "pollinator", "apple orchard", "Murray ward", "Sidney", "Wooler", "foraging"]},

    # 3. Environmental, Ecological & Water Table Impacts
    {"id": "3.1", "section": "03_environmental_water_table", "slug": "water_cooling_vs_closed_loop_compared", "title": "Comparative Analysis: Evaporative Water Cooling vs. Closed-Loop Cooling Systems", "terms": ["evaporative cooling", "closed-loop", "cooling tower", "chiller", "water consumption", "PUE", "WUE", "blowdown", "dry cooler"]},
    {"id": "3.2", "section": "03_environmental_water_table", "slug": "how_data_centers_affect_the_water_table", "title": "How Data Centers Affect the Water Table (Both Open and Closed-Loop Systems)", "terms": ["water table", "aquifer", "groundwater drawdown", "impermeable surface", "stormwater runoff", "dewatering", "thermal plume", "recharge"]},
    {"id": "3.3", "section": "03_environmental_water_table", "slug": "surge_and_backup_power_needs", "title": "How Data Centers Employ Surge and Backup Power Needs", "terms": ["surge power", "backup generator", "diesel", "BESS", "battery storage", "lithium-ion", "UPS", "microgrid", "renewable baseload"]},
    {"id": "3.4", "section": "03_environmental_water_table", "slug": "hydrocarbon_generators_environmental_impact", "title": "How Hydrocarbon-Based Generators from Data Centers Affect the Local Environment", "terms": ["diesel generator", "emissions", "NOx", "PM2.5", "black carbon", "volatile organic compounds", "ozone", "air dispersion", "load bank testing"]},
    {"id": "3.5.1", "section": "03_environmental_water_table", "slug": "quinte_west_diesel_and_glycol_storage_volumes", "title": "Projected Storage Volumes of Diesel Fuel and Propylene Glycol for Quinte West Data Centers", "terms": ["diesel storage", "fuel tank", "propylene glycol volume", "chilled water loop", "7 Riverside", "8 MW", "gallons", "litres", "belly tank"]},
    {"id": "3.5.2", "section": "03_environmental_water_table", "slug": "diesel_spill_mechanics_land_and_rivers", "title": "Environmental Mechanics of a Diesel Fuel Spill on Land and Nearby Rivers", "terms": ["diesel spill", "fuel leak", "hydrocarbon", "soil contamination", "BTEX", "groundwater plume", "Trent River", "sheen", "benthic toxicity"]},
    {"id": "3.5.3", "section": "03_environmental_water_table", "slug": "propylene_glycol_spill_mechanics_and_bod", "title": "Environmental Mechanics of a Propylene Glycol Spill, BOD Loading, and Aquatic Hypoxia", "terms": ["propylene glycol spill", "biochemical oxygen demand", "BOD", "aquatic hypoxia", "dissolved oxygen", "fish kill", "Trent River", "bacterial decomposition"]},
    {"id": "3.6", "section": "03_environmental_water_table", "slug": "risks_to_local_wildlife_from_data_centers", "title": "Risks to Local Terrestrial and Aquatic Wildlife from Data Centers", "terms": ["wildlife risk", "terrestrial", "aquatic", "wetland disruption", "thermal runoff", "noise masking", "fragmentation", "stormwater discharge"]},
    {"id": "3.7", "section": "03_environmental_water_table", "slug": "risks_to_bees_and_pollinators", "title": "Specific Risks to Honeybees and Native Pollinators from Data Center Infrastructure", "terms": ["honeybees", "pollinators", "vibration", "100-500 Hz", "Johnston's organ", "electromagnetic field", "EMF", "waggle dance", "colony stress"]},
    {"id": "3.8", "section": "03_environmental_water_table", "slug": "cumulative_wildlife_impacts_habitat_noise_light", "title": "Cumulative Wildlife Impacts: Habitat Loss, High Utility Demands, Noise, and Light Pollution", "terms": ["habitat loss", "cumulative impact", "light pollution", "ALAN", "skyglow", "continuous noise", "utility demand", "ecological integrity"]},
    {"id": "3.9", "section": "03_environmental_water_table", "slug": "legislation_data_center_environmental_concerns", "title": "How Governments in Canada and Globally Legislate Data Center Environmental Concerns", "terms": ["environmental legislation", "ECA", "Environmental Compliance Approval", "Fisheries Act", "NEPA", "EU Corporate Sustainability", "Clean Water Act"]}
]

def search_corpus(query_terms, top_k=10):
    scored = []
    for item in corpus:
        text_lower = item["text"].lower()
        score = sum(text_lower.count(t.lower()) for t in query_terms if t.lower() in text_lower)
        if score > 0:
            scored.append((score, item))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [x[1] for x in scored[:top_k]]

log(f"=== Starting Execution for {len(REQUIREMENTS)} Line-Item Papers ===")

for idx, req in enumerate(REQUIREMENTS, 1):
    sec_dir = os.path.join(PAPERS_DIR, req["section"])
    os.makedirs(sec_dir, exist_ok=True)
    out_file = os.path.join(sec_dir, f"{req['id']}_{req['slug']}.md")

    log(f"--- [{idx}/{len(REQUIREMENTS)}] Processing Item {req['id']}: {req['title']} ---")

    excerpts = search_corpus(req["terms"], top_k=10)
    log(f"  Scanned corpus: Found {len(excerpts)} top relevant source excerpts.")

    evidence_text = "### Authoritative Raw Source Evidence:\n"
    for e in excerpts:
        evidence_text += f"- **Source File:** `{e['filename']}` | **Location/Page:** {e['page']} | **Archive:** {e['category']}\n"
        evidence_text += f"  > \"{e['text'][:400]}...\"\n\n"

    prompt = (
        f"Write a standalone, rigorous, publication-grade academic research paper answering: Requirement {req['id']} - '{req['title']}'.\n\n"
        f"RAW SOURCE EXCERPTS:\n{evidence_text}\n\n"
        f"REQUIREMENTS:\n"
        f"1. Write an exhaustive, multi-section analysis with Markdown headings (##, ###), bullet points, and data tables.\n"
        f"2. Every factual assertion, quantitative metric, and policy framework MUST cite the exact backing raw source above using inline format ^.\n"
        f"3. Apply direct analysis to Quinte West, Hastings County, and the Trent River watershed where relevant.\n"
        f"Save the document using write_file directly to /workspace/papers/{req['section']}/{req['id']}_{req['slug']}.md."
    )

    cmd = [
        "hermes", "-m", "qwen3-64k:14b", "-s", "grounded-citations", "--yolo", "-z", prompt
    ]

    t0 = time.time()
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    elapsed = int(time.time() - t0)

    if os.path.exists(out_file) and os.path.getsize(out_file) > 400:
        log(f"  ✓ Successfully created {out_file} ({os.path.getsize(out_file)} bytes) in {elapsed}s")
    else:
        log("  [!] write_file check: extracting stdout markdown fallback...")
        text = res.stdout.strip()
        if "```markdown" in text:
            text = text.split("```markdown")[1].split("```")[0].strip()
        elif "```" in text and "# " in text:
            text = text.split("```")[1].split("```")[0].strip()
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        log(f"  ✓ Saved fallback {out_file} ({os.path.getsize(out_file)} bytes) in {elapsed}s")

    time.sleep(2)

log("=== Completed Processing All Defined Line-Item Papers! ===")
