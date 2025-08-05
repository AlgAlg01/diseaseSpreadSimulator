import networkx as nx
import random
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
from person import Person    

class DiseaseSpreadSimulation:
    def __init__(self, graph, kill_prob, infect_prob,infect_inmune_prob, min_cure_days, max_cure_days):
        self.graph = graph
        self.people = {node: Person(node) for node in graph.nodes}
        self.kill_prob = kill_prob
        self.infect_prob = infect_prob
        self.infect_inmune_prob=infect_inmune_prob
        self.min_cure_days = min_cure_days
        self.max_cure_days = max_cure_days
        self.day = 0
        self.history = []

    def infect_initial(self, node):
        self.people[node].infect(self.kill_prob, self.min_cure_days, self.max_cure_days)

    def step(self):
        new_infections = []

        for person in self.people.values():
            if person.isInfected and not person.isDead:
                for neighbor in self.graph.neighbors(person.node):
                    neighbor_obj = self.people[neighbor]
                    if not neighbor_obj.isInfected and not neighbor_obj.hasBeenInfected:
                        for i in range(self.graph[person.node][neighbor]['freq']):
                            if neighbor not in new_infections and random.random() < self.infect_prob :
                                new_infections.append(neighbor)
                    elif not neighbor_obj.isInfected and neighbor_obj.hasBeenInfected:
                        if neighbor not in new_infections and random.random() < self.infect_inmune_prob:
                            new_infections.append(neighbor)        

        for node in new_infections:
            self.people[node].infect(self.kill_prob, self.min_cure_days, self.max_cure_days)

        for person in self.people.values():
            person.progress_disease()

        self.day += 1
        self.record_state()

    def is_finished(self):
        return all(p.isDead or not p.isInfected for p in self.people.values())

    def record_state(self):
        # Save color state for visualization
        colors = []
        for person in self.people.values():
            if person.isDead:
                colors.append('#111111')
            elif person.isInfected:
                colors.append('#f54242')
            elif person.hasBeenInfected:
                colors.append('#42f554')
            else:
                colors.append("#429ef5")    
        self.history.append(colors)

    def run(self, max_steps=100):
        self.record_state()
        while not self.is_finished() and self.day < max_steps:
            self.step()
        if not self.is_finished():
            for p in self.people.values():
                 if not p.isDead:
                     p.isInfected=False
                     p.infectionDaysLeft=0
                     p.willDieFromInfection=False
                     p.hasBeenInfected=True #vaccine
            self.record_state()         

    def animate(self):
        pos = nx.spring_layout(self.graph, seed=42,)  # Layout

        fig, ax = plt.subplots(figsize=(8, 6))

        def update(frame):
            ax.clear()
            colors = self.history[frame]
            nx.draw(self.graph, pos, node_color=colors, with_labels=False, ax=ax)
            ax.set_title(f"Day {frame}")
            if frame == len(self.history) - 1:
                ax.text(0.5, 1.05, "Simulation Finished", fontsize=14, ha='center', transform=ax.transAxes, color='darkred')

        ani = animation.FuncAnimation(fig, update, frames=len(self.history), interval=400, repeat=False)
        plt.show()
