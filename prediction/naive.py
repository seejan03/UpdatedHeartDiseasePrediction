import math
import random
import csv

# the categorical class names are changed to numeric data
# eg: yes and no encoded to 1 and 0
def encode_class(mydata):
    classes = []
    for i in range(len(mydata)):
        # print("Seejan",mydata[i][-1])
        if mydata[i][-1] not in classes:
            classes.append(mydata[i][-1])

    for i in range(len(classes)):
        for j in range(len(mydata)):
            if mydata[j][-1] == classes[i]:
                mydata[j][-1] = i

    return mydata


# Splitting the data
def splitting(mydata, ratio):
    train_num = int(len(mydata) * ratio)
    # print(train_num)
    train = []
    # initially testset will have all the dataset
    test = list(mydata)

    while len(train) < train_num:
        # index generated randomly from range 0
        # to length of testset
        index = random.randrange(len(test))
        # print(index)
        # from testset, pop data rows and put it in train
        train.append(test.pop(index))
    # print(index)
    return train, test


# Group the data rows under each class yes or
# no in dictionary eg: dict[yes] and dict[no]
def groupUnderClass(mydata):
    dict = {}
    for i in range(len(mydata)):
        if (mydata[i][-1] not in dict):
            dict[mydata[i][-1]] = []
        dict[mydata[i][-1]].append(mydata[i])
        # print("Kritika",dict[mydata[i][-1]])
    return dict


# Calculating Mean
def mean(numbers):
    return sum(numbers) / float(len(numbers))


# Calculating Standard Deviation
def std_dev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
    return math.sqrt(variance)


def MeanAndStdDev(mydata):
    info = [(mean(attribute), std_dev(attribute)) for attribute in zip(*mydata)]
    # eg: list = [ [a, b, c], [m, n, o], [x, y, z]]
    # here mean of 1st attribute =(a + m+x), mean of 2nd attribute = (b + n+y)/3
    # delete summaries of last class
    del info[-1]
    return info


# find Mean and Standard Deviation under each class
def MeanAndStdDevForClass(mydata):
    info = {}
    dict = groupUnderClass(mydata)
    # print(dict)
    for classValue, instances in dict.items():
        info[classValue] = MeanAndStdDev(instances)
    return info


# Calculate Gaussian Probability Density Function
def calculateGaussianProbability(x, mean, stdev):
    expo = (math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2)))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * expo


# Calculate Class Probabilities
def calculateClassProbabilities(info, test):
    probabilities = {}
    for classValue, classSummaries in info.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, std_dev = classSummaries[i]
            x = test[i]
            probabilities[classValue] *= calculateGaussianProbability(x, mean, std_dev)
    return probabilities


# Make prediction - highe
# st probability is the prediction
def predict(info, test):
    probabilities = calculateClassProbabilities(info, test)
    bestLabel, bestProb = None, -1
    for classValue, probability in probabilities.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel


# returns predictions for a set of examples
def getPredictions(info, test):
    predictions = []
    for i in range(len(test)):
        result = predict(info, test[i])
        predictions.append(result)
    return predictions


# Accuracy score
def accuracy_rate(test, predictions):
    correct = 0
    for i in range(len(test)):
        if test[i][-1] == predictions[i]:
            correct += 1
    return (correct / float(len(test))) * 100.0


def make_prediction(data):
    # driver code

    # add the data path in your system
    filename = "C:\\Users\seeja\OneDrive\Desktop\HeartDiseasePrediction-main\HeartDiseasePrediction-main\prediction\data.csv"

    # load the file and store it in mydata list
    mydata = csv.reader(open(filename, "r"))
    mydata = list(mydata)
    mydata = encode_class(mydata)

    for i in range(len(mydata)):
        mydata[i] = [float(x) for x in mydata[i]]
    # # split ratio = 0.8
    # # 80% of data is training data and 20% is test data used for testing
    ratio = 0.8
    train_data, test_data = splitting(mydata, ratio)
    # print(test_data)
    # print('Total number of examples are: ', len(mydata))
    # print('Out of these, training examples are: ', len(train_data))
    # print("Test examples are: ", len(test_data))
    # # prepare model
    info = MeanAndStdDevForClass(mydata)

    # test model
    predictions = getPredictions(info, test_data)
    accuracy = accuracy_rate(test_data, predictions)

    print("Accuracy of your model is: ", accuracy)

    # from sklearn.metrics import accuracy_score
    # test = accuracy_score(test_data, predictions);

    predict = getPredictions(info, data)

    return int(predict[0]) , accuracy

data = [
        [52, 1, 0, 128, 255, 0, 1, 161, 1, 0, 2, 1, 3]
    ]
print(make_prediction(data))

