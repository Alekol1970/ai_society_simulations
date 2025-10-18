# AI & Society — ABM Repro Package

One-command reproducibility.

## Reproduce
```
python -m venv .venv && . .venv/Scripts/activate   # Windows
# source .venv/bin/activate                        # macOS/Linux
pip install -r requirements.txt
python scripts/repro.py
```

## Layout
- abm/ (core model)
- scripts/ (make_charter_countries.py, repro.py)
- notebooks/analysis/ai_society_simulations.ipynb
- notebooks/figures/ai_society_figures.ipynb
- notebooks/appendix/cg_hr_t0_sensitivity.ipynb (optional)
