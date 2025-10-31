# Technical Appendix — ABM Repro (2025-10-31)

This appendix documents the exact steps and artifacts to fully reproduce the figures and tables referenced in the preprint.

## A. Repository layout (as of 2025-10-31)

abm/
abm_core.py
scripts/
make_charter_countries.py
repro.py
notebooks/
figures/
ai_society_figures.ipynb
figures/
(generated on the fly)
data/
cg_hr_data.csv (optional)
charter_countries.csv (auto-created if missing)

## B. Environment

- Python ≥ 3.10  
- `pip install -r requirements.txt`  
- One-command repro:
```bash
python -m scripts.repro
C. What the pipeline produces

After a successful run, the folder figures/ contains:

fig1_grid_ER.png — Final prevalence across E,R (heatmap)

fig2_timeseries.png — Prevalence dynamics for selected (E,R) pairs

s7_robustness.png — App. A, Fig. S7: Robustness to seed_frac∈{0.5%,1%,2%} and rng_seed∈{1,11,21}

s7_robustness_summary.csv — aggregates for S7 (mean / median / IQR)

Note: Figure numbers are not baked into images; numbering is controlled by the manuscript.

D. Deterministic data seeding

If data/charter_countries.csv is absent, scripts/make_charter_countries.py creates a deterministic demo table with fixed RNG to guarantee stability of the examples.

E. Mapping to manuscript

Main text

Fig. 1 → fig1_grid_ER.png

Fig. 2 → fig2_timeseries.png

Appendix A

Fig. S7 → s7_robustness.png (+ s7_robustness_summary.csv)

F. Notes on robustness (S7)

Boxplots are computed over 9 values per (E,R) cell (3 seed_fracs × 3 rng_seeds). Ordering across (E,R) is preserved; IQR typically ≈ 0.01–0.03. See CSV for exact aggregates.

G. Re-running in Colab (optional)

Open notebooks/figures/ai_society_figures.ipynb → Runtime → Restart and run all.
The notebook calls the same scripts.repro functions and writes artifacts into figures/.

H. Provenance & licensing

Code: Apache-2.0

Text & figures in this appendix: CC BY 4.0

Data (generated demo tables): CC BY 4.0

Concept DOI: 10.5281/zenodo.17390052; Version DOIs are attached to individual releases.

---

# 2) Приложения F и G — версии для репозитория (EN + RU)

Создай в `appendix/` четыре файла:

### `appendix/Appendix_F_operationalizing_energy_EN.md`

```markdown
# Appendix F — Operationalizing the “Energy-Efficiency of Intervention” (E*)

## F1. Rationale
We define an ethical intervention as **the minimally sufficient intervention** that achieves non-worsening outcomes. To compare strategies, we aggregate costs and load into a single index **E\***.

## F2. Components of E\*
- **Physiology**: heart-rate variability (HRV: RMSSD/SDNN; ms)
- **Behavior**: time-to-stabilization; frequency of episodes
- **Compute**: local CPU/GPU load, on-device battery impact
- **Social**: false positives; user complaints / appeals

All components are z-scored against a baseline (Phase A). E\* is a weighted sum with weights pre-registered; sensitivity reported in SI.

## F3. Estimation & comparison
- ABA mini-studies (A–B–A′): mixed models (random intercept per participant)
- Pilot RCT: ANCOVA/LMM, group factor (companion vs. active control)
- Strategy comparison is performed **under a fixed intervention budget** (time quota, compute cap), making “thrift” measurable rather than implicit.

## F4. Child scenario
The companion acts as a **supportive external regulator**, not surveillance. Prompts are phrased in the language of care; directive interpretations of intentions are avoided. Primary ethics goal: reduce shame and avoid “I am dangerous / I am guilty” internalizations.

## F5. Reporting
We report: (i) ΔHRV, (ii) Δtime-to-stabilization, (iii) Δepisode rate, (iv) compute footprint, (v) appeals ratio. Lower E\* at non-worse primary outcomes is considered ethically superior.
