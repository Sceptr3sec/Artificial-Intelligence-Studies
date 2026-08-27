import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

test_values = [-10, -5, -2, 0, 2, 5, 10]

for z in test_values:
    print(z, sigmoid(z))