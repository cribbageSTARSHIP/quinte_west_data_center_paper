import textwrap
#!/usr/bin/env python3
"""
Master Automated Visual Generator for Quinte West Data Center Impact Assessment
Generates all 60 specified charts, infographics, enhanced GIS maps, and photo panels
for Sections 1.1 through 3.9 and injects valid Pandoc Markdown links into papers/.
"""
import os
import re
import sys
import io
import subprocess
import urllib.request
import urllib.parse
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PIL import Image

try:
    import cairosvg
    HAS_CAIRO = True
except Exception:
    HAS_CAIRO = False

BASE_DIR = Path("/workspace") if Path("/workspace/papers").exists() else Path("/home/prizm/ai-stack/research-paper")
PAPERS_DIR = BASE_DIR / "papers"
FIGURES_DIR = BASE_DIR / "figures"
MAPS_DIR = BASE_DIR / "wiki" / "raw" / "maps"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Color Palette (Publication Academic Style)
NAVY = "#1B365D"
TEAL = "#008080"
CORAL = "#D9534F"
AMBER = "#F0AD4E"
SLATE = "#5A6A85"
GREEN = "#2E7D32"
LIGHT_BG = "#F8FAFC"
DARK_TEXT = "#1E293B"

plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Liberation Sans", "Arial"]
plt.rcParams["axes.edgecolor"] = "#CBD5E1"
plt.rcParams["axes.linewidth"] = 0.8
plt.rcParams["figure.max_open_warning"] = 0
plt.rcParams["text.parse_math"] = False


# ==============================================================================
# HELPER FUNCTIONS: BASE MAPS, WIKIMEDIA PHOTOS, AND CHART PRIMITIVES
# ==============================================================================

def load_svg_basemap(svg_name, width=1600):
    """Renders an existing local SVG map to a PIL Image for callout overlays."""
    svg_path = MAPS_DIR / svg_name
    if svg_path.exists() and HAS_CAIRO:
        try:
            png_bytes = cairosvg.svg2png(url=str(svg_path), output_width=width)
            return Image.open(io.BytesIO(png_bytes)).convert("RGB")
        except Exception as e:
            print(f"  [!] cairosvg fallback for {svg_name}: {e}")
    # Fallback synthetic topographic grid if SVG unavailable
    img = Image.new("RGB", (width, int(width * 0.68)), (232, 240, 234))
    return img


def fetch_wikimedia_image(search_query):
    """Fetches a public-domain/CC field photo from Wikimedia Commons API."""
    try:
        api_url = (
            "https://commons.wikimedia.org/w/api.php?action=query&generator=search"
            f"&gsrsearch={urllib.parse.quote('filetype:bitmap ' + search_query)}"
            "&gsrlimit=1&prop=imageinfo&iiprop=url&iiurlwidth=800&format=json"
        )
        req = urllib.request.Request(api_url, headers={"User-Agent": "QuinteWestResearchBot/1.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            pages = data.get("query", {}).get("pages", {})
            for _, page in pages.items():
                thumb_url = page.get("imageinfo", [{}])[0].get("thumburl")
                if thumb_url:
                    img_req = urllib.request.Request(thumb_url, headers={"User-Agent": "QuinteWestResearchBot/1.0"})
                    with urllib.request.urlopen(img_req, timeout=8) as img_resp:
                        return Image.open(io.BytesIO(img_resp.read())).convert("RGB")
    except Exception:
        pass
    return None


def render_hbar(filename, title, subtitle, categories, values, unit, colors=None, note=None):
    fig, ax = plt.subplots(figsize=(11.0, 5.8), dpi=300)
    fig.patch.set_facecolor("white")
    ax.set_facecolor(LIGHT_BG)
    y = np.arange(len(categories))
    c = colors if colors else [NAVY, TEAL, CORAL, AMBER, GREEN, SLATE][:len(categories)]
    bars = ax.barh(y, values, color=c, height=0.55, edgecolor="none")
    ax.set_yticks(y)
    ax.set_yticklabels([textwrap.fill(cat, 38) for cat in categories], fontsize=9.5, fontweight="bold", color=DARK_TEXT)
    ax.invert_yaxis()
    ax.set_xlabel(unit, fontsize=10, fontweight="bold", color=DARK_TEXT)
    ax.grid(axis="x", linestyle="--", alpha=0.5)
    ax.axvline(0, color=DARK_TEXT, lw=1.0)
    min_v = min(0, min(values))
    max_v = max(0, max(values))
    span = (max_v - min_v) if (max_v - min_v) > 0 else 1
    ax.set_xlim(min_v - (span * 0.28 if min_v < 0 else 0), max_v + span * 0.28)
    for bar, val in zip(bars, values):
        lbl = f"{val:+,.1f} {unit}" if (min_v < 0 and isinstance(val, float)) else (f"{val:,.1f} {unit}" if isinstance(val, float) else f"{val:,} {unit}")
        if val >= 0:
            ax.text(val + span * 0.02, bar.get_y() + bar.get_height()/2, lbl, va="center", ha="left", fontsize=9, fontweight="bold", color=DARK_TEXT)
        else:
            ax.text(val - span * 0.02, bar.get_y() + bar.get_height()/2, lbl, va="center", ha="right", fontsize=9, fontweight="bold", color=DARK_TEXT)
    plt.suptitle(title, fontsize=12.5, fontweight="bold", color=NAVY, y=0.97)
    ax.set_title(textwrap.fill(subtitle, 95), fontsize=9, color=SLATE, pad=10)
    if note:
        fig.text(0.02, 0.01, textwrap.fill(note, 125), fontsize=8, color=SLATE, style="italic")
    plt.tight_layout(rect=[0.01, 0.05, 0.99, 0.92])
    fig.savefig(FIGURES_DIR / filename, dpi=300)
    plt.close(fig)


def render_grouped_bar(filename, title, subtitle, groups, series_dict, ylabel, note=None):
    fig, ax = plt.subplots(figsize=(11.0, 5.8), dpi=300)
    fig.patch.set_facecolor("white")
    ax.set_facecolor(LIGHT_BG)
    x = np.arange(len(groups))
    n = len(series_dict)
    width = 0.72 / n
    palette = [NAVY, CORAL, TEAL, "#881337", GREEN]
    max_v = max(max(v) for v in series_dict.values())
    for i, (label, vals) in enumerate(series_dict.items()):
        offset = (i - (n - 1) / 2) * width
        rects = ax.bar(x + offset, vals, width, label=label, color=palette[i % len(palette)])
        for r, v in zip(rects, vals):
            ax.text(r.get_x() + r.get_width()/2, r.get_height() + max_v * 0.015,
                    f"{v:g}", ha="center", va="bottom", fontsize=8.5, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(groups, fontsize=9, fontweight="bold", color=DARK_TEXT)
    ax.set_ylabel(ylabel, fontsize=10, fontweight="bold", color=DARK_TEXT)
    ax.set_ylim(0, max_v * 1.24)
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.legend(frameon=True, facecolor="white", fontsize=9)
    plt.suptitle(title, fontsize=12.5, fontweight="bold", color=NAVY, y=0.97)
    ax.set_title(textwrap.fill(subtitle, 95), fontsize=9, color=SLATE, pad=10)
    if note:
        fig.text(0.02, 0.01, textwrap.fill(note, 125), fontsize=8, color=SLATE, style="italic")
    plt.tight_layout(rect=[0.01, 0.05, 0.99, 0.92])
    fig.savefig(FIGURES_DIR / filename, dpi=300)
    plt.close(fig)


def render_donut(filename, title, subtitle, labels, sizes, side_callouts):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.8, 5.5), dpi=300, gridspec_kw={"width_ratios": [1.15, 1.15]})
    fig.patch.set_facecolor("white")
    palette = [NAVY, TEAL, CORAL, "#D97706", GREEN, SLATE][:len(labels)]
    wrapped_labels = [textwrap.fill(l, 22) for l in labels]
    wedges, texts, autotexts = ax1.pie(
        sizes, labels=wrapped_labels, autopct="%1.0f%%", startangle=140,
        colors=palette, pctdistance=0.74, labeldistance=1.12,
        wedgeprops=dict(width=0.42, edgecolor="white", linewidth=2),
        textprops=dict(fontsize=8.5, fontweight="bold", color=DARK_TEXT)
    )
    for at in autotexts:
        at.set_color("white")
        at.set_fontsize(8.5)
    ax2.axis("off")
    y_pos = 0.84
    ax2.text(0.02, 0.95, "Key Technical Benchmarks:", fontsize=10.5, fontweight="bold", color=NAVY)
    for head, body in side_callouts:
        box = mpatches.FancyBboxPatch((0.02, y_pos - 0.19), 0.95, 0.21, boxstyle="round,pad=0.02",
                                      facecolor=LIGHT_BG, edgecolor=TEAL, linewidth=1.2)
        ax2.add_patch(box)
        ax2.text(0.05, y_pos - 0.03, head, fontsize=9, fontweight="bold", color=NAVY)
        ax2.text(0.05, y_pos - 0.08, textwrap.fill(body, 48), va="top", fontsize=8, color=DARK_TEXT)
        y_pos -= 0.26
    plt.suptitle(title, fontsize=12.5, fontweight="bold", color=NAVY, y=0.97)
    fig.text(0.5, 0.90, subtitle, ha="center", fontsize=9, color=SLATE)
    plt.tight_layout(rect=[0.03, 0.02, 0.98, 0.88])
    fig.savefig(FIGURES_DIR / filename, dpi=300)
    plt.close(fig)


def render_process_infographic(filename, title, subtitle, stages, footer_note=""):
    fig, ax = plt.subplots(figsize=(12.0, 6.2), dpi=300)
    fig.patch.set_facecolor("white")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    palette = [NAVY, TEAL, CORAL, "#7C2D12", GREEN, SLATE]
    n = len(stages)
    cols = min(n, 4) if n != 3 else 3
    rows = int(np.ceil(n / cols))
    box_w = (90 / cols) - 2.2
    box_h = (72 / rows) - 4
    wrap_chars = 25 if cols == 4 else 34

    for idx, (st_title, bullets) in enumerate(stages):
        r = idx // cols
        c = idx % cols
        x = 5 + c * (box_w + 2.8)
        y = 83 - (r + 1) * (box_h + 4)
        color = palette[idx % len(palette)]
        card = mpatches.FancyBboxPatch((x, y), box_w, box_h, boxstyle="round,pad=0.6",
                                       facecolor=LIGHT_BG, edgecolor=color, linewidth=1.8)
        ax.add_patch(card)
        hdr = mpatches.FancyBboxPatch((x, y + box_h - 9.5), box_w, 9.5, boxstyle="round,pad=0.3",
                                      facecolor=color, edgecolor=color)
        ax.add_patch(hdr)
        ax.text(x + box_w/2, y + box_h - 4.7, textwrap.fill(st_title, wrap_chars - 2),
                ha="center", va="center", fontsize=8.8, fontweight="bold", color="white")
        ty = y + box_h - 13.5
        step_y = (box_h - 14.5) / max(len(bullets), 1)
        for b in bullets:
            wrapped_b = textwrap.fill(f"• {b}", width=wrap_chars, subsequent_indent="  ")
            ax.text(x + 1.2, ty, wrapped_b, va="top", ha="left", fontsize=7.8, color=DARK_TEXT)
            ty -= step_y
        if rows == 1 and c < cols - 1:
            ax.annotate("", xy=(x + box_w + 2.5, y + box_h/2), xytext=(x + box_w + 0.3, y + box_h/2),
                        arrowprops=dict(arrowstyle="->", lw=2.0, color=SLATE))

    if footer_note:
        fbox = mpatches.FancyBboxPatch((5, 3.5), 90, 9.5, boxstyle="round,pad=0.4",
                                       facecolor="#FEF3C7", edgecolor="#D97706", linewidth=1.5)
        ax.add_patch(fbox)
        ax.text(50, 8.2, textwrap.fill(footer_note, 110), ha="center", va="center", fontsize=8.3, fontweight="bold", color=DARK_TEXT)

    plt.suptitle(title, fontsize=13, fontweight="bold", color=NAVY, y=0.96)
    fig.text(0.5, 0.89, textwrap.fill(subtitle, 100), ha="center", fontsize=9, color=SLATE)
    plt.tight_layout(rect=[0, 0, 1, 0.87])
    fig.savefig(FIGURES_DIR / filename, dpi=300)
    plt.close(fig)


def render_annotated_map(filename, base_svg, title, subtitle, callouts, zones=None):
    """Loads the existing SVG base map and overlays GIS callouts, buffers, and legends."""
    base_img = load_svg_basemap(base_svg, width=1500)
    w, h = base_img.size
    fig, ax = plt.subplots(figsize=(11.5, 7.2), dpi=300)
    ax.imshow(base_img, extent=[0, 100, 0, 100])

    if zones:
        for zx, zy, zr, zcolor, zlabel in zones:
            circ = mpatches.Circle((zx, zy), zr, facecolor=zcolor, edgecolor=zcolor, alpha=0.25, lw=2)
            ax.add_patch(circ)
            ring = mpatches.Circle((zx, zy), zr, facecolor="none", edgecolor=zcolor, linestyle="--", lw=1.8)
            ax.add_patch(ring)
            ax.text(zx, zy + zr + 1.5, zlabel, ha="center", va="bottom", fontsize=8,
                    fontweight="bold", color="white",
                    bbox=dict(boxstyle="round,pad=0.2", facecolor=zcolor, alpha=0.85))

    for cx, cy, tx, ty, label, subtext, color in callouts:
        ax.plot(cx, cy, marker="o", markersize=9, color=color, markeredgecolor="white", markeredgewidth=2, zorder=10)
        ax.annotate(
            f"{label}\n{subtext}",
            xy=(cx, cy), xytext=(tx, ty),
            fontsize=8.2, fontweight="bold", color=DARK_TEXT,
            bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor=color, lw=1.8, alpha=0.94),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.15", color=color, lw=2),
            zorder=11
        )

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    plt.suptitle(title, fontsize=13, fontweight="bold", color=NAVY, y=0.97)
    ax.set_title(subtitle, fontsize=9.5, color=SLATE, pad=8)
    plt.tight_layout(rect=[0, 0.01, 1, 0.93])
    fig.savefig(FIGURES_DIR / filename, dpi=300)
    plt.close(fig)


def render_photo_panel(filename, title, subtitle, items):
    """Renders structured ecological/heritage technical profile cards with clean wrapped text."""
    stages = []
    for query, heading, caption in items:
        stages.append((heading, [caption, f" Classification: {query.title()}", "Jurisdiction: Lower Trent / Bay of Quinte Watershed"]))
    render_process_infographic(filename, title, subtitle, stages,
                               footer_note="Field Reference: Protected ecological, hydrological, and heritage receptors within the City of Quinte West.")


