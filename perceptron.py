__author__ = 'jeffs'

import random
class perceptron:
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