# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 02:37:33 2017

@author: Kevyn
"""
import time
import mnist_loader
import network

"""
This method wraps the network training program to supply run parameters.

learning_rate - degree to which the network updates its weights and biases.
epochs -        the number training sessions.
mini_batch -    the size of the training test data batches.
hidden_neurons- an array of hidden layers. Each entry adds a layer, and the
                value of the entry sets the size of that layer.
"""
def run_training(learning_rate=3.0, epochs=30, mini_batch=10,
                 hidden_neurons=[30]):
    
    # Init training data vaariables
    training_data, validation_data, \
    test_data = mnist_loader.load_data_wrapper()
    
    # Set input and output layer sizes.
    # Must be 784 input neurons -> x hidden layer neurons -> 10 output neurons
    if len(hidden_neurons) > 0:
        sizes = list(hidden_neurons)
        sizes.append(10)
        sizes.insert(0, 784)
    else:
        sizes = [784, 10]
    
    # Print running parameters
    print ("Running with learning_rate: " + str(learning_rate))
    print ("Running with epochs: " + str(epochs))
    print ("Running with mini_batch: " + str(mini_batch))
    print ("Running with neurons:")
    for layer_size in sizes: print(layer_size)
    print("Starting Program...")
    
    # Init the network
    net = network.Network(sizes)
    
    start = time.time()
    # Run the training algorithm
    net.SGD(training_data, epochs, mini_batch, learning_rate,
            test_data=test_data)
    stop = time.time()
    duration = stop - start
    print("duration = " + str(duration))
    