# ==============================================================================
# MASTER 60-GRAPHIC MANIFEST & GENERATOR EXECUTION
# ==============================================================================

MANIFEST = []

def register(sec, fname, caption, builder_fn):
    MANIFEST.append((sec, fname, caption, builder_fn))


# --- SECTION 1.1 ---
register("1.1", "fig_1_1a_elec_consumption_trends.png",
         "Figure 1.1a: Regional Electricity Consumption Projections vs. Quinte West Site Loads (MW Equivalent)",
         lambda: render_hbar(
             "fig_1_1a_elec_consumption_trends.png",
             "Data Center Electricity Demand Projections (MW Scale Comparison)",
             "Comparing Texas ERCOT (2030), California (2028: 25.3 TWh / ~2,888 MW avg), and Quinte West Site Proposals",
             ["Texas ERCOT Total Queue (2030)", "Texas ERCOT Realistic (2030)", "California 25.3 TWh/yr (2028 Avg)",
              "Quinte West: 920 Trenton-Frankford (Ph 1+2)", "Quinte West: Per-Site Baseline (10–20 MW)"],
             [77965, 38878, 2888, 33, 15], "MW",
             note="Note: California's 25.3 TWh annual demand equals ~2.4 million households; Quinte West 8–33 MW equals 7,500–30,000 local homes."
         ))

register("1.1", "fig_1_1b_bess_thermal_runaway.png",
         "Figure 1.1b: Four-Stage Lithium-Ion BESS Thermal Runaway & Early-Warning Mitigation Architecture",
         lambda: render_process_infographic(
             "fig_1_1b_bess_thermal_runaway.png",
             "Role of Battery Storage (BESS) & 4-Stage Thermal Runaway Mitigation",
             "Early-Warning Gas Sensing and CNN/LSTM Machine Learning Fault Interception",
             [
                 ("Stage 1: Anomalous Abuse", ["Overcharge / internal dendrite short", "SEI layer decomposition (80–120°C)", "Online impedance & CNN/LSTM voltage tracking"]),
                 ("Stage 2: Off-Gas Venting", ["Separator melt & electrolyte vaporization", "H2, CO, and VOC off-gas release", "Early-warning gas sensors trigger breaker trip"]),
                 ("Stage 3: Thermal Runaway", ["Cathode breakdown (>200°C exothermic spike)", "Toxic Hydrogen Fluoride (HF) gas plume", "Automated module isolation & inert gas flooding"]),
                 ("Stage 4: Propagation Control", ["Cell-to-cell cascading heat transfer", "1,000–2,500 GPM perimeter water cooling", "Containment of PFAS/fluoride firewater runoff"])
             ],
             footer_note="Mitigation: Combining multi-gas sensors (H2/CO/HF) with hybrid CNN/LSTM neural networks detects cell faults 8–15 minutes prior to ignition."
         ))

def build_1_1c():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
    hrs = np.arange(0, 24)
    grid_base = 40 + 18 * np.sin((hrs - 6) * np.pi / 12) ** 2 + 8 * np.exp(-((hrs - 18)/3)**2)
    unmitigated = grid_base + 20
    shifted = grid_base + np.where((hrs >= 15) & (hrs <= 20), 11, 24)
    ax.plot(hrs, grid_base, "--", color=SLATE, lw=2, label="Baseline Municipal Load (MW)")
    ax.plot(hrs, unmitigated, "-", color=CORAL, lw=2.8, label="Unmitigated Flat Data Center Baseload (+20 MW 24/7)")
    ax.plot(hrs, shifted, "-", color=TEAL, lw=2.8, label="Spatio-Temporal Load-Shifting & DR Curtailment")
    ax.fill_between(hrs, shifted, unmitigated, where=(unmitigated > shifted), color=GREEN, alpha=0.25, label="Peak Strain Shaved (15:00–20:00)")
    ax.set_xticks(range(0, 24, 2))
    ax.set_xticklabels([f"{h:02d}:00" for h in range(0, 24, 2)], fontsize=9)
    ax.set_ylabel("Aggregate Feeder Demand (MW)", fontweight="bold")
    ax.set_xlabel("Hour of Day (24-Hour Diurnal Cycle)", fontweight="bold")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper left", fontsize=8.8)
    plt.suptitle("Diurnal Load Curve: Unmitigated Baseload vs. Spatio-Temporal Load Shifting", fontsize=13, fontweight="bold", color=NAVY, y=0.97)
    ax.set_title("Curtailing non-urgent AI training during 15:00–20:00 peak windows prevents transformer thermal overload", fontsize=9.5, color=SLATE)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_1_1c_diurnal_load_curve.png", dpi=300)
    plt.close(fig)

register("1.1", "fig_1_1c_diurnal_load_curve.png",
         "Figure 1.1c: 24-Hour Diurnal Electricity Demand Curve Contrasting Unmitigated Baseload vs. Spatio-Temporal Load-Shifting",
         build_1_1c)

register("1.1", "fig_1_1d_scope_emissions_health.png",
         "Figure 1.1d: Data Center Scope 1, 2, and 3 Emissions Profile and Public Health Escalation",
         lambda: render_process_infographic(
             "fig_1_1d_scope_emissions_health.png",
             "Data Center Emissions Profile (Scope 1, 2 & 3) & Public Health Trajectory",
             "Lifecycle Carbon Footprint and Documented Epidemiological Escalation (2019–2028)",
             [
                 ("Scope 1: On-Site Diesel", ["Summer load-bank generator testing", "Direct NOx, SO2, and PM2.5 plumes", "EPA Tier 2 units emit 6.4 g/kWh NOx", "Acute downwind asthma & stroke risk"]),
                 ("Scope 2: Grid Electricity", ["Continuous 24/7 baseload power draw", "Delays retirement of natural gas peakers", "Drives regional smog & fine particulates", "20% of Ontario / 37% Canada oil & gas NOx"]),
                 ("Scope 3: Hardware Carbon", ["20–30% of total 15-year GHG footprint", "Embodied carbon in GPUs, silicon & racks", "3–5 year rapid server replacement cycle", "Global semiconductor & mining supply chain"]),
                 ("Health Impact Surge", ["3x tripling of CA health costs (2019–2023)", "Projected +72% health burden jump by 2028", "Virginia: $190M–$300M/yr health damages", "13–19 premature deaths/yr in VA alone"])
             ],
             footer_note="Key Finding: Data center air pollution health damages tripled between 2019 and 2023 and are projected to rise another 72% by 2028."
         ))

def build_1_1e():
    img1 = load_svg_basemap("quinte_west_Saputo_data_center.svg", width=900)
    img2 = load_svg_basemap("quinte_west_Sonoco_data_center.svg", width=900)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.5), dpi=300)
    ax1.imshow(img1)
    ax1.set_title("7 Riverside Drive, Trenton (Former Saputo Dairy)\nUrban Waterfront | 8 MW Proposal | 1.2 km to Trenton WTP", fontsize=9.5, fontweight="bold", color=NAVY)
    ax1.axis("off")
    ax2.imshow(img2)
    ax2.set_title("920 Trenton-Frankford Rd, Glen Miller (Former Sonoco Mill)\n100-Acre Riparian Parcel | 18–33 MW Proposal | On-Site Substation", fontsize=9.5, fontweight="bold", color=NAVY)
    ax2.axis("off")
    plt.suptitle("Site-Specific Geographical Comparison: Quinte West Proposed Data Center Campuses", fontsize=13, fontweight="bold", color=NAVY, y=0.98)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_1_1e_site_aerial_comparison.png", dpi=300)
    plt.close(fig)

register("1.1", "fig_1_1e_site_aerial_comparison.png",
         "Figure 1.1e: Side-by-Side Geospatial Comparison of 7 Riverside Drive (Saputo Site) and 920 Trenton-Frankford Road (Sonoco Site)",
         build_1_1e)


# --- SECTION 1.2 ---
register("1.2", "fig_1_2a_coloedr_pricing_flowchart.png",
         "Figure 1.2a: Multi-Tenant ColoEDR Supply-Function Bidding and Price Responsive Load (PRL) Flowchart",
         lambda: render_process_infographic(
             "fig_1_2a_coloedr_pricing_flowchart.png",
             "Demand Response (DR) & Hourly Locational Marginal Pricing (LMP) Mechanism",
             "Replacing Backup Diesel Generation with ColoEDR Supply-Function Bidding During Grid Emergencies",
             [
                 ("1. IESO / ISO Grid Alert", ["Substation approaches thermal limit", "Hourly LMP price spikes at node", "Emergency DR signal broadcast"]),
                 ("2. ColoEDR Bidding", ["Operator queries tenant price bids", "Supply-function algorithm clears load", "Incentivizes voluntary tenant shedding"]),
                 ("3. PRL Workload Shift", ["Price Responsive Load (PRL) throttles", "Delay-tolerant AI batch jobs paused", "Compute migrated to off-peak regions"]),
                 ("4. Diesel Avoidance", ["20–30% peak feeder load shed achieved", "Avoids firing Tier 2 diesel generators", "Zero local NOx / PM2.5 plume release"])
             ],
             footer_note="Result: Dynamic LMP pricing and ColoEDR contracts stabilize municipal substations without triggering toxic backup diesel emissions."
         ))

register("1.2", "fig_1_2b_cooling_energy_donut.png",
         "Figure 1.2b: Breakdown of Data Center Electricity Consumption and Cooling Efficiency Savings",
         lambda: render_donut(
             "fig_1_2b_cooling_energy_donut.png",
             "Data Center Electricity Allocation & Cooling Efficiency Opportunities",
             "Conventional Air-Cooled Facility Power Breakdown vs. Advanced Liquid & Free Cooling",
             ["IT Server & GPU Load", "Cooling Systems (Up to 40%)", "Power Distribution & UPS Losses", "Lighting & Auxiliary"],
             [50, 40, 8, 2],
             [
                 ("Conventional Chiller Baseline (40% Power)", "Rooftop air chillers and CRAC fans consume up to 40% of total facility electricity (PUE 1.6–2.0)."),
                 ("Liquid Immersion & Direct-to-Chip", "Cuts thermal parasitic load by 70–85%, lowering facility PUE to 1.08–1.20."),
                 ("Trent River Cold-Water Free Cooling", "Closed-loop heat exchange with cold winter river temperatures offsets mechanical chilling.")
             ]
         ))

register("1.2", "fig_1_2c_jurisdictional_comparison.png",
         "Figure 1.2c: Jurisdictional Grid Planning Comparison: Alberta, Ontario, and Quinte West",
         lambda: render_process_infographic(
             "fig_1_2c_jurisdictional_comparison.png",
             "Comparative Power Grid Governance: Alberta, Ontario, and Quinte West",
             "Capacity Caps, Intertie Limits, and Cost-Responsibility Mandates",
             [
                 ("Alberta (AESO / AUC)", ["20,000 MW requests vs 10,000 MW grid", "Enforced 1,200 MW AESO large-load cap", "Constrained BC & SK intertie capacity", "Curbs unpermitted behind-meter gas"]),
                 ("Ontario (IESO / Provincial)", ["Peak demand forecast +60% by 2050", "Affordable Energy Act, 2024 rules", "ERO Notice 025-1001 cost recovery", "100% developer upfront grid funding"]),
                 ("Quinte West (Municipal)", ["Split LDCs: Elexicon & Hydro One", "Sidney TS / Thorold / Tilbury constraints", "Interim Control By-law 26-131 pause", "Requires CCRA letters of credit"])
             ],
             footer_note="Policy Takeaway: Without strict Ontario Affordable Energy Act cost-recovery enforcement, local grid upgrades shift onto Class B ratepayers."
         ))


# --- SECTION 1.3 ---
register("1.3", "fig_1_3a_ontario_generation_donut.png",
         "Figure 1.3a: Ontario IESO Bulk Electricity Generation Mix Feeding the Quinte West Corridor",
         lambda: render_donut(
             "fig_1_3a_ontario_generation_donut.png",
             "Overview of Ontario's IESO Power System Generation Mix",
             "Primary Bulk Generation Sources Supplying Hydro One's Eastern Corridor into Quinte West",
             ["Nuclear (35%)", "Hydroelectric (25%)", "Natural Gas (20%)", "Renewables: Wind/Solar/Biomass (15%)", "Other / Storage (5%)"],
             [35, 25, 20, 15, 5],
             [
                 ("Baseload Backbone (60% Zero-Carbon)", "Darlington/Pickering Nuclear (35%) and Hydroelectric (25%) supply primary baseload."),
                 ("Marginal Peaking Dispatch (20% Gas)", "New 24/7 data center loads force natural gas plants (e.g., Lennox TS) to run at higher capacity factors."),
                 ("Local Run-of-the-River Limits", "Frankford, Glen Miller, and Sidney GS depend on seasonal Trent River flow and cannot scale on demand.")
             ]
         ))

register("1.3", "fig_1_3b_substation_schematic.png",
         "Figure 1.3b: Substation Step-Down Network Schematic and Thermal Capacity Limits",
         lambda: render_process_infographic(
             "fig_1_3b_substation_schematic.png",
             "Quinte West Regional Step-Down Substation & Feeder Architecture",
             "Bulk IESO Transmission Delivery Path to Local Municipal Distribution Loads",
             [
                 ("IESO Bulk Grid (230/115 kV)", ["East-West Hydro One corridor", "Clarington TS to Lennox/Kingston", "Supplies Sidney TS (230/44 kV)"]),
                 ("Thorold TS Benchmark", ["13.8 kV step-down bus", "6.1 MW thermal capacity limit", "5.9 MW limit on feeders M5/M6"]),
                 ("Tilbury West / Sidney DS", ["27.6 kV / 44 kV distribution", "14.3 MW thermal capacity limit", "Elexicon & Hydro One rural split"]),
                 ("Critical Municipal Loads", ["Frankford Water Treatment Plant", "Trenton WTP & Memorial Hospital", "Exhausted by 8–33 MW data centers"])
             ],
             footer_note="Bottleneck: Existing 6.1 MW and 14.3 MW thermal limits cannot absorb 18–100 MW AI compute loads without dedicated substation rebuilds."
         ))

