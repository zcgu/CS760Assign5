
def accuracy(output, data_rows):
    correct = 0.
    for i in range(0, len(data_rows)):
        if output[i][1].lower() == output[i][2].lower():
            correct += 1
    # print correct
    # print len(output)
    # print correct / len(output)
    return correct / len(output)


def roc(output, data_rows, class_label):
    output_list = []
    for i in range(0, len(data_rows)):
        output_list.append(output[i])
    # print output_list

    output_list = sorted(output_list, key=lambda output_item: output_item[3], reverse= True)

    total_positive = 0.
    total_negative = 0.

    for item in output_list:
        if item[2].lower() == class_label[1].lower():
            total_positive += 1.
        else:
            total_negative += 1.

    false_positive = []
    true_positive = []
    false_positive.append(0.)
    true_positive.append(0.)

    current_positive = 0.
    current_negative = 0.
    for i in range(0, len(output_list)):
        if output_list[i][2].lower() == class_label[1].lower():
            current_positive += 1.
        else:
            current_negative += 1.

        if i > 0:
            if output_list[i][2].lower() != output_list[i - 1][2].lower():
                true_positive.append(current_positive / total_positive)
                false_positive.append(current_negative / total_negative)

    true_positive.append(1.)
    false_positive.append(1.)

    try:
        import matplotlib.pyplot as plt
        plt.plot(false_positive, true_positive)
        plt.xlabel('false positive')
        plt.ylabel('true positive')
        plt.title('ROC curve')
        plt.show()
    finally:
        pass
