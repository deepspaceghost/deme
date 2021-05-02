import numpy as np

input_vector = [1.72, 1.23]
weights_1 = [1.26, 0]
weights_2 = [2.17, 0.32]

first_indexes_mult = input_vector[0] * weights_1[0]
second_indexes_mult = input_vector[1] * weights_1[1]
dot_product_1 = np.dot(input_vector, weights_1)
dot_product_2 = np.dot(input_vector, weights_2)

print("Hi!")
print(f"This dot product in: {dot_product_1}")
print(f"Another dot product is: {dot_product_2}")

input_vector = np.array([1.66, 1.56])
weights_1 = np.array([1.45, -0.66])
bias = np.array([0.0])


def sigmoid(x):
    """
    Some kind of arcane mathematics.
    """

    return 1 / (1 + np.exp(-x))


def make_preditcion(input_vector, weights, bias):
    """
    """

    layer_1 = np.dot(input_vector, weights) + bias
    layer_2 = sigmoid(layer_1)
    return layer_2


prediction = make_preditcion(input_vector, weights_1, bias)

print("Hello!")
print(f"The prediction result is: {prediction}")
