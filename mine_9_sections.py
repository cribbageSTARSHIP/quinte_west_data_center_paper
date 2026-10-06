import os
import time
import json
import urllib.request
import urllib.parse
from ddgs import DDGS
import trafilatura

out_dir = "/opt/data/wiki/raw/articles/nine_sections"
gap_file = "/opt/data/wiki/queries/research_gaps.md"
os.makedirs(out_dir, exist_ok=True)
os.makedirs(os.path.dirname(gap_file), exist_ok=True)

sections = {
    "s1_quinte_west_power.md": {
        "queries": [
            "Quinte West Hydro One Elexicon electricity distribution",
            "IESO East Lake Ontario transmission capacity megawatt",
            "Ontario IESO large load data centre connection requirements"
        ],
        "direct_urls": [
            ("IESO Regional Planning - East Lake Ontario", "https://www.ieso.ca/en/Power-Data"),
        ],
        "wiki_topics": ["Independent Electricity System Operator", "Hydro One"]
    },
    "s2_quinte_west_ecology_watershed.md": {
        "queries": [
            "Lower Trent Conservation Quinte West watershed conservation areas",
            "Quinte West Trenton Bayside drinking water treatment plant",
            "Quinte West Hastings apiary beekeepers wildlife corridor"
        ],
        "direct_urls": [
            ("City of Quinte West Water and Sewer FAQ", "https://quintewest.ca/water-environment/water-sewer-faq/"),
            ("Lower Trent Conservation Watershed Management", "https://ltc.on.ca/")
        ],
        "wiki_topics": ["Quinte West", "Trent River", "Bay of Quinte", "Murray Canal"]
    },
    "s3_glycol_diesel_bees_wildlife.md": {
        "queries": [
            "propylene glycol spill aquatic toxicity biochemical oxygen demand river",
            "data center backup diesel generator fuel storage tank spill",
            "low frequency noise vibration effects on honeybees pollinators"
        ],
        "direct_urls": [],
        "wiki_topics": ["Propylene glycol", "Diesel exhaust", "Decline in insect populations"]
    },
    "s4_acoustics_dbc_property_bees.md": {
        "queries": [
            "data center low frequency noise dBC vs dBA chiller mitigation",
            "data center noise impact residential property values",
            "honeybee vibration communication 100 Hz 500 Hz anthropogenic noise"
        ],
        "direct_urls": [],
        "wiki_topics": ["A-weighting", "Low-frequency noise"]
    },
    "s5_mental_and_physical_health.md": {
        "queries": [
            "low frequency noise sleep disturbance cortisol cardiovascular stress",
            "data center diesel generator PM2.5 NOx respiratory health asthma"
        ],
        "direct_urls": [],
        "wiki_topics": ["Health effects from noise", "Particulates"]
    },
    "s6_mpac_shell_vs_contents_tax.md": {
        "queries": [
            "MPAC Ontario industrial property tax assessment machinery equipment exemption",
            "data center property tax real property shell vs personal property servers"
        ],
        "direct_urls": [
            ("MPAC Industrial Property Assessment", "https://www.mpac.ca/en/PropertyTypes/IndustrialProperties")
        ],
        "wiki_topics": ["Municipal Property Assessment Corporation", "Property tax"]
    },
    "s7_jobs_trades_materials.md": {
        "queries": [
            "data center construction trades vs permanent operational jobs per megawatt",
            "data center facility maintenance contracts local supply chain consumables"
        ],
        "direct_urls": [],
        "wiki_topics": ["Data center"]
    },
    "s8_spill_agencies_and_accidents.md": {
        "queries": [
            "Ontario Spills Action Centre MECP report pollution chemical spill",
            "data center diesel leak battery fire incident investigation"
        ],
        "direct_urls": [
            ("Ontario Spills Action Centre (MECP)", "https://www.ontario.ca/page/report-pollution-and-spills"),
            ("CANUTEC Emergency Response", "https://tc.canada.ca/en/dangerous-goods/canutec")
        ],
        "wiki_topics": ["Thermal runaway"]
    },
    "s9_quinte_west_facilities.md": {
        "queries": [
            "Quinte Health Trenton Memorial Hospital 242 King St",
            "Quinte West Fire Station locations OPP detachment 7 Creswell Drive",
            "Quinte West elementary secondary schools retirement homes addresses"
        ],
        "direct_urls": [
            ("City of Quinte West Contact & Facilities", "https://quintewest.ca/")
        ],
        "wiki_topics": ["Trenton Memorial Hospital", "Trenton High School (Ontario)"]
    }
}

