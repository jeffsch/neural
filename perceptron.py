__author__ = 'jeffs'

import random

c = 0.01    # learning rate

class Perceptron:
    def __init__(self, n):
        '''
        :param n: number of inputs for the perceptron
        :return: a perceptron
        '''
        self.weights = [random.uniform(-1,1) for i in range(n)]
    def activate(self, sum):
        if sum > 0: return 1
        else: return -1
    def feedfoward(self, inputs):
        sum = 0.0
        for i in range(len(inputs)):
            sum += self.weights[i]*inputs[i]
        return self.activate(sum)
    def train(self, inputs, desired):
        guess = self.feedfoward(inputs)
        error = desired - guess
        for i in range(self.weights):
            self.weights[i] = c * error * inputs[i]

class Trainer:
    def __init__(self, x, y, a):
        self.inputs[0] = x
        self.inputs[1] = y
        self.inputs[2] = 1
        self.answer = a
