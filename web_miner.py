import os
import time
from ddgs import DDGS
import trafilatura

output_dir = "/workspace/output/web_ledgers"
os.makedirs(output_dir, exist_ok=True)

# Concise regional queries that return high result counts
regions = {
    "Quinte West & Bay of Quinte, Ontario": [
        '("Quinte West" OR "Belleville" OR "Trenton" OR "Bay of Quinte") Ontario ("data centre" OR "data center" OR "industrial" OR "IESO")',
        '("Quinte West" OR "Belleville") Ontario employment lands industrial electricity water capacity'
    ],
    "Ontario, Canada": [
        'Ontario ("data centre" OR "data center") IESO electricity grid',
        'Ontario ("Southwold" OR "Niagara" OR "Barrie" OR "Brampton") data centre'
    ],
    "Canada (National)": [
        'Canada ("data centre" OR "data center") Alberta Quebec BC',
    ],
    "United States": [
        'USA "data center" (Virginia OR Texas OR Oregon OR Arizona)',
    ],
    "Global (Europe, Asia, LatAm, Africa)": [
        '("Ireland" OR "Dublin" OR "Frankfurt" OR "Singapore" OR "Chile") "data center"',
    ]
}

# Your 8 Specific Data Center Focus Areas
topics = {
    "01_power_grid.md": {
        "title": "01 - Power Grid",
        "q_suffix": '(megawatt OR electricity OR grid OR utility OR substation)',
        "keywords": ["mw", "gw", "megawatt", "grid", "utility", "substation", "electricity", "ratepayer", "ieso", "power", "gas", "energy"]
    },
    "02_water_ecology.md": {
        "title": "02 - Water & Ecology",
        "q_suffix": '(water OR cooling OR drought OR aquifer OR wastewater)',
        "keywords": ["water", "cooling", "gallons", "mgd", "litres", "aquifer", "drought", "evaporative", "thermal", "watershed", "ecology"]
    },
    "03_pollutants_spills.md": {
        "title": "03 - Pollutants & Spills",
        "q_suffix": '(diesel OR generator OR emissions OR pollution OR fuel)',
        "keywords": ["diesel", "generator", "emissions", "nox", "pm2.5", "spill", "glycol", "pfas", "fuel", "pollution", "exhaust", "carbon"]
    },
    "04_acoustics_dba_dbc.md": {
        "title": "04 - Acoustics (dBA vs dBC)",
        "q_suffix": '(noise OR decibel OR dBA OR dBC OR hum OR cooling)',
        "keywords": ["noise", "dba", "dbc", "decibel", "low-frequency", "hum", "chiller", "acoustic", "hz", "fan", "ordinance", "sound"]
    },
    "05_human_health.md": {
        "title": "05 - Human Health",
        "q_suffix": '(health OR air quality OR noise OR respiratory OR sleep)',
        "keywords": ["health", "sleep", "cardiovascular", "respiratory", "asthma", "hospital", "stress", "mortality", "disease", "pollution"]
    },
    "06_municipal_tax_revenue.md": {
        "title": "06 - Municipal Tax & Revenue",
        "q_suffix": '(tax OR subsidy OR abatement OR municipal OR revenue)',
        "keywords": ["tax", "abatement", "exemption", "subsidy", "pilot", "revenue", "municipal", "incentive", "budget", "fiscal", "million"]
    },
    "07_labor_spinoffs.md": {
        "title": "07 - Labor & Spin-Offs",
        "q_suffix": '(jobs OR employment OR construction OR workforce OR economic)',
        "keywords": ["jobs", "employment", "permanent", "construction", "labor", "worker", "multiplier", "subsidy", "staff", "hiring", "economy"]
    },
    "08_hazards_emergency.md": {
        "title": "08 - Hazards & Emergency Response",
        "q_suffix": '(fire OR battery OR lithium OR emergency OR hazmat)',
        "keywords": ["fire", "battery", "bess", "lithium", "runaway", "hazmat", "emergency", "explosion", "toxic", "suppression", "hazard", "safety"]
    }
}

ddgs = DDGS()

for filename, t_data in topics.items():
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Web Research Ledger: {t_data['title']}\n\n")

    print(f"\n==========================================")
    print(f"Mining Pillar: {t_data['title']}")
    print(f"==========================================")

    seen_urls = set()
    saved_count = 0

    for region_name, base_queries in regions.items():
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"## Region: {region_name}\n\n")

        for bq in base_queries:
            full_query = f"{bq} {t_data['q_suffix']}"
            print(f"  -> Querying [{region_name}]...")

            try:
                results = list(ddgs.text(full_query, max_results=6))
            except Exception as e:
                print(f"     [!] Search warning: {e}")
                time.sleep(2)
                continue

            for r in results:
                url = r.get("href", "")
                title = r.get("title", "Untitled")
                snippet = r.get("body", "")

                if not url or url in seen_urls:
                    continue
                seen_urls.add(url)

                article_text = None
                try:
                    downloaded = trafilatura.fetch_url(url)
                    if downloaded:
                        article_text = trafilatura.extract(downloaded, include_links=False, include_tables=True)
                except Exception:
                    pass

                if article_text and len(article_text.strip()) > 150:
                    paras = [p.strip() for p in article_text.split("\n") if len(p.strip()) > 50]
                    matched = [p for p in paras if any(k in p.lower() for k in t_data["keywords"])]
                    body_out = "\n\n".join(matched[:12]) if matched else "\n\n".join(paras[:8])
                else:
                    body_out = f"**Search Summary Snippet:** {snippet}"

                with open(filepath, "a", encoding="utf-8") as f:
                    f.write(f"### [Source: {title}]\n")
                    f.write(f"**URL:** {url} | **Region:** {region_name}\n\n")
                    f.write(f"{body_out}\n\n---\n\n")
                saved_count += 1

            time.sleep(1.2)

    print(f"  [✓] Saved {saved_count} sources into {filename}")

print("\nWeb mining complete! All 8 regional web ledgers populated.")
