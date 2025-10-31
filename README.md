# AI & Society — ABM Repro Package

[![DOI](https://zenodo.org/badge/994276536.svg)](https://doi.org/10.5281/zenodo.17390051)

Code and materials for a minimal agent-based model (ABM) of the joint effect of **E** (platform filtering) and **R** (institutional response) on harmful-content spread.

## Quick start

```bash
# 1) create & activate venv
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

# 2) deps
pip install -r requirements.txt

# 3) reproduce core figures
python -m scripts.repro
The script:

ensures data/charter_countries.csv exists (creates a deterministic demo if missing);

writes Fig.1–2 and App. A, Fig. S7 to figures/.

Layout
abm/
  abm_core.py
scripts/
  make_charter_countries.py
  repro.py
notebooks/
  figures/
    ai_society_figures.ipynb
figures/
  (generated here)
data/
  cg_hr_data.csv (optional)
  charter_countries.csv (auto-created)
What the figures show

Fig. 1 — Final prevalence across E,R (heatmap)

Fig. 2 — Prevalence dynamics for selected (E,R)

App. A, Fig. S7 — Robustness to seed_frac∈{0.5%,1%,2%} and rng_seed∈{1,11,21}; see s7_robustness_summary.csv

Technical appendix

See preprint_technical_appendix_2025-10-31.md (repro steps, artifacts, mapping to manuscript).

Licenses

Code: Apache-2.0
Text & figures: CC BY 4.0
Data: CC BY 4.0

Citation

If you use this repository, please cite the archived release:
@misc{kolomiets_abm_er_2025,
  title        = {Agent-based modeling of platform filtering (E) and institutional response (R)},
  author       = {Kolomiets, Alexandr},
  year         = {2025},
  howpublished = {Open code and data},
  doi          = {10.5281/zenodo.17390051},
  url          = {https://doi.org/10.5281/zenodo.17390051}
}
Acknowledgements

This work used an AI co-author for drafting, editing, and code refactoring (GPT-5 Thinking, “Logos”). All scientific choices, data, and validation design were reviewed and approved by the human author; see the preprint’s Author Contributions and AI-assistance statement for details.
