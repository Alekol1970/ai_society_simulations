# Technical Appendix — ABM Repro (2025-10-31)

This appendix documents the exact steps and artifacts to fully reproduce the figures and tables referenced in the preprint.
## A. Repository layout (as of 2025-10-31)

ai_society_simulations/

├── abm/

│ └── abm_core.py

├── scripts/

│ ├── make_charter_countries.py

│ └── repro.py

├── notebooks/

│ └── figures/

│ └── ai_society_figures.ipynb

├── figures/ # generated on the fly

├── data/

│ ├── cg_hr_data.csv # optional

│ └── charter_countries.csv # auto-created if missing

├── README.md

└── CITATION.cff

## B. Environment

- Python ≥ 3.10  
- Install deps:
pip install -r requirements.txt

### C. One-command repro

- One-command repro:
```bash
python -m scripts.repro
```

## D. What the pipeline produces

After a successful run, the folder `figures/` contains:

- `fig1_grid_ER.png` — Final prevalence across E,R (heatmap)  
- `fig2_timeseries.png` — Prevalence dynamics for selected (E,R) pairs  
- `s7_robustness.png` — App. A, Fig. S7: Robustness to `seed_frac ∈ {0.5%, 1%, 2%}` and `rng_seed ∈ {1, 11, 21}`  
- `s7_robustness_summary.csv` — aggregates for S7 (mean / median / IQR)

**Note:** Figure numbers are not baked into images; numbering is controlled by the manuscript. Artifacts are created on the fly; the repository does not track binaries.

## E. Deterministic data seeding

If `data/charter_countries.csv` is absent, `scripts/make_charter_countries.py` creates a deterministic demo table with fixed RNG to guarantee stability of the examples.

## F. Mapping to manuscript

**Main text**  
- Fig. 1 → `fig1_grid_ER.png`  
- Fig. 2 → `fig2_timeseries.png`  

**Appendix A**  
- Fig. S7 → `s7_robustness.png` (+ `s7_robustness_summary.csv`)

## G. Notes on robustness (S7)

Boxplots are computed over 9 values per (E,R) cell (3 `seed_frac` × 3 `rng_seed`). Ordering across (E,R) is preserved; IQR typically ≈ 0.01–0.03. See CSV for exact aggregates.

## H. Re-running in Colab (optional)

Open `notebooks/figures/ai_society_figures.ipynb` → **Runtime** → **Restart and run all**.  
The notebook calls the same `scripts.repro` functions and writes artifacts into `figures/`.

## I. Provenance & licensing

- Code: Apache-2.0  
- Text & figures in this appendix: CC BY 4.0  
- Data (generated demo tables): CC BY 4.0

**Concept DOI:** 10.5281/zenodo.17390052  
**Version DOIs** are attached to individual GitHub releases.

