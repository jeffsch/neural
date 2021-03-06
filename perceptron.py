__author__ = 'jeffs'

import random

c = 0.01    # learning rate

class Perceptron:
    def __init__(self, n):
        '''
        :param n: number of inputs for the perceptron
        :return: a perceptron
        '''
        # weights = x, y, and a bias parameter
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
        for i in range(len(self.weights)):
            self.weights[i] = c * error * inputs[i]

class Trainer:
    def __init__(self, x, y, a):
        self.inputs = []
        self.inputs.append(x)
        self.inputs.append(y)
        self.inputs.append(1.0) # bias parameter
        self.answer = a

def yline(x):
    return 2*x+1

trainingCount = 5000 # number of training points to create
ptron = Perceptron(3)
width = 640
height = 360
t = []

# create training points
for i in range(trainingCount):
    x = random.uniform(-width/2,width/2)
    y = random.uniform(-height/2,height/2)
    if y < yline(x):
        answer = -1
    else:
        answer = 1
    t.append(Trainer(x, y, answer))

# Run another loop to train the perceptron.  It's not the most efficient way to do it but
# for this sample it's fine.
for i in range(trainingCount):
    ptron.train(t[i].inputs, t[i].answer)

# create points to test the perceptron
correct = 0
testpoints = 2000
for i in range(testpoints):
    x = random.uniform(-width/2,width/2)
    y = random.uniform(-height/2,height/2)
    if y < yline(x): line = -1
    else: line = 1
    if (line == ptron.feedfoward([x,y,1])): correct += 1
print ('testpoints')
print (correct, testpoints)

#TODO check the percentage of correct training points
# check points in the training set
