# diseaseSpreadSimulator

Overview:
---------
This project simulates the spread of an infectious disease through a community graph using a probabilistic model. It includes a visualization of the spread and a GUI to configure simulation parameters. Each node in the graph represents a person, and connections (edges) represent interactions between individuals.

Features:
---------
- Graph-based simulation of disease spread
- Configurable infection and mortality rates
- Immune reinfection probability (different than normal infection probability)
- Animated visualization using matplotlib
- GUI to set simulation parameters
- Infection duration and death outcomes


Instalation and execution:
-----------

1. To install required libraries, run:
```bash
pip install requirements.txt
```

2. Run the GUI by running gui.py on the proyect root  (*Note:* if your config.json is already saved, you can alternatively run main.py in the src folder)

3. Enter the desired configuration values in the GUI:
   - Seed (for reproducibility)
   - Number of communities
   - People per community
   - Infection probabilities and durations
   - Probability of death due to infection

4. Click "Save Config" to store the settings in `config.json`.

5. Click "Run Simulation" to execute the simulation with the current configuration. (*Note:* configuration should be saved with valid values before you run the simulation)

Configuration Parameters (in config.json):
------------------------------------------
- `seed`: Random seed for reproducibility (integer)
- `num_communities`: Number of isolated communities in the graph
- `people_per_community`: People per community (determines graph size)
- `kill_prob`: Probability that an infected person dies
- `infect_prob`: Probability that an infection occurs during contact
- `infect_inmune_prob`: Infection probability for previously infected people
- `min_cure_days`: Minimum number of days for recovery
- `max_cure_days`: Maximum number of days for recovery

Dependencies:
-------------
- Python 3.x
- networkx
- matplotlib
- tkinter (comes with Python)
- json
- os, sys, subprocess (standard libraries)

Visualization:
--------------
The simulation is visualized using `matplotlib.animation`. Each node is color-coded:
- Red: Currently infected
- Green: Recovered and immune
- Blue: Never infected
- Black: Dead


