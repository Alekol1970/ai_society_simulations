# AI Society Simulations & Supplementary Material
*Companion repository for the articles submitted to **AI and Ethics** and **AI & Society***  
Author – **Aleksandr Kolomiets** ORCID 0009-0008-5153-5546

---

## 1 What is here?
This repo contains **all synthetic data, code notebooks and figures** that support the two core demonstrations in the manuscripts:

| Section | Purpose | Files |
|---------|---------|-------|
| **1 – CG vs Homicide (Monte-Carlo)** | Illustrates the inverse correlation between capability-gain (CG, «months of additional capability per year») and homicide rate | *ai_society_simulations.ipynb*  (first part)  ·  **cg_hr_data.csv**, **cg_hr_plot.png** |
| **2 – Charter Scenario (3 countries)** | Stylised 10-year projection of how a *Non-Violent Governance Charter* diffuses into countries with different initial conditions | the same notebook (second part) ·  **charter_countries.csv**, **charter_cg_plot.png**, **charter_hr_plot.png** |
| **Technical Appendix** | Sensor layer, index model, ethical filter logic; 6 pp PDF referenced in the articles | **technical_appendix.pdf** |

---

## 2 Quick start – reproduce the figures

1. Open the notebook directly in your browser via the GitHub viewer **or** in Colab:  

## 3 File list

* [`ai_society_simulations.ipynb`](ai_society_simulations.ipynb) — single notebook, 2 independent sections  
* [`cg_hr_data.csv`](cg_hr_data.csv) — 5 000 Monte-Carlo pairs (Capability-Gain, Homicide)  
* [`cg_hr_plot.png`](cg_hr_plot.png) — published Figure 1  
* [`charter_countries.csv`](charter_countries.csv) — synthetic 3-country time-series (Year, HR, CG)  
* [`charter_cg_plot.png`](charter_cg_plot.png) — Figure 2 (Capability-Gain trajectories)  
* [`charter_hr_plot.png`](charter_hr_plot.png) — Figure 3 (Homicide trajectories)  
* [`technical_appendix.pdf`](technical_appendix.pdf) — 6-page detailed specs referenced in the papers  

---

## 4 Data & code availability
All synthetic data, simulation notebooks, and the Technical Appendix are **openly available** in this repository under the MIT License and may be reused without restriction, provided appropriate citation.

---

## 5 How to cite
Kolomiets, A. (2025). Ethical Architecture of an AI Companion for Non-Violent
Adaptation. Preprint, arXiv:2406.xxxxx. Supplementary material available at
https://github.com/Alekol1970/ai_society_simulations

---

## 6 License
Code, synthetic data and figures — **MIT License**  
Text in *technical_appendix.pdf* — CC-BY-4.0

---

| `ai_society_figures.ipynb` | Notebook for Figures 4–6 (diffusion, budget, risk matrix) |

*Last update : 2025-06-03*