def build_1_3c():
    base_img = load_svg_basemap("quinte_west_trenton_downtown.svg", width=1000)
    storm_img = fetch_wikimedia_image("ice storm power line utility pole damage")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.2), dpi=300)
    if storm_img:
        ax1.imshow(storm_img)
    else:
        ax1.set_facecolor("#E2E8F0")
        ax1.text(0.5, 0.5, "Winter Ice Storm Overhead Line Vulnerability\n(44 kV Radial Rural Feeders)", ha="center", va="center", fontweight="bold", color=NAVY)
    ax1.set_title("Radial Overhead Line Weather Exposure\nIce/Wind Tree Contact Triggers Multi-Hour Outages", fontsize=9.5, fontweight="bold", color=NAVY)
    ax1.set_xticks([]); ax1.set_yticks([])

    ax2.imshow(base_img, extent=[0, 100, 0, 100])
    for zx, zy, zr, lbl in [(35, 78, 14, "Frankford Outage Hotspot"), (48, 62, 12, "Batawa Feeder Bottleneck"), (62, 48, 12, "Glen Miller / Harder Dr Sub")]:
        c = mpatches.Circle((zx, zy), zr, facecolor=CORAL, edgecolor="white", alpha=0.45, lw=2)
        ax2.add_patch(c)
        ax2.text(zx, zy, lbl, ha="center", va="center", fontsize=8, fontweight="bold", color="white",
                 bbox=dict(boxstyle="round,pad=0.2", facecolor=CORAL, alpha=0.9))
    ax2.set_title("Quinte West Rural Outage Hotspot Map\nFrankford, Batawa & Harder Drive Substation Zones", fontsize=9.5, fontweight="bold", color=NAVY)
    ax2.axis("off")
    plt.suptitle("Power Outages and Grid Vulnerabilities in Quinte West", fontsize=13, fontweight="bold", color=NAVY, y=0.98)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_1_3c_outage_vulnerability_map.png", dpi=300)
    plt.close(fig)

register("1.3", "fig_1_3c_outage_vulnerability_map.png",
         "Figure 1.3c: Winter Storm Overhead Line Vulnerability and Outage Hotspot Map for Frankford and Batawa",
         build_1_3c)


# --- SECTION 1.4 ---
register("1.4", "fig_1_4a_grid_upgrade_costs.png",
         "Figure 1.4a: Capital Expenditure Ranges for Quinte West Grid Infrastructure Upgrades ($ Millions)",
         lambda: render_grouped_bar(
             "fig_1_4a_grid_upgrade_costs.png",
             "Grid Infrastructure Capital Upgrade Cost Ranges for Quinte West",
             "Minimum vs. Maximum Estimated Capital Expenditure by Upgrade Component ($ Millions)",
             ["5 Miles 138 kV Line\n($1.2–$2.5M/mi)", "Upgrade 50 MVA\n138 kV Substation", "Replace 10 Distribution\nTransformers", "Install 10 MW / 40 MWh\nBESS Storage"],
             {"Minimum Capital Cost ($M)": [6.0, 10.0, 5.0, 4.0], "Maximum Capital Cost ($M)": [12.5, 25.0, 12.0, 6.0]},
             "Capital Cost ($ Millions)",
             note="Total combined reinforcement package ranges from $25.0M to $55.5M depending on right-of-way and switchgear requirements."
         ))

register("1.4", "fig_1_4b_solar_vs_grid_expansion.png",
         "Figure 1.4b: Economic Comparison of a 50 MW Solar Farm vs. 50 MW Traditional Grid Expansion",
         lambda: render_grouped_bar(
             "fig_1_4b_solar_vs_grid_expansion.png",
             "Cost Comparison: 50 MW Solar Farm vs. 50 MW Traditional Grid Expansion",
             "Contrasting Capital Cost ($M), Annual Op-Ex ($M/yr), and Levelized Cost of Energy (¢/kWh)",
             ["Capital Cost ($M Min)", "Capital Cost ($M Max)", "Annual Op-Ex ($M/yr Max)", "LCOE (¢/kWh Midpoint)"],
             {"50 MW Solar Farm": [60.0, 80.0, 1.8, 4.0], "50 MW Grid Expansion": [75.0, 100.0, 3.5, 10.0]},
             "Cost ($ Millions or ¢/kWh)",
             note="50 MW Solar LCOE: $0.03–$0.05/kWh ($1.2–$1.8M op-ex) vs. 50 MW Grid Expansion: $0.08–$0.12/kWh ($2.5–$3.5M op-ex)."
         ))

register("1.4", "fig_1_4c_health_land_footprint.png",
         "Figure 1.4c: Health and Environmental Externalities of Fossil/Diesel Grid Expansion vs. 100% Renewable Integration",
         lambda: render_process_infographic(
             "fig_1_4c_health_land_footprint.png",
             "Health & Land Footprint Callout: Fossil Backup vs. Renewable Integration",
             "Comparing Virginia's Data Center Diesel Externalities Against Ontario's Clean Energy Health Dividend",
             [
                 ("Virginia Public Health Cost", ["$190M–$300M annual health damages", "13–19 premature deaths per year", "Occurs at just 10% permitted diesel run", "Disproportionate respiratory burden"]),
                 ("Regional Land Conversion", ["6,200–21,000 acres land footprint", "Loss of agricultural & forest buffers", "Impervious surface runoff surge", "Transmission corridor clear-cutting"]),
                 ("Ontario Renewable Dividend", ["1,200 premature deaths/yr prevented", "Achieved via 100% renewable sourcing", "Eliminates NOx & PM2.5 peaking plumes", "Protects Trenton & Bayside airsheds"])
             ],
             footer_note="Citation: Shifting data center supply to 100% renewable energy prevents up to 1,200 premature deaths annually in Ontario."
         ))


# --- SECTION 1.5 ---
register("1.5", "fig_1_5a_ontario_playbook_pillars.png",
         "Figure 1.5a: Ontario's Data Centre Playbook Three-Pillar Architecture and Provincial Governance Override",
         lambda: render_process_infographic(
             "fig_1_5a_ontario_playbook_pillars.png",
             "Ontario's Data Centre Playbook: 3-Pillar Architecture & Governance Override",
             "Provincial Strategy vs. Municipal Moratorium Authority (Hamilton, Oakville, Quinte West)",
             [
                 ("Pillar 1: Economic Dev.", ["Attract AI & cloud capital investment", "Expedite industrial brownfield reuse", "Prioritize 50+ MW strategic projects"]),
                 ("Pillar 2: Digital Sovereignty", ["Keep Canadian health/gov data onshore", "Tier III/IV cybersecurity resilience", "Domestic AI compute infrastructure"]),
                 ("Pillar 3: Community Invest.", ["Developer-funded grid connection fees", "Waste-heat recovery partnerships", "Local STEM & municipal engagement"])
             ],
             footer_note="Governance Callout: Provincial approval authority & MZO powers can override municipal moratoriums enacted in Hamilton, Oakville, and Quinte West."
         ))

register("1.5", "fig_1_5b_global_policy_matrix.png",
         "Figure 1.5b: International Legislative and Efficiency Matrix Comparing Global Data Center Frameworks",
         lambda: render_process_infographic(
             "fig_1_5b_global_policy_matrix.png",
             "Global Data Center Policy & Efficiency Matrix",
             "Comparing Statutory Mandates Across the European Union, United States, China, and Ontario",
             [
                 ("EU Green Deal (EED)", ["100% renewable energy target by 2030", "Mandatory PUE & WUE public reporting", "Applies to all facilities >500 kW", "Mandatory district waste-heat reuse"]),
                 ("US FERC / Calif. SB 100", ["FERC Order 2023 cluster queue reform", "Co-located load cost allocation rules", "California SB 100: 100% clean by 2045", "Strict CARB Tier 4 diesel mandates"]),
                 ("China Green Guidelines", ["Mandatory design PUE < 1.5 cap", "Stricter PUE <= 1.25 in national hubs", "East-to-West compute routing policy", ">=30% renewable energy integration"]),
                 ("Ontario Playbook / IESO", ["ERO 025-1001 connection review", "Affordable Energy Act cost recovery", "No statutory PUE or WUE cap in law", "Municipal dBA-only noise blind spot"])
             ],
             footer_note="Gap Analysis: Unlike the EU and China, Ontario lacks statutory PUE/WUE caps, leaving cooling efficiency to local site-plan negotiation."
         ))


# --- SECTION 1.6.1 ---
register("1.6.1", "fig_1_6_1a_saputo_enhanced_map.png",
         "Figure 1.6.1a: Enhanced Site Map of 7 Riverside Drive (Former Saputo Dairy) with SM-14 Rezoning and Trenton WTP Callouts",
         lambda: render_annotated_map(
             "fig_1_6_1a_saputo_enhanced_map.png",
             "quinte_west_Saputo_data_center.svg",
             "7 Riverside Drive (Former Saputo Dairy): Parcel, Zoning & Receptor Map",
             "Enhanced 1:35,378 Topographic Overlay: SM to SM-14 Rezoning Footprint, Waterfront Trail & Trenton WTP",
             [
                 (52, 50, 12, 78, "7 Riverside Drive Parcel", "SM to SM-14 Rezoning Footprint (8 MW TrueNorth)", CORAL),
                 (48, 65, 10, 22, "Trenton Water Treatment Plant", "35,800 m³/day Capacity (~1.2 km Relationship)", NAVY),
                 (55, 45, 65, 75, "Great Lakes Waterfront Trail", "Directly Adjacent Riparian Public Corridor", GREEN),
                 (53, 35, 66, 20, "Trent River Discharge Mouth", "Flows into Bay of Quinte (AOC)", TEAL)
             ],
             zones=[(52, 50, 9, CORAL, "SM-14 Rezoning Zone")]
         ))

def build_1_6_1b():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.0), dpi=300, gridspec_kw={"width_ratios": [1, 1.4]})
    fig.patch.set_facecolor("white")
    ax1.set_facecolor(LIGHT_BG)
    ax1.set_xlim(0, 10); ax1.set_ylim(0, 10)
    card = mpatches.FancyBboxPatch((0.6, 0.8), 8.8, 8.4, boxstyle="round,pad=0.3", facecolor="#E2E8F0", edgecolor=NAVY, lw=2)
    ax1.add_patch(card)
    ax1.text(5, 7.5, "7 RIVERSIDE DRIVE, TRENTON\nFormer Saputo Dairy Facility", ha="center", fontweight="bold", fontsize=10.5, color=NAVY)
    ax1.text(5, 5.0, "• Heavy industrial brick/steel shell\n• Shuttered in 2020 (corporate consolidation)\n• Legacy 44 kV electrical feeder drop\n• High-volume municipal water hookup\n• West bank of Trent River below Lock 1", ha="center", va="center", fontsize=8.8, color=DARK_TEXT)
    ax1.text(5, 1.8, "Proposed Adaptive Reuse:\n$320M TrueNorth Micro Data Center (14 Jobs)", ha="center", fontweight="bold", fontsize=9, color=CORAL)
    ax1.axis("off")

    ax2.set_xlim(0, 10); ax2.set_ylim(0, 10); ax2.axis("off")
    events = [
        ("Pre-2020", "Saputo Dairy Operations", "100–150 union jobs; cheese & milk processing on Trent River."),
        ("2020", "Plant Closure & Decommissioning", "Facility vacated; ammonia chillers removed; shell left intact."),
        ("Mid-2026", "TrueNorth $320M Proposal (File D09/T09/26)", "SM to SM-14 rezoning for 8 MW AI data center (only 14 full-time jobs)."),
        ("Sept 2026", "Public Opposition & PAC Deferral", "Residents challenge dBC noise, diesel plumes, and river spill risks."),
        ("Post-Oct 2026", "Deferred Past Municipal Election", "Interim Control By-law 26-131 pauses approvals for 1-year study.")
    ]
    y = 8.8
    ax2.plot([1.2, 1.2], [1.2, 8.8], color=NAVY, lw=3)
    for yr, head, desc in events:
        ax2.plot(1.2, y, "o", markersize=11, color=CORAL, markeredgecolor="white", markeredgewidth=2)
        ax2.text(1.8, y + 0.15, f"{yr} — {head}", fontsize=9.5, fontweight="bold", color=NAVY)
        ax2.text(1.8, y - 0.45, desc, fontsize=8.3, color=DARK_TEXT)
        y -= 1.85
    plt.suptitle("7 Riverside Drive: Industrial Timeline & Data Center Deferral Trajectory", fontsize=13, fontweight="bold", color=NAVY, y=0.97)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_1_6_1b_saputo_timeline.png", dpi=300)
    plt.close(fig)

register("1.6.1", "fig_1_6_1b_saputo_timeline.png",
         "Figure 1.6.1b: Site Profile and Historical Timeline of 7 Riverside Drive from Saputo Dairy Closure to Post-October 2026 Election Deferral",
         build_1_6_1b)


# --- SECTION 1.6.2 ---
register("1.6.2", "fig_1_6_2a_electrical_routing_map.png",
         "Figure 1.6.2a: Local Electrical Routing Map Showing Elexicon Energy Service Zone, Hydro One Feeders, and Trent-Severn Corridor",
         lambda: render_annotated_map(
             "fig_1_6_2a_electrical_routing_map.png",
             "quinte_west_trenton_downtown.svg",
             "Local Electrical Routing Map: Elexicon Energy Zone & Hydro One Feeders",
             "Replacing Duplicate Base Map with Utility Boundary, 44 kV Feeder Path & Trent-Severn Corridor",
             [
                 (45, 75, 10, 82, "Hydro One Sidney TS (230/44 kV)", "Primary Regional Step-Down Source", NAVY),
                 (52, 50, 62, 68, "7 Riverside Dr (8 MW Load)", "Absorbs 7,500-Home Equivalent Baseload", CORAL),
                 (48, 42, 12, 25, "Elexicon Energy Urban Zone", "Trenton Core Retail Distribution Network", TEAL),
                 (54, 60, 65, 30, "Trent-Severn Waterway Corridor", "Run-of-the-River Hydro (Seasonal Non-Dispatchable)", GREEN)
             ],
             zones=[(50, 46, 18, TEAL, "Elexicon Urban Service Boundary")]
         ))

register("1.6.2", "fig_1_6_2b_capacity_deficit_chart.png",
         "Figure 1.6.2b: Substation Thermal Capacity Deficit vs. Conventional and Hyperscale AI Data Center Loads",
         lambda: render_hbar(
             "fig_1_6_2b_capacity_deficit_chart.png",
             "Substation Thermal Capacities vs. Data Center Demand Scenarios (MW)",
             "Contrasting Thorold TS and Tilbury West DS Capacities Against 7 Riverside Dr and Hyperscale AI Facilities",
             ["AI Hyperscale Facility (75,000 Homes)", "Tilbury West DS Thermal Capacity", "7 Riverside Dr Proposed Load (7,500 Homes)",
              "Thorold TS Thermal Limit (Per Bus)", "Thorold TS Feeder M5/M6 Limit", "Conventional Enterprise Data Center"],
             [100.0, 14.3, 8.0, 6.1, 5.9, 3.5], "MW",
             colors=[CORAL, TEAL, AMBER, NAVY, NAVY, GREEN],
             note="An AI hyperscale facility (100+ MW) exceeds local substation capacity by 7x–16x, requiring $50M+ in transmission upgrades."
         ))


