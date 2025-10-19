# AI & Society — ABM Repro Package

[![DOI](https://zenodo.org/badge/994276536.svg)](https://doi.org/10.5281/zenodo.17390051)

Код и материалы для препринта об агент-ориентированной модели (ABM) взаимодействия **E** (platform filtering) и **R** (institutional response).

## Быстрый запуск (Windows / macOS / Linux)

```bash
# 1) создать и активировать окружение
python -m venv .venv
# Windows:
.\.venv\Scriptsctivate
# macOS/Linux:
# source .venv/bin/activate

# 2) установить зависимости
pip install -r requirements.txt

# 3) воспроизвести все основные рисунки
python -m scripts.repro
```

Скрипт:
1) гарантирует наличие `data/charter_countries.csv` (создаёт детерминированный демо-набор, если файла нет);
2) строит **Fig.1–3** в папке `figures/`.

## Структура

```text
abm/
  abm_core.py                  # ядро ABM (параметры E, R)
scripts/
  make_charter_countries.py    # безопасно формирует data/charter_countries.csv при необходимости
  repro.py                     # Точка входа: генерирует Fig.1–3 "одной командой"
data/
  cg_hr_data.csv               # (опционально) исходник; при отсутствии генерится демо-таблица
  charter_countries.csv        # создаётся автоматически, если не найден
figures/
  fig1_grid_ER.png
  fig2_timeseries.png
  fig3_robustness.png
  fig3_robustness_summary.csv  # агрегаты к Fig.3 (mean/median/IQR)
notebooks/
  analysis/
    ai_society_simulations.ipynb   # полный анализ/эксперименты (источник правды)
  figures/
    ai_society_figures.ipynb       # человеко-читаемая отрисовка/варианты фигур
  appendix/
    # опциональные ноутбуки с дополнительными проверками
tests/
  test_abm.py
requirements.txt
environment.yml
```

## Что показывают основные рисунки

- **Fig.1** — финальная распространённость по сетке (E,R).
- **Fig.2** — динамика распространённости во времени для выбранных пар (E,R).
- **Fig.3 (Robustness)** — устойчивость результатов при варьировании **инициализации**:
  seed fraction ∈ {0.5%, 1%, 2%} и rng seed ∈ {1, 11, 21}.
  Порядок исходов по (E,R) сохраняется, разброс малый (см. `fig3_robustness_summary.csv`).

## Code & Data availability

All code and data to reproduce the figures are openly available at **Concept DOI: 10.5281/zenodo.17390052**.  
This release (**v0.1.0**) is archived under **Version DOI: 10.5281/zenodo.17390051**.

Core figures are generated with a single command:
```bash
python -m scripts.repro
```

A deterministic demo dataset (`data/charter_countries.csv`) is created automatically if `cg_hr_data.csv` is absent.  
Additional plotting steps and the t₀-sensitivity artifacts are provided in `notebooks/figures/ai_society_figures.ipynb`.

## License

[![License: Apache-2.0](https://img.shields.io/badge/Code-Apache--2.0-blue.svg)](./LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/Text%20%26%20Figures-CC%20BY%204.0-green.svg)](./LICENSE-DOCS)
[![License: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-green.svg)](./LICENSE-DATA)

- **Code:** Apache-2.0  
- **Text & figures:** CC BY 4.0  
- **Data:** CC BY 4.0

By using this repository you agree to the terms above.  
See the license files in the root directory for full texts.

## Citation

If you use this repository, please cite the archived release:

```bibtex
@misc{alekseev_abm_er_2025,
  title        = {Agent-based modeling of platform filtering (E) and institutional response (R)},
  author       = {Alekseev, Alexander},
  year         = {2025},
  howpublished = {Open code and data},
  doi          = {10.5281/zenodo.17390051},
  url          = {https://doi.org/10.5281/zenodo.17390051}
}
```
