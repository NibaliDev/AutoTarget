import numpy as np
from scipy.optimize import fsolve 

# Constants
d1 = 10.0
d2 = 8.7
t1 = 0.0175
t2 = 0.0175
s = 343.0  # Speed of sound in m/s 


# Define the system of equations
def equations(vars):
    x, y = vars
    f1 = np.sqrt((d1 - x*x)**2 + (d2 - y)**2) - (x*x + y*y)**2 - t1 * s
    f2 = np.sqrt((x - d1/2)**2 + (d2 - y)**2) - (x*x + y*y)**2 - t2 * s
    return [f1, f2]

# Initial guesses for x and y
initial_guess = [1.0, 1.0]

# Solve the equations
solution = fsolve(equations, initial_guess)

x, y = solution
print(f"Solution found: x = {x:.6f}, y = {y:.6f}") 