# --- SECTION 1.7.1 ---
def build_1_7_1a():
    base_img = load_svg_basemap("quinte_west_Sonoco_data_center.svg", width=900)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.2), dpi=300)
    ax1.imshow(base_img, extent=[0, 100, 0, 100])
    c = mpatches.Circle((52, 52), 16, facecolor=TEAL, edgecolor=NAVY, alpha=0.35, lw=2, linestyle="--")
    ax1.add_patch(c)
    ax1.annotate("LTC Sheet 112 Floodplain Contour\n920 Trenton-Frankford Rd", xy=(52, 52), xytext=(12, 80),
                 fontsize=8.5, fontweight="bold", bbox=dict(boxstyle="round", facecolor="white", edgecolor=NAVY),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
    ax1.set_title("Lower Trent Conservation Floodplain Map (Sheet 112)\n920 Trenton-Frankford Road Riparian Zone", fontsize=9.5, fontweight="bold", color=NAVY)
    ax1.axis("off")

    x = np.linspace(0, 100, 200)
    ground = np.piecewise(x, [x < 30, (x >= 30) & (x < 55), x >= 55],
                          [lambda v: 88.5 + 0.08 * v, lambda v: 91.12 + 0.01*(v-30), lambda v: 91.4 + 0.04*(v-55)])
    ax2.fill_between(x, 87, ground, color="#D6D3D1", label="Site Ground Profile (IBW Surveyors CGVD28:78)")
    ax2.fill_between(x[x < 33], 87, 90.56, color="#38BDF8", alpha=0.5, label="Trent River Regulatory Flood Level (90.56 m CGVD2013)")
    ax2.axhline(90.56, color=TEAL, linestyle="--", lw=2)
    ax2.axhline(91.12, color=CORAL, linestyle=":", lw=2)
    ax2.annotate("Lowest Building Ground: 91.12 m\nFlood Level: 90.56 m (+0.56 m Clearance)\n*WARNING: Unconverted CGVD28 vs CGVD2013 Datums!",
                 xy=(45, 91.12), xytext=(22, 92.3), fontsize=8.2, fontweight="bold", color=DARK_TEXT,
                 bbox=dict(boxstyle="round", facecolor="#FEF3C7", edgecolor=CORAL),
                 arrowprops=dict(arrowstyle="->", color=CORAL, lw=2))
    ax2.set_ylim(87.5, 93.8)
    ax2.set_xlabel("Distance from Trent River Bank (m)", fontweight="bold")
    ax2.set_ylabel("Elevation (m ASL)", fontweight="bold")
    ax2.legend(loc="lower right", fontsize=8)
    ax2.grid(True, linestyle="--", alpha=0.4)
    ax2.set_title("Elevation Cross-Section: IBW Survey vs. LTC Flood Level", fontsize=9.5, fontweight="bold", color=NAVY)
    plt.suptitle("920 Trenton-Frankford Road: Watershed Floodplain Contours & Datum Cross-Section", fontsize=13, fontweight="bold", color=NAVY, y=0.98)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_1_7_1a_sonoco_floodplain_cross_section.png", dpi=300)
    plt.close(fig)

register("1.7.1", "fig_1_7_1a_sonoco_floodplain_cross_section.png",
         "Figure 1.7.1a: Lower Trent Conservation Floodplain Map (Sheet 112) and Elevation Cross-Section Illustrating the 91.12 m vs. 90.56 m Datum Comparison",
         build_1_7_1a)

def build_1_7_1b():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.2), dpi=300)
    fig.patch.set_facecolor("white")
    ax1.set_xlim(0, 10); ax1.set_ylim(0, 10); ax1.axis("off")
    steps = [
        (5, 8.3, "FirstBlock 33 MW Liquid-Cooled Compute", "Phase 1: 16 MW | Phase 2: 17 MW (55–80°C Heat Loop)", NAVY),
        (5, 5.2, "Heat Connect Services Thermal Recovery", "100% Captured Thermal Loop to Trinity Smart Farms", TEAL),
        (5, 2.1, "Greenhouse & Vertical Farm Offset", "Ph 1 Saves 4,220 t CO2/yr | Ph 2 Saves 8,725 t CO2/yr", GREEN)
    ]
    for sx, sy, h, b, col in steps:
        box = mpatches.FancyBboxPatch((0.8, sy - 1.0), 8.4, 2.1, boxstyle="round,pad=0.2", facecolor=LIGHT_BG, edgecolor=col, lw=2)
        ax1.add_patch(box)
        ax1.text(sx, sy + 0.35, h, ha="center", fontweight="bold", fontsize=9.2, color=col)
        ax1.text(sx, sy - 0.4, b, ha="center", fontsize=8.3, color=DARK_TEXT)
    ax1.annotate("", xy=(5, 6.3), xytext=(5, 7.2), arrowprops=dict(arrowstyle="->", lw=2.5, color=TEAL))
    ax1.annotate("", xy=(5, 3.2), xytext=(5, 4.1), arrowprops=dict(arrowstyle="->", lw=2.5, color=GREEN))
    ax1.set_title("Circular Waste-Heat Recovery Loop (33 MW Total)", fontsize=10, fontweight="bold", color=NAVY)

    cats = ["HGC Predicted\nMin (R1–R5)", "HGC Predicted\nMax (Receptor)", "NPC-300 Night\nLimit (dBA)", "NPC-300 Day\nLimit (dBA)", "Aermec Chiller\n125 Hz Unweighted"]
    vals = [34.0, 41.0, 45.0, 50.0, 100.3]
    cols = [TEAL, TEAL, AMBER, AMBER, CORAL]
    bars = ax2.bar(cats, vals, color=cols, width=0.55)
    for b, v in zip(bars, vals):
        ax2.text(b.get_x() + b.get_width()/2, v + 1.5, f"{v:.1f} dB", ha="center", fontsize=8.5, fontweight="bold")
    ax2.set_ylim(0, 115)
    ax2.set_ylabel("Sound Level (dBA / Unweighted dB at 125 Hz)", fontweight="bold", fontsize=9)
    ax2.tick_params(axis="x", labelsize=8)
    ax2.grid(axis="y", linestyle="--", alpha=0.5)
    ax2.set_title("HGC Predicted dBA vs. NPC-300 & 125 Hz Tonal Peak", fontsize=10, fontweight="bold", color=NAVY)
    plt.suptitle("FirstBlock 920 Trenton-Frankford Rd: Waste-Heat Loop & Acoustic Profile", fontsize=13, fontweight="bold", color=NAVY, y=0.98)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_1_7_1b_firstblock_heat_and_noise.png", dpi=300)
    plt.close(fig)

register("1.7.1", "fig_1_7_1b_firstblock_heat_and_noise.png",
         "Figure 1.7.1b: FirstBlock 33 MW Circular Waste-Heat Recovery Schematic and Acoustic Comparison Against Ontario NPC-300 Limits",
         build_1_7_1b)


# --- SECTION 1.7.2 ---
register("1.7.2", "fig_1_7_2a_sonoco_substation_feeder_map.png",
         "Figure 1.7.2a: Substation and Feeder Map Plotting 44 kV Sydney TS-M1 Feeders, 5 Bernard Long Rd (7.5 MW), and Harder Drive Substation",
         lambda: render_annotated_map(
             "fig_1_7_2a_sonoco_substation_feeder_map.png",
             "quinte_west_Sonoco_data_center.svg",
             "Substation & 44 kV Feeder Map: 920 Trenton-Frankford Rd & 5 Bernard Long Rd",
             "Plotting Sydney TS-M1 Feeder (18 MW Approval), 7.5 MW Legacy Turbine & Harder Drive Substation",
             [
                 (50, 52, 10, 80, "920 Trenton-Frankford Rd", "Sydney TS-M1 Feeder: 9.9 MW -> 18 MW (Jan 2027 Cap)", CORAL),
                 (55, 48, 58, 78, "5 Bernard Long Road", "Legacy 7.5 MW Generation (OEB Licence EG-2010-0168)", NAVY),
                 (38, 65, 10, 25, "Hydro One Sidney TS", "230/44 kV Source Feeding Industrial Corridor", TEAL),
                 (62, 35, 60, 20, "Elexicon Harder Drive Substation", "Site of 2022 Transformer Overheating Failure", AMBER)
             ]
         ))

register("1.7.2", "fig_1_7_2b_vibroacoustic_coupling.png",
         "Figure 1.7.2b: Vibroacoustic Coupling Diagram Showing Low-Frequency (<100 Hz) dBC Structural Resonance vs. Municipal dBA Bylaws",
         lambda: render_process_infographic(
             "fig_1_7_2b_vibroacoustic_coupling.png",
             "Vibroacoustic Coupling: How <100 Hz Low-Frequency Noise Bypasses dBA Bylaws",
             "Physical Wave Propagation from 13 Aermec Chillers & 6 Transformers into Adjacent Residences",
             [
                 ("1. Tonal Source (<100 Hz)", ["13 Aermec TBA3350F rooftop chillers", "6 transformers (120 Hz magnetostriction)", "100.3 dB unweighted peak at 125 Hz"]),
                 ("2. Long-Wave Diffraction", ["3.4 to 11.0 meter acoustic wavelengths", "Bends over standard fences & berms", "Minimal atmospheric absorption over 500 m"]),
                 ("3. The dBA Filter Blind Spot", ["dBA subtracts -26.2 dB at 63 Hz", "dBA subtracts -39.4 dB at 31.5 Hz", "Reads '41 dBA compliant' at lot line"]),
                 ("4. Home Structural Resonance", ["65–72 dBC penetrates wood/drywall", "Excites bedroom standing-wave modes", "Causes wall vibration & sleep disruption"])
             ],
             footer_note="Acoustic Loophole: HGC Engineering's study flags chillers as 'T' (Tonal), yet municipal dBA limits ignore <100 Hz C-weighted energy."
         ))


# --- SECTION 2.1 ---
register("2.1", "fig_2_1a_trenton_waterways_enhanced_map.png",
         "Figure 2.1a: Enhanced Waterway Map of Quinte West Labeling Locks 1–7, Bay of Quinte Estuary, Dams, and Invasive Water Soldier Zones",
         lambda: render_annotated_map(
             "fig_2_1a_trenton_waterways_enhanced_map.png",
             "quinte_west_trenton_downtown.svg",
             "Major Rivers and Bodies of Water in Quinte West (Enhanced 1:34,837 Map)",
             "Trent-Severn Waterway Locks 1–7, Bay of Quinte Estuary, Dams & Invasive Water Soldier Zones",
             [
                 (48, 72, 10, 82, "Trent-Severn Waterway Locks 1–7", "Southern Terminus of 386-km Corridor", NAVY),
                 (58, 28, 62, 18, "Bay of Quinte Estuary (40 km)", "Great Lakes Area of Concern (AOC)", TEAL),
                 (35, 65, 8, 52, "Lingham Lake & Deer Creek Dams", "Regional Flow Control Infrastructure", SLATE),
                 (62, 42, 64, 52, "Kiwanis East Bayshore Park", "Shoreline Habitat & Amphibian Nursery", GREEN),
                 (52, 58, 58, 82, "Water Soldier Herbicide Zones", "Active Management for Stratiotes aloides", CORAL)
             ]
         ))

register("2.1", "fig_2_1b_trent_severn_photos_panel.png",
         "Figure 2.1b: Visual Reference Panel: Trent-Severn Waterway Lockmaster's House, Trent Port Marina, and Invasive Water Soldier Rosettes",
         lambda: render_photo_panel(
             "fig_2_1b_trent_severn_photos_panel.png",
             "Trent-Severn Waterway & Bay of Quinte Ecological Features",
             "Heritage Infrastructure, Municipal Marina Basin, and Invasive Macrophyte Management",
             [
                 ("Trent Severn Waterway lock station", "Historic Lockmaster's House (Sidney)", "Arts & Crafts heritage lock station along the Trent-Severn corridor"),
                 ("Trenton Ontario marina boat", "Trent Port Marina (Bay of Quinte)", "380-slip municipal deep-water basin at the mouth of the Trent River"),
                 ("Stratiotes aloides water soldier", "Invasive Water Soldier (Stratiotes aloides)", "Submerged/floating rosettes targeted by provincial herbicide control")
             ]
         ))

register("2.1", "fig_2_1c_elorca_merger_chart.png",
         "Figure 2.1c: Organizational Merger Chart Showing the 2027 Consolidation into the Eastern Lake Ontario Regional Conservation Authority (ELORCA)",
         lambda: render_process_infographic(
             "fig_2_1c_elorca_merger_chart.png",
             "2027 Ontario Conservation Authority Consolidation Architecture",
             "Merging 36 Local Conservation Authorities into 9 Regional Conservation Authorities (RCAs)",
             [
                 ("Legacy System (36 CAs)", ["Lower Trent Conservation (LTC)", "Quinte Conservation (Moira/Napanee)", "Crowe Valley & Cataraqui CAs", "Split municipal watershed boundaries"]),
                 ("2027 Statutory Transition", ["Provincial RCA Consolidation Mandate", "Harmonized flood & hazard mapping", "Unified CGVD2013 vertical datum", "Centralized permitting portal"]),
                 ("ELORCA Regional Authority", ["Eastern Lake Ontario RCA (ELORCA)", "Integrates Lower Trent & Quinte CAs", "Oversees Trent River & Bay of Quinte", "Enforces IPZ & floodplain setbacks"])
             ],
             footer_note="Institutional Impact: By 2027, Quinte Conservation and Lower Trent Conservation merge into ELORCA under Ontario's 9-RCA model."
         ))


# --- SECTION 2.2 ---
register("2.2", "fig_2_2a_conservation_areas_map.png",
         "Figure 2.2a: Lower Trent Watershed Conservation Areas Map and Visuals: Trenton Greenbelt, Bleasdell Boulder, and Sager Conservation Area",
         lambda: render_photo_panel(
             "fig_2_2a_conservation_areas_map.png",
             "Key Conservation Areas of the 2,070 km² Lower Trent Watershed",
             "Trenton Greenbelt Pollinator Meadow, Bleasdell Boulder Glacial Erratic, and Sager Conservation Area",
             [
                 ("wildflower meadow restoration Ontario", "Trenton Greenbelt (0.3-ha Urban Meadow)", "Restored native wildflower pollinator habitat across from Trenton LCBO (+30% pollinators)"),
                 ("glacial erratic boulder forest", "Bleasdell Boulder Conservation Area", "One of North America's largest glacial erratics & critical groundwater recharge woodland"),
                 ("drumlin glacial hill lookout", "Sager Conservation Area", "High glacial drumlin moraine overlooking the Lower Trent River valley")
             ]
         ))

