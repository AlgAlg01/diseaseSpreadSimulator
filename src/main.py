import networkx as nx
import random
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
from simulation import DiseaseSpreadSimulation    
    
if __name__ == "__main__":
    def load_config(filename="config.json"):
        with open(filename) as f:
            return json.load(f)
        
    config=load_config()    
    random.seed(config['seed'])
    k=config['num_communities']
    l=config['people_per_community']
    G = nx.connected_caveman_graph(l, k)  
    communities = [set(range(i * k, (i + 1) * k)) for i in range(len(G) // k)]
    nodes=list(G.nodes())
    def coummunity_index(node):
        return next(i for i, comm in enumerate(communities) if nodes.index(node) in comm)
    for u,v in G.edges:
        if coummunity_index(u)==coummunity_index(v):
            G[u][v]['freq']=random.randint(1,8)
        else:
            G[u][v]['freq']=1    
    sim = DiseaseSpreadSimulation(
        G,
        kill_prob=config['kill_prob'],
        infect_prob=config['infect_prob'],
        infect_inmune_prob=config['infect_inmune_prob'],
        min_cure_days=config['min_cure_days'],
        max_cure_days=config['max_cure_days']
    )
    sim.infect_initial(random.choice(list(G.nodes)))
    sim.run()
    sim.animate()
