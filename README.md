# AI & Society — ABM Repro Package

Code and materials for a minimal agent-based model (ABM) of the joint effect of **E** (platform filtering) and **R** (institutional response) on harmful-content spread.

---

## Quick start

### 1) Create & activate venv

    python -m venv .venv

    # Windows:
    .\.venv\Scripts\activate
    # macOS/Linux:
    source .venv/bin/activate

### 2) Install deps

    pip install -r requirements.txt

### 3) Reproduce core figures

    python -m scripts.repro

The script:
- ensures `data/charter_countries.csv` exists (creates a deterministic demo if missing);
- writes **Fig. 1–2** and **App. A, Fig. S7** to `figures/`.

---

## Layout

    abm/
      abm_core.py
    scripts/
      make_charter_countries.py
      repro.py
    notebooks/
      figures/
        ai_society_figures.ipynb
    figures/                 # generated here by the pipeline
    data/
      cg_hr_data.csv         # (optional)
      charter_countries.csv  # (auto-created if missing)

---

## What the figures show

- **Fig. 1** — Final prevalence across **E,R** (heatmap).
- **Fig.  2** — Prevalence dynamics for selected (E,R).
- **App. A, Fig. S7** — Robustness to `seed_frac` and RNG seed across (E,R); CSV summary saved as `s7_robustness_summary.csv`.

---

## Extended appendices

See **[`appendix/`](./appendix/)**:
- F — Operationalizing **E\*** (energy metric)
- G — Validation plan for indices
- H — Ethics & anthropology
- I — Trust & safety protocols

---

## Citing this repository

> Replace the DOI after you mint the new Zenodo release.

    @misc{kolomiets_abm_er_2025,
      title        = {Agent-based modeling of platform filtering (E) and institutional response (R)},
      author       = {Kolomiets, Alexander},
      year         = {2025},
      howpublished = {Open code and data},
      doi          = {10.5281/zenodo.TBD},
      url          = {https://doi.org/10.5281/zenodo.TBD}
    }
