import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

test_values = [-10, -5, -2, 0, 2, 5, 10]

for z in test_values:
    print(z, sigmoid(z))

def classify(probability):
    if probability >= 0.5:
        return "Malware"
    else:
        return "Benign"

probabilities = [0.12, 0.49, 0.50, 0.72, 0.99]

for probability in probabilities:
    print(probability, classify(probability))