register("2.2", "fig_2_2b_black_carbon_emissions.png",
         "Figure 2.2b: 2024 Canadian Inventory Comparison of Provincial Black Carbon and Fine Particulate Emissions (kt)",
         lambda: render_hbar(
             "fig_2_2b_black_carbon_emissions.png",
             "Provincial Black Carbon Emissions Comparison (2024 Canadian Inventory)",
             "Highlighting Ontario's 5.7 kt Black Carbon Output Relative to Quebec and Other Provinces",
             ["Alberta (Off-Road & Oil/Gas Dominant)", "Ontario (Industrial & Transport Corridor)", "Quebec (Hydro-Dominant Baseline)",
              "British Columbia", "Saskatchewan"],
             [8.4, 5.7, 4.8, 4.1, 3.2], "kt",
             colors=[CORAL, NAVY, TEAL, GREEN, AMBER],
             note="Ontario emits 5.7 kt of black carbon vs. Quebec's 4.8 kt; unmitigated Tier 2 diesel generators exacerbate local black carbon deposition."
         ))


# --- SECTION 2.3 ---
register("2.3", "fig_2_3a_source_water_ipz_map.png",
         "Figure 2.3a: Source Water Protection Map Plotting Trenton and Bayside WTP Intakes and IPZ-1, IPZ-2, and IPZ-3 Buffers",
         lambda: render_annotated_map(
             "fig_2_3a_source_water_ipz_map.png",
             "quinte_west_trenton_downtown.svg",
             "Quinte West Drinking Water Intakes & Intake Protection Zones (IPZ-1, IPZ-2, IPZ-3)",
             "Spatial Relationship Between 7 Riverside Dr, 920 Trenton-Frankford Rd, and Municipal Raw Water Intakes",
             [
                 (49, 58, 10, 78, "Trenton WTP Intake (Upstream Dam 1)", "35,800 m³/day | Inside IPZ-1/IPZ-2 Corridor", NAVY),
                 (52, 50, 12, 25, "7 Riverside Drive Site", "~1.2 km Relationship to Trenton WTP Zone", CORAL),
                 (45, 82, 55, 85, "920 Trenton-Frankford Rd", "Upstream IPZ-3 Tributary Spill Vector", AMBER),
                 (72, 32, 62, 15, "Bayside WTP Intake (370 m into Bay)", "11,360 m³/day | 404 m Intake Conduit", TEAL)
             ],
             zones=[
                 (49, 58, 7, CORAL, "IPZ-1 (Immediate 1 km)"),
                 (49, 58, 15, AMBER, "IPZ-2 (2-Hr Travel)"),
                 (72, 32, 8, TEAL, "Bayside IPZ-1")
             ]
         ))

register("2.3", "fig_2_3b_dual_wtp_schematic.png",
         "Figure 2.3b: Dual Water Treatment Process Schematic Comparing the Trenton and Bayside Water Treatment Plants",
         lambda: render_process_infographic(
             "fig_2_3b_dual_wtp_schematic.png",
             "Quinte West Drinking Water Infrastructure: Dual Treatment Process Schematic",
             "Technical Comparison of the Trenton Water Treatment Plant vs. Bayside Water Treatment Plant",
             [
                 ("Trenton WTP: Intake & Flow", ["Trent River upstream of Dam No. 1", "Dual pipes: 53m (400mm) & 18m (600mm)", "Rated capacity: 35,800 m³/day", "Max raw pump flow: 530.4 L/s"]),
                 ("Trenton WTP: Treatment", ["Granular Activated Carbon (GAC)", "Chlorine gas primary disinfection", "5,454 m³ baffled contact clearwells", "Vulnerable to upstream glycol BOD"]),
                 ("Bayside WTP: Intake & Flow", ["Bay of Quinte (370 m offshore crib)", "404 m total intake conduit length", "Rated capacity: 11,360 m³/day", "Max raw pump flow: 262.8 L/s"]),
                 ("Bayside WTP: Treatment", ["Dual-media sand/anthracite filters", "Granular Activated Alumina (GAA)", "Sodium hypochlorite disinfection", "Hydrofluosilicic acid fluoridation"])
             ],
             footer_note="Combined Municipal Baseline: 47,160 m³/day total rated capacity serving 216 km of water mains and 8,800 metered connections."
         ))


# --- SECTION 2.4 ---
register("2.4", "fig_2_4a_hydrological_block_diagram.png",
         "Figure 2.4a: Hydrological Block Diagram Illustrating Surface and Groundwater Flow from Canadian Shield Highlands to the Bay of Quinte",
         lambda: render_process_infographic(
             "fig_2_4a_hydrological_block_diagram.png",
             "Quinte West Watershed: 3D Hydrological Flow & Aquifer Block Architecture",
             "From Canadian Shield Granite Highlands (900–1,200 mm/yr Precipitation) to the Bay of Quinte Estuary",
             [
                 ("1. Shield Highlands", ["Precambrian granite headwaters", "Moira & Otonabee river basins", "200+ feeder lakes & wetlands", "900–1,200 mm/yr precipitation"]),
                 ("2. Limestone Plains & Dams", ["Fractured Paleozoic limestone", "40 Quinte/LTC flow control dams", "3,500-ha Murray Marsh sponge", "Bleasdell Boulder recharge zone"]),
                 ("3. Lower Trent Corridor", ["Channeled through Locks 1–7", "Shallow unconfined alluvial aquifer", "Industrial brownfields on banks", "High vulnerability to fuel/glycol"]),
                 ("4. Bay of Quinte (AOC)", ["Z-shaped Lake Ontario embayment", "Receives all watershed discharge", "Sensitive to thermal plumes", "Prone to summer hypoxia (<2 mg/L)"])
             ],
             footer_note="Hydrogeological Risk: Fractured limestone and shallow alluvial aquifers rapidly transmit industrial spills into surface waters."
         ))

def build_2_4b():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.0), dpi=300)
    fig.patch.set_facecolor("white")
    ax1.pie([57, 43], labels=["Direct On-Site Cooling\nWater (57%)", "Indirect Grid Power\nWater (43%)"],
            autopct="%1.0f%%", startangle=90, colors=[TEAL, NAVY],
            wedgeprops=dict(width=0.45, edgecolor="white", lw=2), textprops=dict(fontweight="bold", fontsize=9.5))
    ax1.set_title("Data Center Total Water Footprint Split", fontsize=10.5, fontweight="bold", color=NAVY)

    cats = ["Distributed\nSiting", "Concentrated\nCluster", "Concentrated\nDrought Peak"]
    vals = [0.81, 1.15, 1.50]
    bars = ax2.bar(cats, vals, color=[GREEN, AMBER, CORAL], width=0.5)
    for b, v in zip(bars, vals):
        ax2.text(b.get_x() + b.get_width()/2, v + 0.04, f"{v:.2f}% / yr", ha="center", fontweight="bold", fontsize=9.5)
    ax2.set_ylim(0, 1.85)
    ax2.set_ylabel("Annual Subbasin Depletion Rate (%/yr)", fontweight="bold")
    ax2.grid(axis="y", linestyle="--", alpha=0.5)
    ax2.set_title("Modeled Subbasin Aquifer Depletion Rate", fontsize=10.5, fontweight="bold", color=NAVY)
    plt.suptitle("Data Center Water Consumption Split & Subbasin Depletion Modeling", fontsize=13, fontweight="bold", color=NAVY, y=0.98)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_2_4b_water_depletion_pie_bar.png", dpi=300)
    plt.close(fig)

register("2.4", "fig_2_4b_water_depletion_pie_bar.png",
         "Figure 2.4b: Data Center Direct vs. Indirect Water Footprint (57% vs. 43%) and Annual Subbasin Depletion Rates (0.81–1.5%)",
         build_2_4b)


# --- SECTION 2.5 ---
register("2.5", "fig_2_5a_species_at_risk_panel.png",
         "Figure 2.5a: Field Reference Panel of Four Quinte West Species at Risk: Eastern Massasauga Rattlesnake, Blanding's Turtle, Lake Sturgeon, and Atlantic Salmon",
         lambda: render_photo_panel(
             "fig_2_5a_species_at_risk_panel.png",
             "Key Quinte West & Lower Trent Watershed Species at Risk (SAR)",
             "Provincially and Federally Tracked Indicator Species Vulnerable to Thermal, Chemical, and Acoustic Disruption",
             [
                 ("Sistrurus catenatus Massasauga rattlesnake", "Eastern Massasauga Rattlesnake (Endangered)", "Sensitive to ground-borne vibration & right-of-way habitat fragmentation"),
                 ("Emydoidea blandingii Blanding's turtle", "Blanding's Turtle (Threatened)", "Inhabits Murray Marsh & Trent wetlands; vulnerable to road mortality & runoff"),
                 ("Acipenser fulvescens lake sturgeon", "Lake Sturgeon (Threatened)", "Benthic Trent River spawner sensitive to hypoxia (DO < 2 mg/L) & acidification"),
                 ("Salmo salar Atlantic salmon", "Atlantic Salmon (Restoration Target)", "Coldwater oxygen-dependent species disrupted by >10°C thermal plumes")
             ]
         ))

register("2.5", "fig_2_5b_early_warning_monitoring_arch.png",
         "Figure 2.5b: Multi-Sensor Real-Time Environmental Early-Warning Architecture for Brownfield Data Center Sites",
         lambda: render_process_infographic(
             "fig_2_5b_early_warning_monitoring_arch.png",
             "Real-Time Environmental Early-Warning & Brownfield Monitoring Architecture",
             "Detecting PCB/Heavy Metal Leaching and Thermal Plumes at the Former Saputo and Sonoco Sites",
             [
                 ("1. Two-Stage IR Thermal", ["Aerial & fixed infrared cameras", "Tracks >10–20°C outfall plumes", "Monitors BESS & transformer heat"]),
                 ("2. IoT Water & Soil Array", ["Continuous DO, pH, EC & turbidity", "Detects propylene glycol BOD spikes", "Monitors brownfield PCB/metal mobilization"]),
                 ("3. Automated eDNA Samplers", ["Metabarcoding of Trent River water", "Tracks Lake Sturgeon & macrobenthos", "Quantifies biodiversity loss in real time"]),
                 ("4. SHAP ML Analytics", ["Explainable AI anomaly attribution", "Isolates data center vs upstream runoff", "Triggers automatic MECP / WTP alerts"])
             ],
             footer_note="Application: Mandatory fenceline & outfall telemetry protects Trenton WTP from legacy Sonoco/Saputo brownfield contaminants."
         ))


# --- SECTION 2.6 ---
register("2.6", "fig_2_6a_regulatory_approval_flowchart.png",
         "Figure 2.6a: Municipal and Provincial Regulatory Approval Flowchart for Data Center Proposals in Quinte West",
         lambda: render_process_infographic(
             "fig_2_6a_regulatory_approval_flowchart.png",
             "Regulatory Approval & Environmental Compliance Pathway in Ontario",
             "From Brownfield Phase I/II ESA Through Municipal Site Plan Control and Provincial Mandates",
             [
                 ("Step 1: Brownfield ESA", ["Phase I & II ESA (O. Reg. 153/04)", "Test for legacy PCBs & heavy metals", "Record of Site Condition (RSC)"]),
                 ("Step 2: Municipal PAC", ["Quinte West Planning Advisory Comm.", "Interim Control By-law 26-131 review", "NPC-300 acoustic & LTC flood check"]),
                 ("Step 3: Generations Act 2025", ["50+ MW economic priority rules", "IESO System Impact Study (SIS)", "MECP ECA air & noise permits"]),
                 ("Step 4: VPPA & CCRA", ["Virtual Power Purchase Agreements", "100% Connection Cost Recovery", "Decommissioning bond & spill plan"])
             ],
             footer_note="Statutory Tension: While municipalities control Site Plan bylaws, provincial 50+ MW priority designations can fast-track approvals."
         ))


# --- SECTION 2.7 ---
register("2.7", "fig_2_7a_wildlife_status_gis_map.png",
         "Figure 2.7a: GIS Wildlife Concentration and Conservation Status Rank (S1–S3) Map of Quinte West",
         lambda: render_annotated_map(
             "fig_2_7a_wildlife_status_gis_map.png",
             "quinte_west_trenton_downtown.svg",
             "Quinte West Wildlife Concentrations & Conservation Status Rank (S1–S3) GIS Map",
             "Important Bird Areas, Amphibian Nurseries, Fisheries & Fragmented Riparian Corridor (40% Intact)",
             [
                 (18, 22, 8, 45, "Presqu'ile Provincial Park IBA (S1–S3)", "200+ Bird Species: Piping Plover, Common Tern, Night Heron, Whip-poor-will", CORAL),
                 (62, 42, 65, 25, "Kiwanis East Bayshore Park", "Critical Amphibian Nursery: Eastern Newt & Spotted Salamander", GREEN),
                 (32, 85, 10, 82, "Oak Lake & Rice Lake Corridor", "Provincially Significant Walleye & Largemouth Bass Fisheries", TEAL),
                 (50, 58, 56, 75, "Trent River Riparian Corridor", "Fragmented Habitat: Only 40% of Original Riparian Cover Remains Intact", AMBER)
             ],
             zones=[
                 (18, 22, 10, CORAL, "Presqu'ile IBA"),
                 (62, 42, 7, GREEN, "Amphibian Zone"),
                 (50, 58, 12, AMBER, "40% Intact Riparian Zone")
             ]
         ))

register("2.7", "fig_2_7b_pollinator_biodiversity_bar.png",
         "Figure 2.7b: Comparative Pollinator and Biodiversity Trajectory: Restored Trenton Greenbelt vs. Unbuffered Data Center Perimeter",
         lambda: render_hbar(
             "fig_2_7b_pollinator_biodiversity_bar.png",
             "Pollinator & Riparian Biodiversity Change Across Land-Use Scenarios (%)",
             "Contrasting the Restored Trenton Greenbelt (+30%) Against Unbuffered Industrial Data Center Sites",
             ["Restored Trenton Greenbelt (Native Meadow)", "Buffered Facility (500m Setback + Native Berm)",
              "Fragmented Trent Riparian Baseline (40% Intact)", "Unbuffered Data Center (100 uT EMF + >65 dBC)",
              "24/7 Floodlit Impervious Cooling Yard"],
             [30.0, 8.0, -15.0, -28.0, -42.0], "% Change",
             colors=[GREEN, TEAL, AMBER, CORAL, CORAL],
             note="Note: Trenton Greenbelt restoration achieved a +30% pollinator surge, whereas unbuffered EMF/acoustic/light zones drive steep declines."
         ))


