#!/usr/bin/env python3
import os
import re
import glob
from pathlib import Path

VERSION = "v0.5.9"

# Master Canonical Titles for every sub-section (prevents blank or missing TOC entries)
CANONICAL_TITLES = {
    # Section 1
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
    # Section 2
    "2.1": "Major Rivers and Bodies of Water in Quinte West",
    "2.2": "Conservation Areas of Quinte West",
    "2.3": "Where Quinte West Gets Its Drinking Water From",
    "2.4": "What Is the Quinte West Watershed",
    "2.5": "Major Environmental, Ecological, and Conservation Concerns",
    "2.6": "How Quinte West Legislates Data Center Environmental Concerns",
    "2.7": "Concentrations of Wildlife in Quinte West and Spatial Mapping",
    "2.8": "Apiaries and Pollinator Zones in Quinte West",
    # Section 3
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
    # Section 4
    "4.1": "dBA vs. dBC: Technical Differences and Application to Data Centers",
    "4.2": "Data Center Components Producing dBC and Engineering Mitigations",
    "4.3": "Medical Implications of Short- and Long-Term dBC Exposure",
    "4.4": "Effects of Data Center Noise on Residential Property Values",
    "4.5": "Acoustic and Vibrational Impacts on Wildlife and Bees",
    "4.6": "How Governments Legislate Data Center Noise",
    # Section 5
    "5.1": "Physical Human Health Impacts from Data Centers",
    "5.2": "Mental Health and Vibroacoustic Stress Impacts",
    "5.3": "How Governments Legislate Data Center Health Concerns",
    # Section 6
    "6.1": "Quinte West Approach to Municipal Taxation of Data Centers",
    "6.2": "Canadian and International Data Center Taxation Frameworks",
    "6.3": "Property Tax Assessment: Real Property Shell vs. Exempt Machinery Contents",
    # Section 7
    "7.1": "Data Center Employment Headcount and Staffing Ratios",
    "7.2": "Trades and Job Classifications in Operational Facilities",
    "7.3": "Trades Required to Build and Commission a Facility",
    "7.4": "Long-Term Operational Staffing Requirements",
    "7.5": "Local Business and Professional Services Required",
    "7.6": "Materials and Consumables Required for Operations",
    # Section 8
    "8.1": "Spill Emergency Agencies Beyond Police, Fire, and Ambulance",
    "8.2": "Contamination Types and Environmental Pathways",
    "8.3": "Historical Data Center Contamination in Canada",
    "8.4": "Historical Data Center Contamination Worldwide",
    "8.5": "Canadian Government Responses to Data Center Incidents",
    "8.6": "International Government Responses to Data Center Incidents",
    # Section 9
    "9.1": "Hazardous Spills and Contamination Incidents in Ontario",
    "9.2": "Hazardous Spills and Contamination Incidents in Canada (Excl. Ontario)",
    "9.3": "Hazardous Spills and Contamination Incidents in the United States",
    "9.4": "Hazardous Spills and Contamination Incidents in Europe",
    "9.5": "Hazardous Spills and Contamination Incidents in Asia",
    "9.6": "Hazardous Spills and Contamination Incidents in Australia",
    "9.7": "Hazardous Spills and Contamination Incidents in China",
    "9.8": "Hazardous Spills and Contamination Incidents in Russia",
    # Section 10
    "10.1": "Medical Facilities in Quinte West",
    "10.2": "Educational Facilities in Quinte West",
    "10.3": "Retirement and Long-Term Care Homes in Quinte West",
    "10.4": "Fire and Emergency Stations in Quinte West",
    "10.5": "Police Detachments in Quinte West",
    "10.6": "Government and Administrative Offices in Quinte West"
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
    
    # 1. Audit trail extraction
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

    # 2. References extraction
    ref_pat = re.compile(r'(?im)^#{1,4}\s*(?:\d+(?:\.\d+)*\.?\s*)?(?:Section\s+\d+\s*[:\-–\.]\s*)?References\s*$')
    m_ref = ref_pat.search(text)
    if m_ref:
        refs_raw = text[m_ref.end():].strip()
        text = text[:m_ref.start()].rstrip()
        refs_raw = re.sub(r'(?im)^\s*\*?\*?Word\s+Count\s*:.*$', '', refs_raw)
        refs_raw = re.sub(r'(?m)^---\s*$', '', refs_raw).strip()
        refs_raw = re.sub(r'(?m)^(\s*)\^?\[\s*(\d+)\s*\]\^?\s*[:\-]?\s*', r'\1- **[Source #\2]:** ', refs_raw)
        refs_md = make_breakable(refs_raw)

    return text, smap, audit_md, refs_md

global_endnote_counter = 0

def convert_citations(body, smap):
    global global_endnote_counter
    endnotes = []
    body = re.sub(r'(?im)^\s*\*?\*?Word\s+Count\s*:.*$', '', body)

    def add_en(desc):
        global global_endnote_counter
        global_endnote_counter += 1
        endnotes.append(f"{global_endnote_counter}. {desc}")
        return f"^\\[{global_endnote_counter}\\]^"

    def repl_src(m):
        inner = m.group(1).strip()
        nums = [n for n in re.findall(r'\d+', inner) if 1 <= int(n) <= 30]
        if nums and all(n in smap for n in nums):
            return add_en("; ".join([smap[n] for n in nums]))
        return add_en(inner)

    body = re.sub(r'\^\[([^\]]+)\]', repl_src, body)
    body = re.sub(r'\[\^([^\]]+)\]', repl_src, body)
    return body, endnotes

master_body = []
all_endnotes = []
all_refs = []
all_audits = []

# Front-matter verification block
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

        # Get authoritative title
        canonical_title = CANONICAL_TITLES.get(req_id, fname.replace(".md", "").replace("_", " "))

        raw_text = fpath.read_text(encoding="utf-8", errors="ignore")
        body, smap, audit_md, refs_md = clean_audit_and_refs(raw_text)

        # Normalize headings and delete any empty headers
        cleaned_lines = []
        first_header_handled = False

        for line in body.splitlines():
            stripped = line.strip()
            # Catch markdown headings
            hm = re.match(r'^(#{1,6})\s*(.*)$', stripped)
            if hm:
                h_level, h_text = len(hm.group(1)), hm.group(2).strip()
                # Clean out bolding and numbers
                h_text = re.sub(r'\*\*(.*?)\*\*', r'\1', h_text)
                h_text = re.sub(r'^(?:Intelligence|Technical)?\s*Requirement\s+[0-9\.]+\s*[:\-–\.]\s*', '', h_text, flags=re.I)
                h_text = re.sub(r'^Section\s+\d+\s*[:\-–\.]\s*', '', h_text, flags=re.I)
                h_text = re.sub(r'^[0-9\.]+\s*[:\-–\.]\s*', '', h_text)

                if not first_header_handled:
                    # Enforce standardized sub-section heading for the TOC
                    cleaned_lines.append(f"\n## {req_id} {canonical_title}\n")
                    first_header_handled = True
                    continue

                # Discard empty headings (the cause of bare page numbers in TOC)
                if not h_text or h_text.lower() in ("introduction", "overview", "executive summary"):
                    if not h_text:
                        continue  # completely empty heading -> DROP IT

                # Demote sub-headings inside the paper
                new_level = "###" if h_level <= 3 else "####"
                cleaned_lines.append(f"\n{new_level} {h_text}\n")
            else:
                cleaned_lines.append(line)

        if not first_header_handled:
            cleaned_lines.insert(0, f"\n## {req_id} {canonical_title}\n")

        paper_text = "\n".join(cleaned_lines)
        paper_text, paper_endnotes = convert_citations(paper_text, smap)

        master_body.append(paper_text + "\n\n")

        if paper_endnotes:
            all_endnotes.append(f"\n### {req_id} {canonical_title}\n\n" + "\n".join(paper_endnotes) + "\n")
        if refs_md:
            all_refs.append(f"\n### {req_id} {canonical_title}\n\n{refs_md}\n")
        if audit_md:
            all_audits.append(f"\n### {req_id} {canonical_title}\n\n{audit_md}\n")

# Assembly in strict back-matter order
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

print(f"✓ Successfully built {out_path} with 100% clean TOC hierarchy.")
