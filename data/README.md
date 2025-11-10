# Data folder

This folder contains input data and auxiliary files for the simulations and figures.

- `charter_countries.csv` — demo table with country-level parameters for the Charter adoption scenarios (E/R proxies, governance indices). If `cg_hr_data.csv` is present, the generator derives `charter_countries.csv`; otherwise a small demo table is created.
- `economic_model_sensitivity.xlsx` — Excel workbook with the NPV sensitivity analysis for the “20% military → FF-T companion” scenario. Contains the yearly cash-flow assumptions, discounting, and parameter sweeps used for Appendix E (NPV distribution and related figures).
Unless otherwise specified, these data files are released under the same terms as `LICENSE-DATA`.
