
import numpy as np

# Input data
inputs = np.array([[0.5, 0.2]])

# Weights and bias
weights = np.array([[0.4, 0.6],
                    [0.3, 0.7]])

bias = np.array([0.1, 0.1])

# Feed forward calculation
hidden = np.dot(inputs, weights) + bias

# Sigmoid activation function
output = 1 / (1 + np.exp(-hidden))

print("Input:", inputs)
print("Output:", output)