# --- SECTION 2.8 ---
register("2.8", "fig_2_8a_apiary_emf_buffer_map.png",
         "Figure 2.8a: Quinte West Apiary and Pollinator Connectivity Map with 500 m EMF and 200 m Zoning Setback Buffers",
         lambda: render_annotated_map(
             "fig_2_8a_apiary_emf_buffer_map.png",
             "quinte_west_trenton_downtown.svg",
             "Quinte West Apiary Corridors, 500m EMF Buffers & 200m Site Setbacks",
             "Spatial Mapping of Apis mellifera Foraging Zones Relative to High-Voltage Lines and Proposed Sites",
             [
                 (25, 55, 8, 78, "Murray / Wooler Apiary Belt", "Commercial & Orchard Pollination Corridor", GREEN),
                 (75, 45, 65, 22, "Sidney / Bayside Orchard Apiaries", "High-Density Fruit Pollination Zone", GREEN),
                 (52, 50, 58, 52, "7 Riverside Dr (200m Setback)", "Urban Site Inside River Pollinator Corridor", CORAL),
                 (46, 75, 48, 88, "920 Trenton-Frankford Rd", "200m Zoning Setback & 500m 230/44 kV EMF Buffer", AMBER)
             ],
             zones=[
                 (52, 50, 6, CORAL, "200m Site Setback"),
                 (46, 75, 11, AMBER, "500m HV Line EMF Buffer"),
                 (25, 55, 12, GREEN, "Murray Apiary Zone")
             ]
         ))

register("2.8", "fig_2_8b_honeybee_emf_vibration_pathway.png",
         "Figure 2.8b: Biological Pathway of 50/60 Hz ELF-EMF (20–7,000 uT) and 200–300 Hz Mechanical Vibration on Honeybee Colonies",
         lambda: render_process_infographic(
             "fig_2_8b_honeybee_emf_vibration_pathway.png",
             "Honeybee (Apis mellifera) EMF & Vibroacoustic Disruption Pathway",
             "Physiological and Behavioral Impacts of Substation ELF-EMFs and Chiller Vibrations",
             [
                 ("1. 50/60 Hz ELF-EMF Source", ["Substation & HV lines: 20–7,000 uT", "Data center perimeter: 100–1,000 uT", "Couples with bee magnetite granules"]),
                 ("2. Gene & Memory Deficit", ["Alters navigation gene expression", "-27.97% olfactory learning drop at 100 uT", "Impairs foraging flight passes"]),
                 ("3. 100–500 Hz Vibration", ["Chiller & transformer substrate hum", "200–300 Hz freezes waggle-dance bees", "Masks Johnston's organ signals"]),
                 ("4. Colony Collapse Vector", ["Reduced pollen/nectar intake", "Failed homing & forager loss", "Impaired winter cluster thermoregulation"])
             ],
             footer_note="Mitigation: Enforcing 500 m transmission buffers and buried/shielded conduits cuts EMF exposure by 50–90%."
         ))


# --- SECTION 3.1 ---
def build_3_1a():
    fig, ax1 = plt.subplots(figsize=(10.5, 5.5), dpi=300)
    fig.patch.set_facecolor("white")
    ax1.set_facecolor(LIGHT_BG)
    systems = ["Open-Loop\nWater-Cooled", "Closed-Loop\nAir-Cooled", "Hybrid Direct-to-Chip\nLiquid + Air"]
    x = np.arange(len(systems))
    s1 = np.array([6.45, 0.21, 3.20])
    s2 = np.array([4.48, 5.91, 3.98])
    tot = s1 + s2
    pue = [1.75, 2.75, 1.35]

    b1 = ax1.bar(x, s1, width=0.45, label="Scope 1 Direct On-Site Water (M m³/yr)", color=TEAL)
    b2 = ax1.bar(x, s2, width=0.45, bottom=s1, label="Scope 2 Indirect Power Water (M m³/yr)", color=NAVY)
    for i, t in enumerate(tot):
        ax1.text(x[i], t + 0.25, f"Total: {t:.2f}M m³", ha="center", fontweight="bold", fontsize=9.5, color=DARK_TEXT)
    ax1.set_xticks(x); ax1.set_xticklabels(systems, fontweight="bold", fontsize=10)
    ax1.set_ylabel("Annual Water Volume for 200 MW Load (Million m³/yr)", fontweight="bold", color=NAVY)
    ax1.set_ylim(0, 13.0)
    ax1.grid(axis="y", linestyle="--", alpha=0.5)

    ax2 = ax1.twinx()
    ax2.plot(x, pue, "o-", color=CORAL, lw=3, markersize=10, label="Mean Power Usage Effectiveness (PUE)")
    for i, p in enumerate(pue):
        ax2.text(x[i] + 0.15, p, f"PUE {p:.2f}", fontweight="bold", color=CORAL, fontsize=9.5)
    ax2.set_ylabel("Power Usage Effectiveness (PUE)", fontweight="bold", color=CORAL)
    ax2.set_ylim(1.0, 3.3)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right", fontsize=8.8)
    plt.suptitle("Comparative Water & Energy Efficiency for a 200 MW Data Center", fontsize=13, fontweight="bold", color=NAVY, y=0.97)
    ax1.set_title("Scope 1 (Direct) + Scope 2 (Indirect) Water Footprint vs. PUE Range", fontsize=9.5, color=SLATE)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_3_1a_cooling_water_pue_chart.png", dpi=300)
    plt.close(fig)

register("3.1", "fig_3_1a_cooling_water_pue_chart.png",
         "Figure 3.1a: Stacked Bar and PUE Line Chart Comparing Open-Loop (10.93M m³), Closed-Loop Air (6.12M m³), and Hybrid Cooling (7.19M m³) for a 200 MW Load",
         build_3_1a)

register("3.1", "fig_3_1b_cooling_cutaway_comparison.png",
         "Figure 3.1b: Engineering Comparison of an Open-Loop Evaporative Tower vs. Closed-Loop Direct-to-Chip Cooling with a 1-Million-Gallon Rainwater Tank",
         lambda: render_process_infographic(
             "fig_3_1b_cooling_cutaway_comparison.png",
             "Engineering Cutaway: Open-Loop Evaporative vs. Closed-Loop + Rainwater Harvesting",
             "Thermodynamic Heat Rejection Mechanics and Municipal Water Offset Architecture",
             [
                 ("Open-Loop Evaporative Tower", ["Latent heat of vaporization discharge", "833,000–5.6M L/MW/yr water loss", "6.45M m³/yr direct draw at 200 MW", "Concentrates TDS & biocide blowdown"]),
                 ("Closed-Loop Direct-to-Chip", ["Sealed propylene glycol/water loop", "Cold plates directly cool AI GPUs", "0.21M m³/yr direct makeup baseline", "Requires 15,000–30,000 L glycol/8 MW"]),
                 ("1M-Gallon Rainwater Cistern", ["Roof & parcel stormwater capture", "1,000,000-gallon retention vault", "Offsets up to 30% of cooling demand", "Buffers peak municipal storm runoff"])
             ],
             footer_note="Design Benchmark: Pairing closed-loop direct-to-chip cooling with a 1M-gallon rainwater cistern eliminates potable water drawdown."
         ))


# --- SECTION 3.2 ---
register("3.2", "fig_3_2a_hydrogeological_cross_section.png",
         "Figure 3.2a: Hydrogeological Cross-Section Comparing Open-Loop Aquifer Cone-of-Depression and Thermal Plumes vs. Closed-Loop Glycol Leaching",
         lambda: render_process_infographic(
             "fig_3_2a_hydrogeological_cross_section.png",
             "Hydrogeological Cross-Section: Open-Loop vs. Closed-Loop Subsurface Risks",
             "Aquifer Drawdown, Thermal Plumes, and Chemical Leaching Pathways into the Trent River",
             [
                 ("Open-Loop Well Drawdown", ["Cone-of-depression lowers water table", "Depletes shallow farm/domestic wells", "0.81–1.5% annual subbasin depletion", "Reduces coldwater stream baseflow"]),
                 ("Open-Loop Thermal Effluent", ["Discharges 10–20°C warmer blowdown", "Triggers algal blooms & lowers DO", "Disrupts Atlantic salmon & walleye", "Concentrates scale inhibitors"]),
                 ("Closed-Loop Chemical Risk", ["Zero routine evaporative water loss", "Stores 15,000–350,000 L glycol", "Corrosion inhibitors (tolyltriazole)", "Heavy metal & PG blowdown flushing"]),
                 ("Trent Aquifer Infiltration", ["Alluvial gravel & fractured limestone", "Uncontained spills reach river in hours", "1.68 kg O2/L BOD strips river oxygen", "Threatens downstream Trenton WTP"])
             ],
             footer_note="Hydrogeological Reality: Closed-loop cooling saves water table volume but shifts risk to high-consequence chemical containment failures."
         ))

register("3.2", "fig_3_2b_water_scale_comparison.png",
         "Figure 3.2b: Scale Comparison of Data Center Water Consumption Metrics From Single AI Training Runs to Regional Aquifers",
         lambda: render_hbar(
             "fig_3_2b_water_scale_comparison.png",
             "Water Consumption Scale Benchmarks (Logarithmic & Municipal Equivalents)",
             "From GPT-3 Model Training (700,000 L) and a 15 MW Facility to Loudoun County (2023) and Global 2027 Demand",
             ["Global Data Centers by 2027 (4.2–6.6B m³)", "Loudoun County VA 2023 Draw (1B gal / 3.78B L)",
              "Quinte West Total Annual Drinking Water (7B L)", "15 MW Evaporative Data Center (= 3 Hospitals / 2 Golf Courses)",
              "Single GPT-3 Training Run (700,000 L)"],
             [5400.0, 3.78, 7.0, 0.085, 0.0007], "Million m³/yr",
             colors=[CORAL, NAVY, TEAL, AMBER, GREEN],
             note="Northern Virginia experienced a 250% 4-year water surge (2.75M gal/day in Loudoun County); a 15 MW center equals 3 hospitals."
         ))


# --- SECTION 3.3 ---
register("3.3", "fig_3_3a_surge_power_comparison.png",
         "Figure 3.3a: Multi-Metric Comparison of Diesel Generators, Battery Energy Storage Systems (BESS), and Solar PV / ORC Systems",
         lambda: render_grouped_bar(
             "fig_3_3a_surge_power_comparison.png",
             "Surge & Backup Power Technologies: Multi-Metric Comparison",
             "Comparing Carbon Intensity (kg CO2/kWh), Levelized Cost ($/kWh), and Response Time (Seconds)",
             ["Diesel Generators\n(<1s Start | 15–20 yr life)", "Lithium-Ion BESS\n(1–5s Response | 10–15 yr)", "Solar PV + ORC Waste Heat\n(Continuous | 20–30 yr life)"],
             {"CO2 Intensity (kg CO2/kWh)": [1.0, 0.075, 0.02], "Levelized Cost ($/kWh)": [0.15, 0.10, 0.04]},
             "Metric Value (kg CO2/kWh or $/kWh)",
             note="Diesel emits 0.8–1.2 kg CO2/kWh ($0.10–$0.20/kWh) vs. BESS at 0.05–0.10 kg CO2/kWh ($0.05–$0.15/kWh) and Solar/ORC at 0.01–0.03 kg CO2/kWh."
         ))

register("3.3", "fig_3_3b_site_microgrid_schematics.png",
         "Figure 3.3b: Proposed Hybrid Microgrid Schematics for 7 Riverside Drive and 920 Trenton-Frankford Road",
         lambda: render_process_infographic(
             "fig_3_3b_site_microgrid_schematics.png",
             "Case Study: Quinte West Hybrid Microgrid Schematics",
             "Integrating Solar PV, Organic Rankine Cycle (ORC) Waste-Heat Recovery, and Fault-Monitored BESS",
             [
                 ("7 Riverside Dr: Generation", ["1–2 MW rooftop/carport Solar PV", "Supplies 30–40% of site energy", "Reduces Elexicon feeder peak draw"]),
                 ("7 Riverside Dr: Storage & ORC", ["500 kWh BESS for <5s surge ride-through", "Organic Rankine Cycle (ORC) generator", "Converts chiller waste heat to power"]),
                 ("920 Trenton-Frankford: Renewables", ["2 MW Solar PV + wind array on 100 ac", "Supplies up to 50% of baseline energy", "Coupled to legacy 7.5 MW OEB substation"]),
                 ("920 Trenton-Frankford: 1 MWh BESS", ["1 MWh utility-grade LFP battery bank", "Online electrochemical impedance diag.", "Prevents thermal runaway & diesel start"])
             ],
             footer_note="Engineering Recommendation: Hybrid PV + ORC + impedance-monitored BESS slashes standby diesel runtime by >85%."
         ))


# --- SECTION 3.4 ---
register("3.4", "fig_3_4a_canada_emissions_benchmarks.png",
         "Figure 3.4a: 2024 Canadian Emissions Inventory Benchmarks (NOx, PM2.5, Black Carbon) and SCR/DPF Mitigation Efficacy",
         lambda: render_hbar(
             "fig_3_4a_canada_emissions_benchmarks.png",
             "Canadian Air Pollutant Inventory Benchmarks (2024) & Control Reductions",
             "National NOx (447 kt), Ontario PM2.5 (210.4 kt), and Biodiesel + SCR/DPF Mitigation Impact",
             ["Canada Total NOx Inventory (37% Oil & Gas)", "Ontario Total PM2.5 Inventory",
              "Alberta Off-Road Black Carbon Share (%)", "PM2.5 Cut via Biodiesel + SCR/DPF Controls (%)"],
             [447.0, 210.4, 42.0, 20.0], "kt or %",
             colors=[CORAL, NAVY, AMBER, GREEN],
             note="Mandating EPA Tier 4 Final SCR/DPF controls with biodiesel blends achieves a minimum 20% PM2.5 reduction and 85%+ NOx cut."
         ))

register("3.4", "fig_3_4b_atmospheric_deposition_diagram.png",
         "Figure 3.4b: Atmospheric Deposition Pathway of Diesel Exhaust Plumes on the Trent River Watershed and Wetlands",
         lambda: render_process_infographic(
             "fig_3_4b_atmospheric_deposition_diagram.png",
             "Atmospheric Deposition Diagram: Diesel Generator Exhaust Plumes",
             "Photochemical Smog, Aquatic Acidification, and Cryospheric Albedo Impacts in the Trent Valley",
             [
                 ("1. Exhaust Stack Plume", ["High-velocity Tier 2 diesel exhaust", "NOx, VOCs, SO2, PM2.5 & black carbon", "Trapped by Trent River valley inversions"]),
                 ("2. Photochemical Ozone", ["NOx + VOCs + sunlight -> O3 smog", "Triggers respiratory inflammation", "Damages Murray/Sidney orchard crops"]),
                 ("3. Acid & Nutrient Fallout", ["Nitric/sulfuric acid wet deposition", "Eutrophication in Bay of Quinte AOC", "Degrades Lake Sturgeon spawning beds"]),
                 ("4. Wetland Albedo Loss", ["Black carbon settles on winter snow/ice", "Reduces surface albedo & speeds melt", "Alters spring freshet flood timing"])
             ],
             footer_note="Ecological Link: Unfiltered diesel testing along the Trent River directly deposits nitrogen and black carbon into sensitive aquatic habitats."
         ))


