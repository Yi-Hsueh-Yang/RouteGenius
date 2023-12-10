# RouteGenius: Optimizing Delivery Networks with CVRP Solutions
### 94867 Decision Analytics & Public Policy
#### Fall 2023, Heinz College, Carnegie Mellon University
Authors: 

- Sajujya Gangopadhyay - sajujyag@andrew.cmu.edu
- Grace Eunji Kim - eunjik@andrew.cmu.edu
- Yi-Hsueh Yang - yihsuehy@andrew.cmu.edu
  
## Executive Summary 
RouteGenius is a cutting-edge solution that revolutionizes delivery network optimization through the implementation of the Capacitated Vehicle Routing Problem (CVRP) using Optimization through Gurobi, and an interface to converse with the model using a Natural Language Wrapper (OptiGuide).
In the rapidly evolving landscape of logistics and supply chain management, efficient route planning is a critical factor in reducing costs and enhancing overall operational effectiveness. RouteGenius addresses this challenge by seamlessly integrating CVRP algorithms to create a dynamic and adaptive system that continually optimizes delivery routes with changing demand, vehicle capacities, and even integration with real-time traffic data. 

### Key Features
- CVRP Optimization: RouteGenius employs CVRP algorithms to efficiently allocate resources and plan delivery routes, considering vehicle capacity constraints and optimizing for the shortest paths. This leads to reduced transportation costs and optimized route allocation which can be used by transportation services, ride-share applications and food-delivery and logistics companies like Uber, Doordash, and FedEx.
- Real-time Adaptability: The system, coupled with the language wrapper (Optiguide) is designed to dynamically adapt to changing conditions in real-time through human feedback in the form of both rudimentary and exploratory questions. It changes the underlying code to factor in additional constraints and changes in demand while simultaneously ensuring that routes remain optimal and responsive to the evolving operational environment.
- Sustainability: By minimizing fuel consumption and carbon emissions through route optimization, RouteGenius supports environmentally conscious and sustainable logistics practices.
  
In conclusion, RouteGenius is a game-changing solution for organizations seeking to optimize their delivery networks. By integrating CVRP algorithms and Natural Language technologies, it offers a comprehensive and adaptive approach to route planning, resulting in substantial cost savings, operational efficiency, and a positive impact on environmental sustainability.

## Problem Statement
In the dynamic landscape of delivery services, the effective management of delivery routes poses a critical challenge for companies striving to meet customer demands and minimize operational costs. Our model addresses this challenge through the implementation of the Capacitated Vehicle Routing problem (CVRP). The CVRP pertains to the operations of any company that dwells with logistic operations involving the transportation of goods from one depot to customers using a predefined set of vehicles on a road network. Therefore, the primary question that motivates this problem is: What is the optimal set of routes for a fleet of vehicles to traverse in order to deliver to a given set of customers? The primary objective is to develop an optimized set of routes (solution), with each route tailored for a specific vehicle, ensuring that all customer requirements and operational constraints (i.e., limited load capacity) are met while simultaneously minimizing the overall transportation cost (objective function). The optimized cost to travel from node $i$ to node $j$ would be the distance between the two nodes that is travelled along the optimal route.

## Repository Structure
- belgium-road-km-n100-k10.vrp
- vrp_belgium_small.ipynb
- sensitivity_analysis.py
- new_cvrp.py
- optiguide_queries.ipynb
- OAI_CONFIG_LIST

## **Running the Project / Getting Started**
0. Dataset
[Belgium Dataset](belgium-road-km-n100-k10.vrp)
Source: OptaPlanner

1. vrp_belgium_small.ipynb
   This notebook preprocesses data, down-scales the dataset, solves the CVRP using random allocation and optimization using Gurobi, and visualizes the optimal solution.

2. Veroviz source code
  The folders for the veroviz package contain the package source code, which was edited for compatibility with our Gurobi implementation of the model.

3. sensitivity_analysis.py
  This Python file produces a sensitivity analysis plot for the parameters used in the optimization problem.

4. new_cvrp.py
  This is the Python source file used by OptiGuide.

5. optiguide_queries.ipynb
  This notebook contains the query responses from OptiGuide.
  OAI_CONFIG_LIST: This is the configuration file required by OptiGuide implementation.

## Holistic Procedure
- The data was first preprocessed in the vrp_belgium_small.ipynb and the optimal solution was visualized using the veroviz package. Then, we wrote the new_cvrp.py file, which was the down-scaled optimization model compatible with OptiGuide. This file was then fed into the optiguide_queries notebook, which provided analysis with the language wrapper. Finally, the OptiGuide answers were validated by inputting the OptiGuide code back into the vrp_belgium_small.ipynb to produce the visualization for each OptiGuide query/scenario.
