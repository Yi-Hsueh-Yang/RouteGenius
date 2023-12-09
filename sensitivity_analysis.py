import gurobipy as gp
from gurobipy import GRB, Model, quicksum
import matplotlib.pyplot as plt
import numpy as np

def cvrp(num_cars, capacity):
    # Hard code variables 
    num_locations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    num_vehicles = num_cars
    V = [0] + num_locations
    CAPACITY = capacity
    demands = {1: 15, 2: 16, 3: 31, 4: 14, 5: 33, 6: 7, 7: 9, 8: 17, 9: 33, 10: 26, 11: 18, 12: 10, 13: 32, 14: 26}
    distance_matrix = {(0, 0): 0.0, (0, 1): 142.045, (0, 2): 101.756, (0, 3): 31.554, (0, 4): 106.986, (0, 5): 31.592, (0, 6): 81.427, (0, 7): 57.534, (0, 8): 74.462, (0, 9): 62.477, (0, 10): 74.556, (0, 11): 180.648, (0, 12): 102.289, (0, 13): 73.463, (0, 14): 134.406, (1, 0): 140.803, (1, 1): 0.0, (1, 2): 94.792, (1, 3): 161.105, (1, 4): 38.164, (1, 5): 111.111, (1, 6): 201.61, (1, 7): 86.164, (1, 8): 109.372, (1, 9): 94.115, (1, 10): 111.962, (1, 11): 75.551, (1, 12): 94.073, (1, 13): 162.239, (1, 14): 254.551, (2, 0): 101.239, (2, 1): 94.845, (2, 2): 0.0, (2, 3): 132.35, (2, 4): 57.163, (2, 5): 85.549, (2, 6): 182.222, (2, 7): 57.872, (2, 8): 113.343, (2, 9): 39.555, (2, 10): 36.518, (2, 11): 106.221, (2, 12): 111.148, (2, 13): 153.777, (2, 14): 234.993, (3, 0): 31.367, (3, 1): 161.562, (3, 2): 132.292, (3, 3): 0.0, (3, 4): 134.86, (3, 5): 54.23, (3, 6): 52.037, (3, 7): 83.633, (3, 8): 74.95, (3, 9): 93.013, (3, 10): 105.088, (3, 11): 208.206, (3, 12): 107.002, (3, 13): 50.967, (3, 14): 105.615, (4, 0): 106.571, (4, 1): 38.181, (4, 2): 57.152, (4, 3): 135.057, (4, 4): 0.0, (4, 5): 84.247, (4, 6): 179.202, (4, 7): 52.296, (4, 8): 89.402, (4, 9): 58.531, (4, 10): 76.379, (4, 11): 76.863, (4, 12): 74.188, (4, 13): 141.182, (4, 14): 233.494, (5, 0): 30.717, (5, 1): 111.776, (5, 2): 85.229, (5, 3): 54.108, (5, 4): 83.9, (5, 5): 0.0, (5, 6): 100.137, (5, 7): 32.672, (5, 8): 51.736, (5, 9): 45.949, (5, 10): 65.867, (5, 11): 157.245, (5, 12): 72.564, (5, 13): 76.593, (5, 14): 156.804, (6, 0): 81.087, (6, 1): 200.441, (6, 2): 181.405, (6, 3): 52.024, (6, 4): 177.327, (6, 5): 98.733, (6, 6): 0.0, (6, 7): 126.1, (6, 8): 101.203, (6, 9): 142.732, (6, 10): 154.807, (6, 11): 250.673, (6, 12): 134.022, (6, 13): 48.076, (6, 14): 58.092, (7, 0): 57.704, (7, 1): 86.128, (7, 2): 57.897, (7, 3): 83.616, (7, 4): 52.06, (7, 5): 32.805, (7, 6): 127.76, (7, 7): 0.0, (7, 8): 63.858, (7, 9): 20.165, (7, 10): 45.928, (7, 11): 125.406, (7, 12): 69.114, (7, 13): 99.507, (7, 14): 184.426, (8, 0): 73.08, (8, 1): 109.317, (8, 2): 113.283, (8, 3): 75.307, (8, 4): 89.304, (8, 5): 51.411, (8, 6): 101.55, (8, 7): 63.966, (8, 8): 0.0, (8, 9): 81.469, (8, 10): 105.657, (8, 11): 162.004, (8, 12): 40.138, (8, 13): 60.186, (8, 14): 152.499, (9, 0): 61.711, (9, 1): 93.983, (9, 2): 39.306, (9, 3): 92.822, (9, 4): 58.639, (9, 5): 46.021, (9, 6): 142.694, (9, 7): 20.069, (9, 8): 80.978, (9, 9): 0.0, (9, 10): 25.763, (9, 11): 125.749, (9, 12): 86.196, (9, 13): 115.264, (9, 14): 195.465, (10, 0): 74.513, (10, 1): 111.747, (10, 2): 36.522, (10, 3): 105.495, (10, 4): 76.403, (10, 5): 65.942, (10, 6): 155.367, (10, 7): 45.849, (10, 8): 105.546, (10, 9): 25.781, (10, 10): 0.0, (10, 11): 133.969, (10, 12): 111.977, (10, 13): 140.263, (10, 14): 207.202, (11, 0): 181.621, (11, 1): 75.859, (11, 2): 111.668, (11, 3): 210.107, (11, 4): 76.702, (11, 5): 159.297, (11, 6): 254.251, (11, 7): 127.346, (11, 8): 162.121, (11, 9): 131.637, (11, 10): 139.119, (11, 11): 0.0, (11, 12): 146.822, (11, 13): 214.988, (11, 14): 307.301, (12, 0): 101.805, (12, 1): 94.084, (12, 2): 110.988, (12, 3): 107.374, (12, 4): 74.276, (12, 5): 72.113, (12, 6): 134.341, (12, 7): 69.417, (12, 8): 40.111, (12, 9): 86.675, (12, 10): 112.438, (12, 11): 146.772, (12, 12): 0.0, (12, 13): 92.978, (12, 14): 185.29, (13, 0): 73.285, (13, 1): 162.671, (13, 2): 153.013, (13, 3): 51.371, (13, 4): 141.058, (13, 5): 76.636, (13, 6): 47.903, (13, 7): 98.733, (13, 8): 60.674, (13, 9): 115.464, (13, 10): 139.911, (13, 11): 215.359, (13, 12): 93.492, (13, 13): 0.0, (13, 14): 94.174, (14, 0): 134.075, (14, 1): 254.613, (14, 2): 235.071, (14, 3): 105.826, (14, 4): 233.0, (14, 5): 155.405, (14, 6): 58.024, (14, 7): 182.772, (14, 8): 152.615, (14, 9): 195.792, (14, 10): 206.751, (14, 11): 307.3, (14, 12): 185.434, (14, 13): 93.908, (14, 14): 0.0}
    arcs = [(i, j) for i in V for j in V if i != j] 

    # Create a new model
    model = Model("CVRP")

    # OPTIGUIDE DATA CODE GOES HERE

    # Variables
    x = model.addVars(arcs, vtype=GRB.BINARY)
    u = model.addVars(num_locations, vtype=GRB.CONTINUOUS)

    # Objective: Minimize total distance
    model.modelSense = GRB.MINIMIZE
    model.setObjective(quicksum(x[i, j] * distance_matrix[i, j] for i, j in arcs))

    # Constraint 1: Each customer node visited exactly once
    model.addConstrs(quicksum(x[i, j] for j in V if j != i) == 1 for i in num_locations)
    model.addConstrs(quicksum(x[i, j] for i in V if i != j) == 1 for j in num_locations)

    # Constraint 2: Flow Conservation Constraint
    model.addConstrs((x[i, j] == 1) >> (u[i] + demands[j] == u[j])
                    for i, j in arcs if i != 0 and j != 0)
    # model.addConstrs((x[i, j] == 1) >> (u[i] + demands[j] == u[j])
    #                 for i, j in arcs if (i != 0 and j != 0) and (i != 13 and j != 13) and (i != 4 and j != 4))

    # Constraint 3: Capacity Constraints:
    model.addConstrs(u[i] >= demands[i] for i in num_locations)
    model.addConstrs(u[i] <= CAPACITY for i in num_locations)

    # Constraint 4: Use exactly n vehicles
    model.addConstr(quicksum(x[0, j] for j in num_locations) == num_vehicles)

    model.Params.MIPGap = 0.1
    model.Params.TimeLimit = 100 # seconds

    # Optimize model
    model.optimize()
    m = model

    # OPTIGUIDE CONSTRAINT CODE GOES HERE

    # Solve
    m.update()
    # Optimize model
    model.optimize()
    m = model

    if m.status == GRB.OPTIMAL:
        print("Total distance of all routes:", m.objVal)
    else:
        print("Not solved to optimality. Optimization status:", m.status)

    return round(m.objVal,3)