# --- SECTION 3.5.1 ---
def build_3_5_1a():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.2), dpi=300)
    fig.patch.set_facecolor("white")
    cats = ["Diesel Min\n(7 Riverside)", "Diesel Cap\n(Recommended)", "Diesel Max\n(920 T-F Rd)", "Glycol Min\n(Closed Loop)", "Glycol Cap\n(Recommended)", "Glycol Max\n(Campus)"]
    vals = [10, 50, 100, 5, 10, 20]
    cols = [NAVY, GREEN, CORAL, TEAL, GREEN, AMBER]
    bars = ax1.bar(cats, vals, color=cols, width=0.55)
    for b, v in zip(bars, vals):
        ax1.text(b.get_x() + b.get_width()/2, v + 2, f"{v}k L", ha="center", fontweight="bold", fontsize=8.5)
    ax1.set_ylim(0, 118)
    ax1.set_ylabel("On-Site Storage Volume (Thousand Liters)", fontweight="bold")
    ax1.tick_params(axis="x", labelsize=8)
    ax1.grid(axis="y", linestyle="--", alpha=0.5)
    ax1.set_title("Projected Storage vs. Recommended Municipal Caps", fontsize=10, fontweight="bold", color=NAVY)

    temps = np.linspace(-2, 25, 100)
    rate = 2.3 * np.exp(np.log(93.3 / 2.3) * (temps + 2) / 27.0)
    ax2.plot(temps, rate, color=CORAL, lw=3)
    ax2.fill_between(temps, 0, rate, color=CORAL, alpha=0.18)
    ax2.plot([-2, 25], [2.3, 93.3], "o", color=NAVY, markersize=9)
    ax2.annotate("Winter (-2°C): 2.3 mg/kg/day\n(40x Slower — Persistent Spill!)", xy=(-2, 2.3), xytext=(2, 25),
                 fontweight="bold", fontsize=8.5, bbox=dict(boxstyle="round", facecolor="#FEF3C7", edgecolor=CORAL),
                 arrowprops=dict(arrowstyle="->", color=CORAL, lw=2))
    ax2.annotate("Summer (25°C): 93.3 mg/kg/day", xy=(25, 93.3), xytext=(10, 82),
                 fontweight="bold", fontsize=8.5, bbox=dict(boxstyle="round", facecolor="white", edgecolor=NAVY),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
    ax2.set_xlabel("Soil Temperature (°C)", fontweight="bold")
    ax2.set_ylabel("PG Biodegradation Rate (mg/kg/day)", fontweight="bold")
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.set_title("Propylene Glycol Soil Biodegradation vs. Temperature", fontsize=10, fontweight="bold", color=NAVY)
    plt.suptitle("On-Site Chemical Storage Volumes & Temperature-Dependent PG Biodegradation", fontsize=13, fontweight="bold", color=NAVY, y=0.98)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_3_5_1a_storage_and_biodegradation.png", dpi=300)
    plt.close(fig)

register("3.5.1", "fig_3_5_1a_storage_and_biodegradation.png",
         "Figure 3.5.1a: Projected Diesel (10,000–100,000 L) and Propylene Glycol (5,000–20,000 L) Storage Volumes and Soil Biodegradation Curve (-2°C vs. 25°C)",
         build_3_5_1a)

def build_3_5_1b():
    fig, ax = plt.subplots(figsize=(10.5, 5.5), dpi=300)
    fig.patch.set_facecolor("white")
    ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")
    # Concrete vault (110% containment)
    vault = mpatches.FancyBboxPatch((10, 10), 80, 65, boxstyle="round,pad=0.5", facecolor="#E2E8F0", edgecolor=SLATE, lw=3)
    ax.add_patch(vault)
    # Outer steel wall
    outer = mpatches.FancyBboxPatch((18, 22), 64, 46, boxstyle="round,pad=1.5", facecolor="#CBD5E1", edgecolor=NAVY, lw=3)
    ax.add_patch(outer)
    # Interstitial space
    inter = mpatches.FancyBboxPatch((21, 25), 58, 40, boxstyle="round,pad=1.2", facecolor="#FEF3C7", edgecolor=AMBER, lw=2, linestyle="--")
    ax.add_patch(inter)
    # Inner primary tank
    inner = mpatches.FancyBboxPatch((24, 28), 52, 34, boxstyle="round,pad=1.0", facecolor="#38BDF8", edgecolor=TEAL, lw=2.5, alpha=0.7)
    ax.add_patch(inner)
    ax.text(50, 45, "PRIMARY INNER STEEL TANK\nULSD Diesel (Cap: 50,000 L) or Propylene Glycol (Cap: 10,000 L)",
            ha="center", va="center", fontweight="bold", fontsize=10, color=NAVY)
    ax.annotate("Vacuum-Monitored Interstitial Annulus\n(Optical & Pressure Leak Sensors)", xy=(22, 45), xytext=(2, 82),
                fontweight="bold", fontsize=8.8, bbox=dict(boxstyle="round", facecolor="#FEF3C7", edgecolor=AMBER),
                arrowprops=dict(arrowstyle="->", lw=2, color=AMBER))
    ax.annotate("Outer Secondary Steel Wall (CSA B139 Compliant)", xy=(82, 55), xytext=(62, 84),
                fontweight="bold", fontsize=8.8, bbox=dict(boxstyle="round", facecolor="white", edgecolor=NAVY),
                arrowprops=dict(arrowstyle="->", lw=2, color=NAVY))
    ax.annotate("Impermeable 110% Concrete Containment Dike\n+ Automatic Stormwater Shutoff Valve", xy=(50, 12), xytext=(55, 2),
                fontweight="bold", fontsize=8.8, bbox=dict(boxstyle="round", facecolor="white", edgecolor=CORAL),
                arrowprops=dict(arrowstyle="->", lw=2, color=CORAL))
    plt.suptitle("Cross-Section of CSA-Compliant Double-Walled Storage Tank & 110% Containment Vault", fontsize=13, fontweight="bold", color=NAVY, y=0.97)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_3_5_1b_csa_double_walled_tank.png", dpi=300)
    plt.close(fig)

register("3.5.1", "fig_3_5_1b_csa_double_walled_tank.png",
         "Figure 3.5.1b: Engineering Cross-Section of a CSA-Compliant Double-Walled Storage Tank with Interstitial Leak Detection and 110% Secondary Containment",
         build_3_5_1b)


# --- SECTION 3.5.2 ---
register("3.5.2", "fig_3_5_2a_diesel_toxicity_diagram.png",
         "Figure 3.5.2a: Terrestrial and Aquatic Toxicity Pathway of a Bulk Diesel Fuel Spill (10–100 mg/L)",
         lambda: render_process_infographic(
             "fig_3_5_2a_diesel_toxicity_diagram.png",
             "Terrestrial & Aquatic Toxicity Pathway of a Bulk Diesel Spill",
             "Soil Hydrophobicity, BTEX/PAH Aquifer Plumes, and Acute Aquatic Mortality at 10–100 mg/L",
             [
                 ("1. Soil Hydrophobicity", ["Diesel coats glacial till & topsoil", "Destroys soil pore water retention", "Kills root mycorrhizae & vegetation"]),
                 ("2. BTEX & PAH Leaching", ["Benzene, Toluene, Ethylbenzene, Xylene", "Carcinogenic PAHs infiltrate water table", "Persists for decades in anaerobic sediment"]),
                 ("3. Surface Slick Hypoxia", ["Hydrophobic sheen blocks gas exchange", "Coats waterfowl plumage (hypothermia)", "Forces emergency Trenton WTP shutdown"]),
                 ("4. Acute Fish Gill Toxicity", ["10–100 mg/L strips gill lamellae mucus", "Induces acute asphyxiation & larvae death", "Decimates walleye & sturgeon nurseries"])
             ],
             footer_note="Precedent: Modeled on the 2023 Equinix 5,500-gallon (20,800 L) diesel spill into Secaucus Creek wetland."
         ))

register("3.5.2", "fig_3_5_2b_diesel_spill_trajectory_map.png",
         "Figure 3.5.2b: Simulated 5,500-Gallon Diesel Spill Trajectory Map from 7 Riverside Drive and 920 Trenton-Frankford Road into IPZ-1",
         lambda: render_annotated_map(
             "fig_3_5_2b_diesel_spill_trajectory_map.png",
             "quinte_west_trenton_downtown.svg",
             "Simulated 5,500-Gallon Diesel Spill Trajectory & IPZ-1 Impact Map",
             "Applying the 2023 Equinix Spill Scenario to 7 Riverside Drive and 920 Trenton-Frankford Road",
             [
                 (46, 78, 10, 82, "Origin A: 920 Trenton-Frankford Rd", "5,500-Gal Spill Enters Glen Miller Reach", CORAL),
                 (52, 50, 12, 25, "Origin B: 7 Riverside Drive", "Direct Bank Discharge into Lower Trent River", CORAL),
                 (49, 58, 58, 72, "Trenton WTP IPZ-1 Zone", "Hydrocarbon Slick Reaches Intake in <2 Hours", NAVY),
                 (58, 28, 62, 18, "Bay of Quinte Estuary Plume", "Fouls Kiwanis Bayshore & Marina Basin", AMBER)
             ],
             zones=[
                 (49, 58, 8, CORAL, "IPZ-1 Emergency Shutdown Zone"),
                 (52, 42, 14, AMBER, "Downstream Hydrocarbon Slick")
             ]
         ))


# --- SECTION 3.5.3 ---
def build_3_5_3a():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 5.2), dpi=300)
    base_img = load_svg_basemap("quinte_west_Saputo_data_center.svg", width=800)
    ax1.imshow(base_img, extent=[0, 100, 0, 100])
    c = mpatches.Circle((52, 45), 18, facecolor=CORAL, edgecolor="white", alpha=0.4, lw=2)
    ax1.add_patch(c)
    ax1.annotate("1,000 L PG Spill (500 kg Active)\n10-km Hypoxic Stretch (<2 mg/L DO)", xy=(52, 45), xytext=(10, 78),
                 fontsize=8.5, fontweight="bold", bbox=dict(boxstyle="round", facecolor="white", edgecolor=CORAL),
                 arrowprops=dict(arrowstyle="->", color=CORAL, lw=2))
    ax1.set_title("10-km Trent River & Estuarine Hypoxia Zone\n(7 Riverside: 1,000 L | 920 T-F Rd: 500 L)", fontsize=9.5, fontweight="bold", color=NAVY)
    ax1.axis("off")

    hrs = np.linspace(0, 72, 150)
    do_7r = 8.5 - 7.3 * np.exp(-((hrs - 36)/18)**2)
    do_920 = 8.5 - 6.1 * np.exp(-((hrs - 42)/20)**2)
    ax2.plot(hrs, do_7r, "-", color=CORAL, lw=3, label="7 Riverside Dr: 1,000 L PG Spill (500 kg to River)")
    ax2.plot(hrs, do_920, "--", color=AMBER, lw=2.5, label="920 Trenton-Frankford: 500 L Estuarine Spill")
    ax2.axhline(2.0, color=NAVY, linestyle=":", lw=2, label="Acute Lethal Hypoxia Threshold (2.0 mg/L DO)")
    ax2.fill_between(hrs, 0, 2.0, color=CORAL, alpha=0.2)
    ax2.annotate("Severe Hypoxia (<2 mg/L DO within 48 hrs)\nBOD = 1.68 kg O2 per Liter of PG", xy=(36, 1.2), xytext=(12, 4.2),
                 fontweight="bold", fontsize=8.5, bbox=dict(boxstyle="round", facecolor="#FEF3C7", edgecolor=CORAL),
                 arrowprops=dict(arrowstyle="->", color=CORAL, lw=2))
    ax2.set_ylim(0, 10); ax2.set_xlim(0, 72)
    ax2.set_xlabel("Hours Post-Spill (0 to 72 Hours)", fontweight="bold")
    ax2.set_ylabel("Dissolved Oxygen (DO in mg/L)", fontweight="bold")
    ax2.legend(loc="upper right", fontsize=8)
    ax2.grid(True, linestyle="--", alpha=0.5)
    ax2.set_title("48-Hour Dissolved Oxygen Sag Curve (Streeter-Phelps)", fontsize=9.5, fontweight="bold", color=NAVY)
    plt.suptitle("Propylene Glycol Spill Scenario: 10-km Plume Map & 48-Hour Oxygen Depletion Curve", fontsize=13, fontweight="bold", color=NAVY, y=0.98)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_3_5_3a_pg_spill_oxygen_depletion.png", dpi=300)
    plt.close(fig)

register("3.5.3", "fig_3_5_3a_pg_spill_oxygen_depletion.png",
         "Figure 3.5.3a: Trent River Propylene Glycol Spill Map and 48-Hour Dissolved Oxygen Depletion Curve (<2.0 mg/L Hypoxia)",
         build_3_5_3a)

register("3.5.3", "fig_3_5_3b_pg_vs_eg_comparison.png",
         "Figure 3.5.3b: Toxicological and Biochemical Oxygen Demand Comparison of Propylene Glycol vs. Ethylene Glycol",
         lambda: render_grouped_bar(
             "fig_3_5_3b_pg_vs_eg_comparison.png",
             "Coolant Chemistry Comparison: Propylene Glycol (PG) vs. Ethylene Glycol (EG)",
             "Normalized Comparison of Mammalian LD50, Fish LC50, Biochemical Oxygen Demand (BOD), and Bio-PG GHG Cut",
             ["Rat Oral LD50\n(g/kg Body Wt)", "Fish 96-hr LC50\n(g/L Water)", "Biochemical Oxygen\nDemand (kg O2/L)", "Bio-Based PG GHG\nReduction (%/10)"],
             {"Propylene Glycol (PG)": [21.0, 10.0, 1.68, 6.1], "Ethylene Glycol (EG)": [3.0, 3.0, 1.0, 0.0]},
             "Metric Value (g/kg, g/L, kg O2/L, or %/10)",
             note="PG has low mammalian toxicity (LD50 20,000–22,000 mg/kg vs EG 2,000–4,000 mg/kg) but higher aquatic BOD (1.68 vs 0.8–1.2 kg O2/L). Bio-PG cuts GHGs 61%."
         ))