def fetch_wiki_summary(topic):
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(topic)}"
        req = urllib.request.Request(url, headers={"User-Agent": "HermesResearchBot/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("extract", ""), data.get("content_urls", {}).get("desktop", {}).get("page", url)
    except Exception:
        return "", ""

ddgs = DDGS()
gaps = []

for fname, cfg in sections.items():
    fpath = os.path.join(out_dir, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(f"# Targeted Research Ledger: {fname}\n\n")

    print(f"\n==========================================")
    print(f"Mining {fname}...")
    seen = set()
    total_sources = 0

    # 1. Run live DDGS searches
    for q in cfg["queries"]:
        print(f"  -> DDGS Query: {q}")
        q_count = 0
        try:
            results = list(ddgs.text(q, max_results=5))
        except Exception as e:
            print(f"     [!] DDGS warning: {e}")
            results = []

        for r in results:
            url = r.get("href", "") or r.get("link", "")
            title = r.get("title", "Untitled")
            snippet = r.get("body", "") or r.get("snippet", "")
            if not url or url in seen:
                continue
            seen.add(url)

            text = None
            try:
                html = trafilatura.fetch_url(url)
                if html:
                    text = trafilatura.extract(html, include_tables=True)
            except Exception:
                pass

            if text and len(text.strip()) > 200:
                paras = [p.strip() for p in text.split("\n") if len(p.strip()) > 40]
                body = "\n\n".join(paras[:10])
            else:
                body = f"**Search Summary Snippet:** {snippet}"

            with open(fpath, "a", encoding="utf-8") as f:
                f.write(f"## [Source: {title} | {url}]\n\n{body}\n\n---\n\n")
            total_sources += 1
            q_count += 1

        if q_count == 0:
            gaps.append((fname, q))
        time.sleep(1.5)

    # 2. Scrape Direct Authoritative URLs
    for title, url in cfg["direct_urls"]:
        if url in seen:
            continue
        seen.add(url)
        try:
            html = trafilatura.fetch_url(url)
            text = trafilatura.extract(html, include_tables=True) if html else ""
            if text:
                paras = [p.strip() for p in text.split("\n") if len(p.strip()) > 40]
                with open(fpath, "a", encoding="utf-8") as f:
                    f.write(f"## [Source: {title} | {url}]\n\n" + "\n\n".join(paras[:12]) + "\n\n---\n\n")
                total_sources += 1
                print(f"  -> Direct URL captured: {title}")
        except Exception:
            pass

    # 3. Reference Baseline via Wikipedia REST API
    for topic in cfg["wiki_topics"]:
        extract, w_url = fetch_wiki_summary(topic)
        if extract:
            with open(fpath, "a", encoding="utf-8") as f:
                f.write(f"## [Source: Wikipedia Reference - {topic} | {w_url}]\n\n{extract}\n\n---\n\n")
            total_sources += 1
            print(f"  -> Baseline captured: {topic}")

    print(f"  [✓] Finished {fname} with {total_sources} total sources.")

# Write out any 0-result search queries to research_gaps.md
with open(gap_file, "w", encoding="utf-8") as gf:
    gf.write("# Targeted Research Gaps Log\n\n")
    gf.write("The following search queries returned 0 live search results and can be supplemented by dropping specific URLs into `/ingest-url <URL>` or `urls.txt`:\n\n")
    if gaps:
        for sec, q in gaps:
            gf.write(f"- **{sec}**: `{q}`\n")
    else:
        gf.write("- All queries returned live sources!\n")

print(f"\n✓ Completed mining! Gap report saved to {gap_file}")