distance = {}
for i in range(100, 400, 5):
    for j in range(3, 9):
        distance[(j, i)] = cvrp(num_cars=j, capacity=i)
    
print(distance)

# Extract unique x and y values
X = [key[0] for key in distance.keys()]
Y = [key[1] for key in distance.keys()]
Z = list(distance.values())

# Define the grid size based on the range of X and Y values
X_unique = np.unique(X)
Y_unique = np.unique(Y)
X_grid, Y_grid = np.meshgrid(X_unique, Y_unique)

# Initialize the Z_grid with zeros
Z_grid = np.zeros(X_grid.shape)

# Loop through the data and fill Z_grid with values from Z
for x, y, z in zip(X, Y, Z):
    x_index = np.where(X_unique == x)[0][0]
    y_index = np.where(Y_unique == y)[0][0]
    Z_grid[y_index, x_index] = z

# Create the heatmap
plt.figure(figsize=(10, 6))
plt.pcolor(X_grid, Y_grid, Z_grid, cmap='summer')  # You can choose a different colormap
plt.colorbar(label='Distance')
plt.xlabel('Number of Vehicles')
plt.ylabel('Capacity of each Vehicle')
plt.title('Distance of # of vehicles and vehicles cap combination')
plt.gca().invert_yaxis()  # Invert Y-axis to match traditional heatmap orientation
plt.show()
