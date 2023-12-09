# RouteGenius: Optimizing Delivery Networks with CVRP Solutions
### 94867 Decision Analytics & Public Policy
#### Fall 2023, Heinz College, Carnegie Mellon University
Authors: 

- Sajujya Gangopadhyay - sajujyag@andrew.cmu.edu
- Grace Eunji Kim - eunjik@andrew.cmu.edu
- Yi-Hsueh Yang - yihsuehy@andrew.cmu.edu

## Repository Structure
- belgium-road-km-n100-k10.vrp
- vrp_belgium_small.ipynb
- sensitivity_analysis.py
- new_cvrp.py
- optiguide_queries.ipynb
- OAI_CONFIG_LIST

## **Running the Project / Getting Started**
0. Dataset
- [Belgium Dataset](belgium-road-km-n100-k10.vrp)
- Source: OptaPlanner

1. vrp_belgium_small.ipynb
- This notebook preprocesses data, down-scales the dataset, solves the CVRP using random allocation and optimization using Gurobi, and visualizes the optimal solution.

2. Veroviz source code
- The folders for the veroviz package contains the package source code, which was edited for compatibility with our Gurobi implementation of the model.

3. sensitivity_analysis.py
- This python file produces sensitivity analysis plot for the parameters used in the optimization problem.

4. new_cvrp.py
- This is the python source file used by OptiGuide.

5. optiguide_queries.ipynb
- This notebook contains the query responses from OptiGuide.
- OAI_CONFIG_LIST: This is the configuration file required by OptiGuide implementation.

## Holistic Procedure
- The data was first preprocessed in the vrp_belgium_small.ipynb and the optimal solution was visualized using the veroviz package. Then, we wrote the new_cvrp.py file, which was the down-scaled optimization model compatible with OptiGuide. This file was then fed into the optiguide_queries notebook, which provided analysis with the language wrapper. Finally, the OptiGuide answers were validated by inputting the OptiGuide code back into the vrp_belgium_small.ipynb to produce the visualization for each OptiGuide query/scenario.