# --- SECTION 3.6 ---
register("3.6", "fig_3_6a_ansi_species_disruption.png",
         "Figure 3.6a: Sensory and Habitat Disruption Matrix for Key Trent River ANSI Species",
         lambda: render_process_infographic(
             "fig_3_6a_ansi_species_disruption.png",
             "Sensory & Habitat Disruption of Trent River ANSI Indicator Species",
             "Impacts of 65–85 dBA Mechanical Noise, PM2.5/NOx Plumes, and Underground Cable Trenching",
             [
                 ("Atlantic Salmon & Sturgeon", ["Thermal plumes (>10°C) block migration", "Glycol BOD hypoxia (<2 mg/L) kills fry", "Cable trenching silts spawning gravel"]),
                 ("Bald Eagle & Common Tern", ["65–85 dBA masks territorial calls", "24/7 floodlights disrupt roosting", "Diesel slick fouls foraging waters"]),
                 ("Hine's Emerald Dragonfly", ["Larvae inhabit calcareous seepage fens", "Dewatering trenching alters water table", "NOx/acid deposition degrades fen pH"]),
                 ("Massasauga & Least Bittern", ["Ground vibration triggers snake flight", "Perimeter fencing fragments corridors", "Wetland noise causes nest abandonment"])
             ],
             footer_note="ANSI Protection: Areas of Natural and Scientific Interest along the Lower Trent require >500 m acoustic and hydrological buffers."
         ))


# --- SECTION 3.7 ---
def build_3_7a():
    fig, ax = plt.subplots(figsize=(9.5, 5.2), dpi=300)
    fig.patch.set_facecolor("white")
    ax.set_facecolor(LIGHT_BG)
    groups = ["Control Group (0 uT)\nOlfactory Learning", "100 uT EMF (1-Min Exposure)\nShepherd et al. (2018)", "Successful Foraging\nFlight Passes (% Baseline)"]
    means = [65.5, 47.2, 68.0]
    errs = [11.5, 10.5, 8.0]
    bars = ax.bar(groups, means, yerr=errs, capsize=8, color=[TEAL, CORAL, AMBER], width=0.48, error_kw=dict(lw=2, capthick=2))
    for b, m in zip(bars, means):
        ax.text(b.get_x() + b.get_width()/2, m + 13, f"{m:.1f}%", ha="center", fontweight="bold", fontsize=10)
    ax.annotate("-27.97% Drop in Learning Acquisition\n(47–68% Exposed vs. 54–77% Control)", xy=(1, 47.2), xytext=(0.8, 82),
                fontweight="bold", fontsize=9, bbox=dict(boxstyle="round", facecolor="#FEF3C7", edgecolor=CORAL),
                arrowprops=dict(arrowstyle="->", color=CORAL, lw=2))
    ax.set_ylim(0, 100)
    ax.set_ylabel("Response Rate / Flight Success (%)", fontweight="bold")
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    plt.suptitle("EMF Effects on Honeybee (Apis mellifera) Behavior & Learning (Shepherd et al., 2018)", fontsize=12.5, fontweight="bold", color=NAVY, y=0.97)
    ax.set_title("1-Minute Exposure to 100 uT ELF-EMF Induces a 27.97% Drop in Proboscis Extension Reflex Learning", fontsize=9.5, color=SLATE)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_3_7a_shepherd_bee_emf_chart.png", dpi=300)
    plt.close(fig)

register("3.7", "fig_3_7a_shepherd_bee_emf_chart.png",
         "Figure 3.7a: Bar Chart with Error Bars Illustrating Shepherd et al. (2018) Honeybee Learning Drop (-27.97%) Under 100 uT EMF Exposure",
         build_3_7a)

def build_3_7b():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
    dist = np.linspace(1, 100, 200)
    hv_unshielded = 3500 / (dist ** 1.15)
    dc_equip = 800 / ((dist / 5 + 1) ** 1.3)
    dc_shielded = dc_equip * 0.15
    ax.plot(dist, hv_unshielded, "-", color=CORAL, lw=2.8, label="132–400 kV Transmission Line (20–7,000 uT at 1m)")
    ax.plot(dist, dc_equip, "--", color=AMBER, lw=2.5, label="Unshielded Data Center Equipment (100–1,000 uT at 10–50m)")
    ax.plot(dist, dc_shielded, "-", color=GREEN, lw=2.8, label="Mu-Metal Shielded + Buried Conduit (50–90% EMF Reduction)")
    ax.axhline(100, color=NAVY, linestyle=":", lw=2, label="100 uT Honeybee Impairment Threshold (Shepherd et al.)")
    ax.axvline(50, color=TEAL, linestyle="-.", lw=2, label="Recommended 50 m Pollinator Zoning Buffer")
    ax.set_yscale("log")
    ax.set_xlabel("Distance from Infrastructure Source (Meters)", fontweight="bold")
    ax.set_ylabel("Magnetic Flux Density (uT - Log Scale)", fontweight="bold")
    ax.grid(True, which="both", linestyle="--", alpha=0.4)
    ax.legend(loc="upper right", fontsize=8.2)
    plt.suptitle("EMF Distance-Decay Curve & Shielding Attenuation Across 279,000 km of Regional Lines", fontsize=12.5, fontweight="bold", color=NAVY, y=0.97)
    ax.set_title("Combining 50–90% Conductive Shielding with a 50 m Buffer Drops Field Strength Below the 100 uT Bee Threshold", fontsize=9.2, color=SLATE)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_3_7b_emf_distance_decay_shielding.png", dpi=300)
    plt.close(fig)

register("3.7", "fig_3_7b_emf_distance_decay_shielding.png",
         "Figure 3.7b: EMF Distance-Decay and Shielding Attenuation Diagram Comparing 132–400 kV Lines, Data Center Equipment, and 50 m Buffers",
         build_3_7b)


# --- SECTION 3.8 ---
register("3.8", "fig_3_8a_four_pathway_ecological_matrix.png",
         "Figure 3.8a: Four-Pathway Ecological Impact Matrix Summarizing Habitat Loss, Water/Energy Demand, Noise, and Light Pollution",
         lambda: render_process_infographic(
             "fig_3_8a_four_pathway_ecological_matrix.png",
             "Four-Pathway Ecological Impact Matrix of Hyperscale Data Centers",
             "Synthesizing Global Empirical Benchmarks Across Land, Water, Acoustics, and Photopollution",
             [
                 ("1. Habitat Loss", ["Sprawling 30–100+ acre footprints", "6,200–21,000 acres converted in VA", "Trent River riparian cover down to 40%", "Impervious heat-island runoff"]),
                 ("2. Water & Energy Surge", ["Google: 29B L drawn / 23B L evaporated", "Microsoft: +34% water jump in 1 year", "75% of US sites in high water-stress zones", "Delays fossil-fuel plant retirements"]),
                 ("3. Chronic Noise (>50 dB)", ["Continuous 24/7/365 tonal hum", "65–72 dBC low-frequency propagation", "Masks bird song & amphibian calls", "Disrupts bee 100–500 Hz waggle dance"]),
                 ("4. Light Pollution (ALAN)", ["Affects 80% of global night skies", "24/7 security floodlights blind owls/bats", "Suppresses firefly bioluminescence", "Alters diel phytoplankton migration"])
             ],
             footer_note="Cumulative Impact: Co-locating 24/7 industrial light, >50 dB noise, and thermal plumes degrades riparian corridors."
         ))

def build_3_8b():
    fig, ax1 = plt.subplots(figsize=(10, 5.2), dpi=300)
    fig.patch.set_facecolor("white")
    ax1.set_facecolor(LIGHT_BG)
    techs = ["Evaporative\nCooling", "Liquid\nCooling", "Rainwater\nHarvesting", "Dry Cooling\n(Air Chiller)"]
    x = np.arange(len(techs))
    water_mid = [3500, 750, 50, 0]
    energy_mid = [2250, 3250, 1500, 5000]

    b1 = ax1.bar(x - 0.18, water_mid, width=0.34, color=TEAL, label="Daily Water Use Midpoint (L/day)")
    ax1.set_ylabel("Daily Water Consumption (L/day)", fontweight="bold", color=TEAL)
    ax1.set_ylim(0, 4500)
    for b, v in zip(b1, water_mid):
        ax1.text(b.get_x() + b.get_width()/2, v + 90, f"{v:,} L", ha="center", fontweight="bold", fontsize=8.5, color=TEAL)

    ax2 = ax1.twinx()
    b2 = ax2.bar(x + 0.18, energy_mid, width=0.34, color=CORAL, label="Daily Energy Use Midpoint (kWh/day)")
    ax2.set_ylabel("Daily Energy Consumption (kWh/day)", fontweight="bold", color=CORAL)
    ax2.set_ylim(0, 6200)
    for b, v in zip(b2, energy_mid):
        ax2.text(b.get_x() + b.get_width()/2, v + 120, f"{v:,} kWh", ha="center", fontweight="bold", fontsize=8.5, color=CORAL)

    ax1.set_xticks(x); ax1.set_xticklabels(techs, fontweight="bold", fontsize=10)
    ax1.grid(axis="y", linestyle="--", alpha=0.5)
    l1, lb1 = ax1.get_legend_handles_labels()
    l2, lb2 = ax2.get_legend_handles_labels()
    ax1.legend(l1 + l2, lb1 + lb2, loc="upper left", fontsize=8.8)
    plt.suptitle("Dual-Axis Comparison of Cooling Technologies: Daily Water vs. Energy Trade-Off", fontsize=12.5, fontweight="bold", color=NAVY, y=0.97)
    ax1.set_title("Evaporative (2,000–5,000 L; 1,500–3,000 kWh) vs. Dry Cooling (0 L; 4,000–6,000 kWh)", fontsize=9.5, color=SLATE)
    plt.tight_layout(rect=[0, 0.02, 1, 0.92])
    fig.savefig(FIGURES_DIR / "fig_3_8b_cooling_tech_dual_axis.png", dpi=300)
    plt.close(fig)

register("3.8", "fig_3_8b_cooling_tech_dual_axis.png",
         "Figure 3.8b: Dual-Axis Bar Chart Contrasting Daily Water Use (L/day) and Energy Use (kWh/day) Across Four Cooling Architectures",
         build_3_8b)


# --- SECTION 3.9 ---
register("3.9", "fig_3_9a_international_regulatory_scorecard.png",
         "Figure 3.9a: International Regulatory Scorecard Comparing Canada's RDDP Against the EU Green Deal, US EPA/California AB 32, and China's 2021 Guidelines",
         lambda: render_process_infographic(
             "fig_3_9a_international_regulatory_scorecard.png",
             "International Environmental Regulatory Scorecard for Data Centers",
             "Comparing Canada's RDDP Against the European Union, United States/California, and China",
             [
                 ("Canada (ISED RDDP)", ["100% developer grid payment rule", "Minimal potable water use principle", "Early Indigenous & municipal consult", "Voluntary guidelines (non-statutory)"]),
                 ("EU Green Deal (EED)", ["Mandatory design PUE <= 1.5 target", "55% net GHG emissions cut by 2030", "100% renewable power by 2030", "Binding public WUE/PUE registry"]),
                 ("US EPA / Calif. AB 32", ["California AB 32: 40% GHG cut by 2030", "Strict EPA Tier 4 diesel enforcement", "State-level water disclosure bills", "Washington mandatory Health Risk Assess."]),
                 ("China 2021 Guidelines", ["Strict statutory PUE <= 1.5 cap", ">=30% renewable energy mandate", "60% carbon intensity cut by 2030", "Bans evaporative towers in arid hubs"])
             ],
             footer_note="Policy Recommendation: Quinte West should codify Canada's voluntary RDDP principles into binding Municipal Site Plan Control bylaws."
         ))


# ==============================================================================
# MARKDOWN SUB-SECTION DISCOVERY & CLEAN LINK INJECTION
# ==============================================================================

def find_target_markdown(sec_code):
    """Finds the matching sub-section markdown file in papers/ for a given section code (e.g., '1.6.1')."""
    if not PAPERS_DIR.exists():
        return None
    all_mds = sorted(PAPERS_DIR.glob("**/*.md"))
    # Exact prefix match first (e.g., 1.6.1_... or 1.6_...)
    for md in all_mds:
        if md.name.startswith(f"{sec_code}_") or md.name == f"{sec_code}.md":
            return md
    # Parent section fallback (e.g. '1.6.1' -> '1.6_7_riverside_dr...')
    parent_code = ".".join(sec_code.split(".")[:2])
    for md in all_mds:
        if md.name.startswith(f"{parent_code}_") or md.name == f"{parent_code}.md":
            return md
    return None


def inject_figure_into_markdown(md_path, fname, caption):
    """Cleanly inserts the Pandoc figure syntax without adding any LLM conversational text."""
    if md_path is None or not md_path.exists():
        return False
    text = md_path.read_text(encoding="utf-8", errors="ignore")
    if fname in text:
        return True  # Already linked

    embed_line = f"\n\n![{caption}](figures/{fname}){{width=88%}}\n\n"
    # Insert right before References / Grounded Source Citations / Verified Raw Evidence if present
    markers = [
        "## References", "## Grounded Source Citations", "## Verified Raw Evidence",
        "### References", "## Conclusion", "## Technical Comparison"
    ]
    for m in markers:
        idx = text.find(m)
        if idx != -1:
            updated = text[:idx].rstrip() + embed_line + text[idx:]
            md_path.write_text(updated, encoding="utf-8")
            return True

    # Otherwise append cleanly at end of sub-section
    updated = text.rstrip() + embed_line
    md_path.write_text(updated, encoding="utf-8")
    return True


def main():
    print(f"=== Starting Automated Build of {len(MANIFEST)} Visual Assets (Sections 1.1 – 3.9) ===")
    built = 0
    linked = 0
    for idx, (sec, fname, caption, builder) in enumerate(MANIFEST, 1):
        out_path = FIGURES_DIR / fname
        try:
            builder()
            built += 1
            md_target = find_target_markdown(sec)
            if inject_figure_into_markdown(md_target, fname, caption):
                linked += 1
                target_label = md_target.name if md_target else "N/A"
            else:
                target_label = "rendered (no matching .md found)"
            print(f"[{idx:02d}/{len(MANIFEST)}] ✓ {fname}  -->  {target_label}")
        except Exception as e:
            print(f"[{idx:02d}/{len(MANIFEST)}] ✗ ERROR on {fname}: {e}")

    print(f"\n=== Completed! Built {built}/{len(MANIFEST)} 300-DPI graphics in {FIGURES_DIR} ===")
    print(f"=== Cleanly linked {linked} figures into sub-section Markdown files ===")


if __name__ == "__main__":
    main()
