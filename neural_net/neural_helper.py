
def accuracy(output, data_rows):
    correct = 0.
    for row in data_rows:
        if output[str(row)][1].lower() == output[str(row)][2].lower():
            correct += 1
    # print correct
    # print len(output)
    # print correct / len(output)
    return correct / len(output)