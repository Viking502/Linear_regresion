import random


class Regresion:

    def __init__(self, inputs_num):
        self.inputs_num = inputs_num
        self.weight = [random.random() for i in range(inputs_num)]
        self.bias = random.random()

        print('[{}, {}]'.format(self.weight[0], self.bias))

    def learn(self, input):

        print(input)
        print(self.weight[0] * input[0] + self.bias)
        error = self.weight[0] * input[0] + self.bias - input[1]
        print('error: ', error)

        for i in range(len(self.weight)):
            self.weight[i] -= 0.0000001 * error * input[i]
            #print(self.weight[i])
        self.bias -= 0.0000001 * error
        #print(self.bias)