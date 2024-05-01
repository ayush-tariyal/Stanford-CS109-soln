import numpy as np
from tqdm import tqdm
from naive_bayes_algo import txtToNpList, checkAccuracy

"""This Logistic Regression Classifier assumes that the input data is in binary i.e. 1s & 0s. The input data should be in a 'txt' file. 
Input data format: x1 x2 .... xn: y


    Returns:
        Predicts the output from the given data, using Gradient Ascent
        Returns the accuracy of the classifier
"""

ITERATION = 10000
LEARNING_RATE = 0.0001


# sigmoid function
def sigmoidFunction(value):
    return 1 / (1 + np.exp(-value))


# Gradient Ascent algorithm - calculate parameters
def optimization(data_array, learning_rate, iteration):
    print("optimizing thetas....")
    theta_list = [0 for i in range(len(data_array[0][:-1]))]
    # print(theta_list)
    for i in tqdm(range(iteration)):
        gradient = [0 for i in range(len(data_array[0][:-1]))]
        # print(gradient)
        for item in data_array:
            sig_sum = 1 + sum(
                int(theta_list[i]) * int(item[i]) for i in range(len(item[:-1]))
            )
            # print(sig_sum)
            for i in range(len(theta_list)):
                gradient[i] += int(item[i]) * (int(item[-1]) - sigmoidFunction(sig_sum))
            # print(gradient)

        for i in range(len(theta_list)):
            theta_list[i] += learning_rate * gradient[i]
        # print(theta_list)
    print("finished :)")
    return theta_list


# Predict output(y-cap) using calculated thetas
def predictingOutcomes(test_list, theta_list):
    print("predicting output")
    result_list = []
    for data in test_list:
        sum_y = sum(int(data[i]) * int(theta_list[i]) for i in range(len(theta_list)))
        prob_y1 = sigmoidFunction(sum_y)

        if prob_y1 > 0.5:
            result_list.append(1)
        else:
            result_list.append(0)

    # print(result_list)
    print("finished predicting :)")
    return result_list


train_list = txtToNpList(r"pset6\simple-train.txt")
test_list = txtToNpList(r"pset6\simple-test.txt")

thetas = optimization(train_list, LEARNING_RATE, ITERATION)
# # print(thetas)
y_cap = predictingOutcomes(test_list, thetas)
# # print(sigmoidFunction(0))
checkAccuracy(y_cap, test_list)
