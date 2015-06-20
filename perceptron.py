__author__ = 'jeffs'

import random
class perceptron:
    def __init__(self, n):
        '''
        :param n: number of inputs for the perceptron
        :return: a perceptron
        '''
        self.weights = [random.uniform(-1,1) for i in range(n)]
