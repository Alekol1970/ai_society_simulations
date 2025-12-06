# ai_society_simulations

## Preprint

The canonical preprint describing the companion architecture and simulations is available as  
[`ai-companion_social-shift_preprint_arxiv_v0.1.5.pdf`](ai-companion_social-shift_preprint_arxiv_v0.1.5.pdf).


Minimal, reproducible pipeline for the preprint (ABM of platform filtering **E** and institutional response **R**). Clean figures, one notebook, and an appendix with protocols.

**All versions DOI:**  
[![All versions DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17390051.svg)](https://doi.org/10.5281/zenodo.17390051)

**Latest version DOI:**  
[![Latest version DOI](https://zenodo.org/badge/994276536.svg)](https://zenodo.org/badge/latestdoi/994276536)
[![Release](https://img.shields.io/github/v/release/Alekol1970/ai_society_simulations?display_name=tag&sort=semver)](https://github.com/Alekol1970/ai_society_simulations/releases)


[![License: Apache-2.0 (Code)](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Docs: CC BY-NC 4.0](https://img.shields.io/badge/Docs-CC_BY--NC_4.0-lightgrey.svg)](LICENSE-DOCS)
[![Data: ODC-By + CC BY-NC](https://img.shields.io/badge/Data-ODC--By_1.0_+_CC_BY--NC_4.0-lightgrey.svg)](LICENSE-DATA)

**Proof of authorship & integrity**
- Evidence bundle (endorsement emails) registered on **Zenodo** — see `NOTICE.txt` for DOI and details.
- Releases are tagged on GitHub; figures/notebooks are reproducible from `scripts/repro.py`.
- Checksums for evidence files are inside the ZIP (`CHECKSUMS.txt`).
Release tags are GPG-signed

---

## Licensing (at a glance)
| Component | License | Notes |
|---|---|---|
| **Code & Algorithms** | Apache-2.0 | Open use with attribution; no endorsement. |
| **Texts & Concept Materials (Appendix F/G, G.1–G.2, figures’ captions)** | **CC BY-NC 4.0** | Non-commercial only; attribution required. |
| **Data / Tables / Index structures** | **ODC-By 1.0 + CC BY-NC 4.0** | Research use; commercial use requires permission. |
| **Audio / Regulatory Scripts** | Proprietary | Use by written permission only. |

**Proprietary modules (commercial license only):** Music Mirror, Video Mirror (symbolic shorts), Pair Dynamics.

**Commercial add-ons.** Materials listed in `appendix/License_Overview_*` (e.g., EmoTest-NG scoring rules, operator manuals, training scripts, branding assets) are offered under **separate commercial terms** upon request and are **not** covered by the open-source licenses in this repository.  
**Trademarks/brand names:** any use requires prior permission.

## Commercial offerings (concepts under proprietary license)

Short descriptions of modules/packages available under separate commercial terms by **Aleksandr Kolomiets**. For licensing/partnerships: <your-email-here>.

- **Pilot: AI Companion (B2B/B2G)** — safe pilot with KPIs, ethics (G.1/G.2), reports. *What clients pay for:* measurable impact, compliance, customization. **Proprietary.**
- **AI-led Webinar / Training** — scalable sessions on stress-resilience & self-support; pre/post metrics. *Pay for:* learning outcomes at scale. **Proprietary.**
- **Pairs Game (SaaS)** — light, guided “pair dynamics” practice with reports. *Pay for:* conflict reduction, retention. **Proprietary.**
- **EmoTest-NG** — minimal screening + scoring, norms & privacy. *Pay for:* validated metrics. **Proprietary.**
- **Trust & Safety / Ethics Pack** — playbooks from F/G/H/I; risk mitigation. *Pay for:* policies, audits. **Proprietary.**
- **Energy Analytics / Journals** — trends, micro-KPI, reports. *Pay for:* actionable insights. **Proprietary.**
- **R&D Bundle (datasets + notebook)** — clean, reproducible sets + code. *Pay for:* convenience & speed. **Proprietary.**
- **Platform Playbooks** — templates for governance & moderation. *Pay for:* ready procedures. **Proprietary.**
- **Case Studies / Reports** — evidence packs, narratives. *Pay for:* persuasion assets. **Proprietary.**
- **Learning Products** — courses & materials. *Pay for:* structured knowledge. **Proprietary.**
- **Music Mirror** — neuro-emotional music layer (no catalog). *Pay for:* regulation & IP. **Proprietary.**
- **Video Mirror (symbolic shorts)** — 2D/3D geometric stories with safe framing. *Pay for:* engagement & effect. **Proprietary.**
- **Computer Game as Mirror** — stand-alone experience, IP funnel. *Pay for:* IP & deployment. **Proprietary.**
- **Series: Companion Implementation** — scripted docu/anthology on deployment. *Pay for:* format rights, consultancy. **Proprietary.**
- **Equity / Revenue-share Model** — partnership tracks around the project. *Pay for:* structured deal options. **Proprietary.**

> Proprietary modules and concepts are **not** covered by open-source licenses in this repository and require a **separate commercial agreement** with the author.

More details: see [`NOTICE.txt`](./NOTICE.txt) (Proprietary modules) and [`TERMS_OF_USE.txt`](./TERMS_OF_USE.txt) (Generated Media & IP).

**Author:** **Aleksandr Kolomiets** · AI co-author: GPT-5 Thinking (“Logos”)  
**Repository:** https://github.com/Alekol1970/ai_society_simulations

**Commercial use** of materials in this repository is **prohibited without written consent** of the author.  
© **Aleksandr Kolomiets**, 2025. All rights reserved.  
Contact: <ai.society.commercial@gmail.com>

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

The simulation is deterministic given the parameters specified in
`scripts/repro.py`.

### Reproducible figures

The script

    python -m scripts.repro

regenerates the main ABM-based quantitative figures used in the paper
(e.g. the E–R surface and robustness plots for seed shares and parameter
perturbations), including the images underlying Figures 1 and S7.

In addition, the notebook produces a small number of exploratory plots
(e.g. `figures/fig2_timeseries.png`) that were useful for inspection
but are not used directly in the article.

Conceptual and purely illustrative diagrams (such as coverage and budget
scenarios or the global military-expenditure curve in the supplement)
are hand-crafted for clarity and are not intended to be generated
automatically from code.

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
