import math


def sigmoid(x):
    return 1. / (1. + math.pow(math.e, - x))


class Network:
    def __init__(self, input_dimension, class_label, learning_rate):
        self.input_dimension = input_dimension
        self.class_label = class_label
        self.learning_rate = learning_rate

        self.weight_list = []
        for i in range(0, input_dimension + 1):
            self.weight_list.append(0.1)

    def train(self, row):
        input_row = row[:-1]
        input_row.append(1.)

        if row[-1].lower() == self.class_label[0].lower():
            label = 0.
        else:
            label = 1.

        # print label

        sum_input = 0.
        for i in range(0, len(input_row)):
            sum_input += input_row[i] * self.weight_list[i]
        output = sigmoid(sum_input)

        # print output
        # print output - label

        delta = output * (1. - output) * (label - output)
        for i in range(0, len(self.weight_list)):
            self.weight_list[i] += self.learning_rate * delta * input_row[i]

        # print self.weight_list

    def predict(self, row):
        input_row = row[:-1]
        input_row.append(1.)

        sum_input = 0.
        for i in range(0, len(input_row)):
            sum_input += input_row[i] * self.weight_list[i]
        output = sigmoid(sum_input)

        if output < 0.5:
            predict_label = self.class_label[0]
        else:
            predict_label = self.class_label[1]

        return predict_label, output

    def cross_validation(self, stratified_data_rows, num_epochs):
        output = {}

        for i in range(0, len(stratified_data_rows)):
            for j in range(0, self.input_dimension + 1):
                self.weight_list[j] = 0.1

            traning_rows = []
            testing_rows = []

            for row in stratified_data_rows[i]:
                testing_rows.append(row)
            for j in range(0, len(stratified_data_rows)):
                if j != i:
                    for row in stratified_data_rows[j]:
                        traning_rows.append(row)

            for epoch in range(0, num_epochs):
                for row in traning_rows:
                    self.train(row[0])

            for row in testing_rows:
                predict_label, confidence_of_prediction = self.predict(row[0])
                output[row[1]] = (i, predict_label, row[0][-1], confidence_of_prediction)

        return output
