import arff
import random


def read_file(trainfile):
    data_rows = []
    class_label = []

    data = arff.load(open(trainfile, 'rb'))

    for row in data['data']:
        data_rows.append(row)

    for attribute in data['attributes']:
        if attribute[0].lower() == 'class':
            class_label = attribute[1]

    return data_rows, class_label


def n_fold_stratified(n, data_rows, class_label):
    total_rows = len(data_rows)
    row_length = len(data_rows[0])

    data_rows_label_0 = []
    data_rows_label_1 = []

    for row in data_rows:
        if row[row_length - 1].lower() == class_label[0].lower():
            data_rows_label_0.append(row)
        else:
            data_rows_label_1.append(row)

    # print len(data_rows_label_0)
    # print len(data_rows_label_1)

    random.seed()
    random.shuffle(data_rows_label_0)
    random.shuffle(data_rows_label_1)

    fold_sample_num = []
    for i in range(0, n):
        fold_sample_num.append(0)
    for i in range(0, total_rows):
        fold_sample_num[i % n] += 1

    # print fold_sample_num

    stratified_data_rows = []
    for i in range(0, n):
        stratified_data_rows.append([])
    # print stratified_data_rows
    for i in range(0, len(data_rows_label_0)):
        stratified_data_rows[i % n].append(data_rows_label_0[i])
    # for i in range(0, n):
    #     print len(stratified_data_rows[i])

    for i in range(0, n):
        while len(stratified_data_rows[i]) < fold_sample_num[i]:
            stratified_data_rows[i].append(data_rows_label_1[0])
            data_rows_label_1 = data_rows_label_1[1:]

    # for i in range(0, n):
    #     print len(stratified_data_rows[i])

    # print stratified_data_rows
    return stratified_data_rows
