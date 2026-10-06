# Wiki Schema

## Domain
Environmental, socioeconomic, infrastructure, and public health impacts of hyperscale AI data centers across Quinte West (Ontario), Canada, the United States, and global regions.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `evaporative-cooling-loss.md`)
- Every wiki page starts with YAML frontmatter (`title`, `type`, `created`, `updated`, `sources`, `tags`)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- Every quantitative statistic, quote, or regulatory claim must include an inline provenance citation: `^[Source: filename, Page X]` or `^[Source: Title | URL]`
- Never modify files inside `raw/`
- Log every operation to `log.md` and keep `index.md` updated

## 8 Core Research Pillars (Tags & Concept Groupings)
1. `01-power-grid`: Megawatt/gigawatt demand, IESO constraints, substation capacity, peaker plants, ratepayer cost-shifting.
2. `02-water-ecology`: Evaporative cooling loss (MGD/litres), municipal water drawdown, aquifer depletion, thermal discharge.
3. `03-pollutants-spills`: Backup diesel generator emissions (NOx, PM2.5, EPA Tier 2 vs Tier 4), PFAS, glycol/fuel spills.
4. `04-acoustics-dba-dbc`: Low-frequency hum (<100 Hz), dBC vs dBA measurement differentials, chiller fan noise, municipal ordinances.
5. `05-human-health`: Sleep disturbance, cardiovascular stress, respiratory/asthma impacts from particulate plumes.
6. `06-municipal-tax-revenue`: Tax abatements, PILOT agreements, sales tax exemptions vs municipal infrastructure costs.
7. `07-labor-spinoffs`: Temporary construction jobs vs permanent staffing, subsidy-per-job ratios, automation effects.
8. `08-hazards-emergency`: BESS/Lithium-ion thermal runaway, toxic HF gas plumes, rural/municipal fire department readiness.

## Folder Organization
- `raw/papers/` — Pre-extracted peer-reviewed PDF ledgers (immutable)
- `raw/articles/` — Regional web-mined ledgers (immutable)
- `entities/` — Specific facilities, municipalities (e.g., `quinte-west.md`), utilities (`ieso.md`), and corporations
- `concepts/` — Technical mechanisms and impact categories across the 8 pillars
- `comparisons/` — Cross-regional tables and conflicting study syntheses
- `queries/` — Saved research syntheses and drafted paper sections

## Strict Anti-Hallucination & Provenance Rules
- NEVER invent, estimate, or extrapolate statistics, facility counts, or megawatt figures.
- Only include facts explicitly stated in the raw source text you have read in the current turn.
- Every single claim MUST have an exact inline citation (`^[Source: filename, Page X]` or `^[Source: Title | URL]`).
- If a requested entity or region is not present in the raw text you read, DO NOT create a page for it; report that no source data was found.
- When using `write_file` or `patch`, write clean Markdown only—never include line numbers or header banners from `read_file`.
