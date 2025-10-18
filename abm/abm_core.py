from dataclasses import dataclass
import numpy as np, networkx as nx
from typing import Dict, Any, Tuple

@dataclass
class ABMParams:
    n_agents:int=1000; k:int=8; beta:float=0.1; seed_frac:float=0.01; timesteps:int=100; E:float=0.3; R:float=0.2; rng_seed:int=42

def initialize_graph(p:ABMParams)->Tuple[nx.Graph,np.ndarray]:
    rng=np.random.default_rng(p.rng_seed)
    G=nx.watts_strogatz_graph(p.n_agents,p.k,p.beta,seed=p.rng_seed)
    state=np.zeros(p.n_agents,dtype=np.int8)
    idx=rng.choice(p.n_agents,size=max(1,int(p.seed_frac*p.n_agents)),replace=False)
    state[idx]=1
    return G,state

def step(G,state,p,rng):
    new=state.copy()
    spread=0.20*(1.0-p.E)
    recov=0.05+0.40*p.R
    for i in range(len(state)):
        if state[i]==1:
            if rng.random()<recov: new[i]=0
            for j in G.neighbors(i):
                if state[j]==0 and rng.random()<spread: new[j]=1
    return new

def simulate(p:ABMParams)->Dict[str,Any]:
    G,state=initialize_graph(p); rng=np.random.default_rng(p.rng_seed)
    series=[state.mean()]
    for _ in range(p.timesteps):
        state=step(G,state,p,rng); series.append(state.mean())
    return {"prevalence":np.array(series),"params":p}
