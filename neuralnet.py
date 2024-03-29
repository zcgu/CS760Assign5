from neural_net import *
import sys


def main():
    trainfile = str(sys.argv[1])
    num_folds = int(sys.argv[2])
    learning_rate = float(sys.argv[3])
    num_epochs = int(sys.argv[4])

    data_rows, class_label = read_file(trainfile)

    stratified_data_rows = n_fold_stratified(num_folds, data_rows, class_label)

    network = Network(len(data_rows[0][0]) - 1, class_label, learning_rate)

    output = network.cross_validation(stratified_data_rows, num_epochs)

    for i in range(0, len(data_rows)):
        print str(output[i][0]) + ' ' + output[i][1].encode("ascii") \
              + ' ' + output[i][2].encode("ascii") + ' ' + str(output[i][3])


def part_b_1():
    trainfile = 'sonar.arff'
    num_folds = 10
    learning_rate = 0.1
    num_epochs = [25, 50, 75, 100]

    accuracys = []

    for epoch in num_epochs:
        data_rows, class_label = read_file(trainfile)

        stratified_data_rows = n_fold_stratified(num_folds, data_rows, class_label)

        network = Network(len(data_rows[0][0]) - 1, class_label, learning_rate)

        output = network.cross_validation(stratified_data_rows, epoch)
        accuracys.append(accuracy(output, data_rows))

    print accuracys
    try:
        import matplotlib.pyplot as plt
        plt.plot(num_epochs, accuracys)
        plt.xlabel('epochs')
        plt.ylabel('accuracy')
        plt.show()
    finally:
        pass


def part_b_2():
    trainfile = 'sonar.arff'
    num_folds = [5, 10, 15, 20, 25]
    learning_rate = 0.1
    num_epochs = 50

    accuracys = []
    for fold in num_folds:
        data_rows, class_label = read_file(trainfile)

        stratified_data_rows = n_fold_stratified(fold, data_rows, class_label)

        network = Network(len(data_rows[0][0]) - 1, class_label, learning_rate)

        output = network.cross_validation(stratified_data_rows, num_epochs)
        accuracys.append(accuracy(output, data_rows))

    print accuracys
    try:
        import matplotlib.pyplot as plt
        plt.plot(num_folds, accuracys)
        plt.xlabel('folds')
        plt.ylabel('accuracy')
        plt.show()
    finally:
        pass


def part_b_3():
    trainfile = 'sonar.arff'
    num_folds = 10
    learning_rate = 0.1
    num_epochs = 50

    data_rows, class_label = read_file(trainfile)

    stratified_data_rows = n_fold_stratified(num_folds, data_rows, class_label)

    network = Network(len(data_rows[0][0]) - 1, class_label, learning_rate)

    output = network.cross_validation(stratified_data_rows, num_epochs)

    roc(output, data_rows, class_label)


main()
# part_b_1()
# part_b_2()
# part_b_3()
