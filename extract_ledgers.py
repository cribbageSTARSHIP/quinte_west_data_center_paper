import os
import fitz  # pymupdf

pdf_dir = "/workspace/pdfs"
out_dir = "/workspace/output/ledgers"
os.makedirs(out_dir, exist_ok=True)

topics = {
    "01_power_grid.md": ["power", "grid", "electricity", "substation", "utility", "generator", "outage", "kw", "mw", "voltage", "ieso"],
    "02_water_wastewater.md": ["water", "wastewater", "sewer", "treatment", "aquifer", "pipeline", "gallons", "mgd", "cooling", "evaporative"],
    "03_transportation_logistics.md": ["road", "bridge", "highway", "transit", "rail", "traffic", "corridor", "freight"],
    "04_telecommunications_cyber.md": ["telecom", "fiber", "broadband", "network", "cyber", "communication", "cellular"],
    "05_public_health_medical.md": ["hospital", "health", "medical", "clinic", "ems", "sleep", "noise", "air quality", "emissions", "pm2.5", "asthma"],
    "06_food_agriculture.md": ["food", "agriculture", "crop", "farm", "apiary", "bee", "pollinator", "livestock", "soil"],
    "07_economic_demographics.md": ["population", "economy", "gdp", "employment", "tax", "jobs", "revenue", "incentive", "abatement", "mpac"],
    "08_hazards_emergency.md": ["hazard", "emergency", "fire", "spill", "glycol", "bess", "battery", "thermal runaway", "toxic", "plume"]
}

# Initialize ledgers
for fname in topics.keys():
    with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
        f.write(f"# Research Ledger: {fname}\n\n")

# Recursively locate all PDFs
pdf_paths = []
for root, _, files in os.walk(pdf_dir):
    for f in files:
        if f.lower().endswith(".pdf"):
            pdf_paths.append(os.path.join(root, f))

pdf_paths.sort()
print(f"Discovered {len(pdf_paths)} PDFs across {pdf_dir}. Starting extraction...")

for idx, pdf_path in enumerate(pdf_paths, 1):
    pdf_name = os.path.basename(pdf_path)
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            text = doc[page_num].get_text()
            if not text.strip():
                continue
            text_lower = text.lower()
            for fname, keywords in topics.items():
                matched = [kw for kw in keywords if kw in text_lower]
                if matched:
                    snippet = "\n".join([line.strip() for line in text.split("\n") if len(line.strip()) > 35][:8])
                    if snippet:
                        fpath = os.path.join(out_dir, fname)
                        with open(fpath, "a", encoding="utf-8") as f:
                            f.write(f"## [Source: {pdf_name}, Page {page_num + 1}]\n*Keywords: {', '.join(matched[:5])}*\n\n{snippet}\n\n---\n\n")
        doc.close()
    except Exception as e:
        print(f"Error reading {pdf_name}: {e}")

print("Extraction complete! All 8 ledgers populated.")
