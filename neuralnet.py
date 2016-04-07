from neural_net import *

trainfile = "sonar.arff"
num_folds = 10
learning_rate = 0.1
num_epochs = 50

data_rows, class_label = read_file(trainfile)

stratified_data_rows = n_fold_stratified(num_folds, data_rows, class_label)

# print data_rows[0]
# print class_label

network = Network(len(data_rows[0]) - 1, class_label, learning_rate)

# print stratified_data_rows[0][0]

output = network.cross_validation(stratified_data_rows, num_epochs)

# print output

for row in data_rows:
    print str(output[str(row)][0]) + ' ' + output[str(row)][1].encode("ascii") \
          + ' ' + output[str(row)][2].encode("ascii") + ' ' + str(output[str(row)][3])
