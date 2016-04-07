import math


def sigmoid(x):
    return 1. / (1. + math.pow(math.e, - x))


class Connection:
    def __init__(self):
        self.weight = 0.1


class Network:
    def __init__(self, input_dimension, class_label):
        self.input_dimension = input_dimension
        self.class_label = class_label

        self.connection_list = []
        for i in range(0, input_dimension + 1):
            self.connection_list.append(Connection())

    def train(self, row):
        input_row = row[:len(row) - 1]
        input_row.append(1.)

        if row[-1].lower() == self.class_label[0].lower():
            label = 0
        else:
            label = 1

        print label

        output = 0.
        for i in range(0, len(input_row)):
            output += input_row[i] * self.connection_list[i].weight

        print output
        print output - label