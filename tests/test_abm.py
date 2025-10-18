from abm.abm_core import ABMParams, simulate

def test_smoke():
    out = simulate(ABMParams(timesteps=5, n_agents=200))
    assert 'prevalence' in out and len(out['prevalence'])==6
