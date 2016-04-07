from neural_net import *

trainfile = "sonar.arff"
num_folds = 10
learning_rate = 0.1
num_epochs = 50

data_rows, class_label = read_file(trainfile)

stratified_data_rows = n_fold_stratified(num_folds, data_rows, class_label)

# print data_rows[0]
# print class_label

network = Network(len(data_rows) - 1, class_label)



