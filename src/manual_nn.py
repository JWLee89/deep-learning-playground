import numpy as np
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


# Input data
class NeuralNetwork(object):

    def __init__(self):
        # An N x 2 dimensional vector with the
        # Following inputs
        # 1.
        self.layers = []
        self.activation_functions = []

    def add_layer(self, layer_size, activation_function):
        """
            Add layer to the neural network
            :return:
        """
        if type(layer_size) == int:
            layer_size = layer_size, layer_size
        self.layers.append(np.random.rand(*layer_size))
        self.activation_functions.append(activation_function)

    def feedforward(self, X):
        """
            Perform a forward pass
            :param output_dimension:
            :return:
        """
        input_layer = self.activation_functions[0](np.matmul(X, self.layers[0]))
        print(self.layers[0])
        # for i, layer in enumerate(self.layers[1:]):
        #     print(" x ", layer.shape)
        #     current = np.matmul(X, layer)


    """
        =================================
        Activation functions right here
        =================================
    """
    def relu(self, input_data):
        return np.maximum(input_data, 0)

    def softmax(self, input_data):
        exponents = np.exp(input_data)
        return exponents / sum(exponents, axis=0)



    """
        =================================
        Cost functions
        =================================
    """
    def cross_entropy_loss(self, y, y_pred):
        """
            Calculate the cross entropy loss
            between the cost and the loss

            :param y:
            :param y_pred:
            :return:
        """
        pass


    def fit(self, X, epoch_count=100):
        """
            Train the neural network
            by making a number of feedforward passes,
            along with back-propagation.
            :return:
        """
        for epoch in range(epoch_count):
            # Perform forward pass
            y = self.feedforward(X)
            # Calculate cost by subtracting the
            # output value with the actual cost
            y_pred = self.fit()


    def backpropagation(self, y, y_pred):
        """
            Perform backpropagation once we
            get the output from the neural network
            :return:
        """
        pass

    def calculate_cost(self, y, y_pred):
        """
            Find the value of the actual output.
            :param y: The actual output
            :param y_pred: The predicted output
            :return:
        """


    def predict(self, X):
        """
            Make an inference on a set of data
            :param X: The set of data to make an inference
            :return: A list of predictions made by the neural network
        """



neural_network =  NeuralNetwork()
neural_network.add_layer((28, 32), activation_function=neural_network.relu)
neural_network.add_layer((32, 16), activation_function=neural_network.relu)
neural_network.add_layer((16, 10), activation_function=neural_network.softmax)

neural_network.feedforward(X=x_train)
