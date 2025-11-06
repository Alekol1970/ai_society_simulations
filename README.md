# ai_society_simulations

Minimal, reproducible pipeline for the preprint (ABM of platform filtering **E** and institutional response **R**). Clean figures, one notebook, and an appendix with protocols.

[![DOI](https://zenodo.org/badge/994276536.svg)](https://doi.org/10.5281/zenodo.17390051)
[![License: Apache-2.0 (Code)](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Docs: CC BY-NC 4.0](https://img.shields.io/badge/Docs-CC_BY--NC_4.0-lightgrey.svg)](LICENSE-DOCS)
[![Data: ODC-By + CC BY-NC](https://img.shields.io/badge/Data-ODC--By_1.0_+_CC_BY--NC_4.0-lightgrey.svg)](LICENSE-DATA)

> **Proof of authorship (eAuthor.eu):** repository snapshot and key files are registered.  
> See `NOTICE.txt` for certificate IDs and timestamps.

---

## Licensing (at a glance)
| Component | License | Notes |
|---|---|---|
| **Code & Algorithms** | Apache-2.0 | Open use with attribution; no endorsement. |
| **Texts & Concept Materials (Appendix F/G, G.1–G.2, figures’ captions)** | **CC BY-NC 4.0** | Non-commercial only; attribution required. |
| **Data / Tables / Index structures** | **ODC-By 1.0 + CC BY-NC 4.0** | Research use; commercial use requires permission. |
| **Audio / Regulatory Scripts** | Proprietary | Use by written permission only. |

**Commercial add-ons.** Materials listed in `appendix/License_Overview_*` (e.g., EmoTest-NG scoring rules, operator manuals, training scripts, branding assets) are offered under **separate commercial terms** upon request and are **not** covered by the open-source licenses in this repository.  
**Trademarks/brand names:** any use requires prior permission.

**Author:** **Aleksandr Kolomiets** · AI co-author: GPT-5 Thinking (“Logos”)  
**Repository:** https://github.com/Alekol1970/ai_society_simulations

---

## What’s inside
- `notebooks/figures/ai_society_figures.ipynb` — single clean notebook (7 cells).
- `scripts/repro.py` — generates figures/data.
- `figures/` — outputs created at runtime.
- `appendix/` — F,G materials (EN/RU).

## Quick start (Colab)
Open: https://colab.research.google.com/github/Alekol1970/ai_society_simulations/blob/main/notebooks/ai_society_figures.ipynb  
Run: **Runtime → Restart and run all**. Figures appear in `figures/`.

## Reproducibility
- Deterministic params in `scripts/repro.py`.
- Generated files:
  - `figures/fig1_grid_ER.png`
  - `figures/fig2_timeseries.png`
  - `figures/s7_robustness.png`
  - `figures/s7_robustness_summary.csv`

## Appendix
- Appendix F (Energy / Ethics): `appendix/Appendix_F_operationalizing_energy_EN.md`
- Appendix G (Validation / Trust): `appendix/Appendix_G_validation_plan_EN.md`

## Cite
See `CITATION.cff`.

BibTeX:
```bibtex
@misc{kolomiets_abm_er_2025,
  title={Agent-based modeling of platform filtering (E) and institutional response (R)},
  author={Kolomiets, Aleksandr},
  year={2025},
  doi={10.5281/zenodo.17390052},
  howpublished={Open code and data}
}
