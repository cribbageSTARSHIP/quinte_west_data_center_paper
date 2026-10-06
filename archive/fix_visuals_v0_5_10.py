#!/usr/bin/env python3
import re
import textwrap
from pathlib import Path

script_path = Path("/workspace/auto_build_visuals.py") if Path("/workspace/auto_build_visuals.py").exists() else Path("/home/prizm/ai-stack/research-paper/auto_build_visuals.py")
code = script_path.read_text(encoding="utf-8")

# 1. Disable matplotlib mathtext parsing of '$' signs so "$M" never turns into italics
if 'plt.rcParams["text.parse_math"] = False' not in code:
    code = code.replace(
        'plt.rcParams["axes.linewidth"] = 0.8',
        'plt.rcParams["axes.linewidth"] = 0.8\nplt.rcParams["text.parse_math"] = False'
    )

# 2. Replace helper functions with wrapped, non-clipping, negative-bar-aware versions
new_helpers = '''def render_hbar(filename, title, subtitle, categories, values, unit, colors=None, note=None):
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
'''

start_marker = "def render_hbar("
end_marker = "def render_annotated_map("
code = code[:code.index(start_marker)] + new_helpers + "\n\n" + code[code.index(end_marker):]

# 3. Fix render_photo_panel so offline fallback never duplicates headings/captions
old_photo_fn = code[code.index("def render_photo_panel("):code.index("# ==============================================================================\n# MASTER 60-GRAPHIC MANIFEST")]
new_photo_fn = '''def render_photo_panel(filename, title, subtitle, items):
    """Renders structured ecological/heritage technical profile cards with clean wrapped text."""
    stages = []
    for query, heading, caption in items:
        stages.append((heading, [caption, f" Classification: {query.title()}", "Jurisdiction: Lower Trent / Bay of Quinte Watershed"]))
    render_process_infographic(filename, title, subtitle, stages,
                               footer_note="Field Reference: Protected ecological, hydrological, and heritage receptors within the City of Quinte West.")
'''
code = code.replace(old_photo_fn, new_photo_fn + "\n\n")

# 4. Fix build_2_4b overlapping X-axis labels
code = code.replace(
    'cats = ["Distributed Siting\\n(Low Depletion)", "Concentrated Cluster\\n(Moderate Draw)", "Concentrated Drought\\nPeak (Max Draw)"]',
    'cats = ["Distributed\\nSiting", "Concentrated\\nCluster", "Concentrated\\nDrought Peak"]'
)

script_path.write_text(code, encoding="utf-8")
print("✓ Updated auto_build_visuals.py with wrapped text cards, negative bar support, and clean layouts.")
