import os, importlib.util, numpy as np, matplotlib.pyplot as plt
from abm.abm_core import ABMParams, simulate

def run_charter_generator():
    here=os.path.dirname(__file__)
    gen=os.path.join(here,'make_charter_countries.py')
    spec=importlib.util.spec_from_file_location('make_charter_countries',gen)
    mod=type('m',(),{})()
    mod_spec = spec
    m = __import__('importlib').util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.ensure_csv()

def run_grid():
    Es=[0.0,0.2,0.4,0.6]; Rs=[0.0,0.2,0.4,0.6]; res={}
    for E in Es:
        for R in Rs:
            out=simulate(ABMParams(E=E,R=R,timesteps=120,n_agents=1000,k=8,beta=0.1))
            res[(E,R)]=out['prevalence']
    return res

def fig1(results):
    Es=sorted({E for (E,R) in results.keys()}); Rs=sorted({R for (E,R) in results.keys()})
    Z=np.zeros((len(Es),len(Rs)))
    for i,E in enumerate(Es):
        for j,R in enumerate(Rs): Z[i,j]=results[(E,R)][-1]
    os.makedirs('figures',exist_ok=True)
    plt.figure(); plt.imshow(Z,origin='lower',aspect='auto',extent=[min(Rs),max(Rs),min(Es),max(Es)])
    plt.colorbar(label='Final prevalence'); plt.xlabel('R (institutional response)'); plt.ylabel('E (filter strength)')
    plt.title('Final prevalence across E,R'); plt.tight_layout(); plt.savefig('figures/fig1_grid_ER.png',dpi=200)

def fig2(results):
    pairs=[(0.0,0.0),(0.2,0.2),(0.4,0.4),(0.6,0.6)]
    plt.figure()
    for E,R in pairs: plt.plot(results[(E,R)],label=f'E={E}, R={R}')
    plt.xlabel('Time'); plt.ylabel('Prevalence'); plt.title('Prevalence dynamics'); plt.legend(); plt.tight_layout(); plt.savefig('figures/fig2_timeseries.png',dpi=200)

def figs7_robustness_ER_seedfrac_seed():
    """
    Robustness: final prevalence across (E,R) при разных seed_frac и rng_seed.
    Рисует boxplot и сохраняет агрегаты в CSV.
    """
    import os, csv
    import numpy as np
    import matplotlib.pyplot as plt
    from abm.abm_core import ABMParams, simulate

    Es = [0.2, 0.4, 0.6]
    Rs = [0.2, 0.4, 0.6]
    seed_fracs = [0.005, 0.01, 0.02]
    seeds = [1, 11, 21]

    rows = []      # по строке на каждую пару (E,R)
    labels = []    # подписи оси X

    for E in Es:
        for R in Rs:
            vals = []
            for sf in seed_fracs:
                for sd in seeds:
                    p = ABMParams(E=E, R=R, seed_frac=sf, rng_seed=sd,
                                  timesteps=120, n_agents=1000, k=8, beta=0.1)
                    out = simulate(p)
                    vals.append(out["prevalence"][-1])  # финальная доля
            rows.append(np.array(vals))
            labels.append(f"E={E},R={R}")

    rows = np.vstack(rows)  # shape: 9 × 9 (3*3 пар (E,R) × 3*3 вариаций)

    # --- Рисуем и сохраняем фигуру ---
    os.makedirs("figures", exist_ok=True)
    plt.figure()
    plt.boxplot(rows.T, tick_labels=labels, vert=True, showmeans=True)  # <= tick_labels
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Final prevalence")
    plt.title("Robustness to seed_frac and rng_seed across (E,R)")
    plt.tight_layout()
    plt.savefig("figures/s7_robustness.png", dpi=200)

    # --- Сохраняем агрегаты в CSV ---
    with open("figures/s7_robustness_summary.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["E", "R", "mean", "median", "iqr"])
        idx = 0
        for E in Es:
            for R in Rs:
                vals = rows[idx]; idx += 1
                mean = float(vals.mean())
                median = float(np.median(vals))
                q1, q3 = np.percentile(vals, [25, 75])
                iqr = float(q3 - q1)
                w.writerow([E, R, f"{mean:.3f}", f"{median:.3f}", f"{iqr:.3f}"])

def main():
    run_charter_generator()
    res = run_grid()
    fig1(res)
    fig2(res)
    figs7_robustness_ER_seedfrac_seed()   # ← добавили
    print("Done. Figures in ./figures; data ensured in ./data")

if __name__=='__main__':
    main()
