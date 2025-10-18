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
    plt.title('Fig.1: Final prevalence across E,R'); plt.tight_layout(); plt.savefig('figures/fig1_grid_ER.png',dpi=200)

def fig2(results):
    pairs=[(0.0,0.0),(0.2,0.2),(0.4,0.4),(0.6,0.6)]
    plt.figure()
    for E,R in pairs: plt.plot(results[(E,R)],label=f'E={E}, R={R}')
    plt.xlabel('Time'); plt.ylabel('Prevalence'); plt.title('Fig.2: Prevalence dynamics'); plt.legend(); plt.tight_layout(); plt.savefig('figures/fig2_timeseries.png',dpi=200)

def main():
    run_charter_generator(); res=run_grid(); fig1(res); fig2(res); print('Done. Figures in ./figures; data ensured in ./data')

if __name__=='__main__':
    main()
