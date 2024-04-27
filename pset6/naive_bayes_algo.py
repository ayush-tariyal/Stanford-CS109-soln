from math import log
import numpy as np
from tqdm import tqdm

"""This Naive Bayesian Classifier assumes that the input data is in binary i.e. 1s & 0s. The input data should be in a 'txt' file. 
Input data format: x1 x2 .... xn: y


    Returns:
        Predicts the output from the given data, using MAP/MLE
        Returns the accuracy of the classifier
"""


# convert txt files to np array
def txtToNpList(dir_path):
    with open(dir_path) as f1:
        file1 = f1.readlines()
        file_list = np.array(
            [item.replace("\n", "").replace(":", "").split() for item in file1]
        )
    return file_list


# returns the probability of Y = 1/Y = 0 as an array
def probY(tr_lst, method_type):
    sum_y1 = sum(1 for item in tr_lst if item[-1] == "1")
    if method_type == "MAP":
        sum_y1 += 1
        return [1 - (sum_y1 / (len(tr_lst) + 2)), sum_y1 / (len(tr_lst) + 2)]
    return [1 - (sum_y1 / len(tr_lst)), sum_y1 / len(tr_lst)]


# returns parameters using MLE or MAP
def calculatingParameters(tr_lst, method_type):
    print("calculating parameters....")
    param_list = []
    sum_y1 = sum(1 for item in tr_lst if item[-1] == "1")
    sum_y0 = len(tr_lst) - sum_y1
    if method_type == "MAP":
        sum_y0 += 2
        sum_y1 += 2
    for i in tqdm(range(len(tr_lst[0][:-1]))):
        X1_Y0 = 0
        X1_Y1 = 0
        X0_Y0 = 0
        X0_Y1 = 0
        if method_type == "MAP":
            X1_Y0 += 1
            X1_Y1 += 1
            X0_Y0 += 1
            X0_Y1 += 1
        new_list = tr_lst[:, i]
        for j in range(len(new_list)):
            if new_list[j] == "1" and tr_lst[:, -1][j] == "0":
                X1_Y0 += 1
            elif new_list[j] == "0" and tr_lst[:, -1][j] == "0":
                X0_Y0 += 1
            elif new_list[j] == "1" and tr_lst[:, -1][j] == "1":
                X1_Y1 += 1
            else:
                X0_Y1 += 1

        param_list.append(
            [X0_Y0 / sum_y0, X1_Y0 / sum_y0, X0_Y1 / sum_y1, X1_Y1 / sum_y1]
        )
    print("finished :)")
    print(f"Parameters using {method_type}: {param_list}")

    return param_list


# returns the index of the maximum in an array
def argmax(product_lst):
    return product_lst.index(np.max(product_lst))


# returns the predicted output
# log sum only works for MAP or when params != 0
def predictingOutput(test_list, params_lst, probY_list):
    print("predicting output.....")
    result_list = []
    test_list = test_list[:, :-1].tolist()
    for i in tqdm(range(1)):
        for item in test_list:
            log_sum_XiY0 = log(probY_list[0])
            log_sum_XiY1 = log(probY_list[1])
            for ele in item:
                if ele == "0":
                    log_sum_XiY0 += log(params_lst[item.index(ele)][0])
                    log_sum_XiY1 += log(params_lst[item.index(ele)][2])
                else:
                    log_sum_XiY0 += log(params_lst[item.index(ele)][1])
                    log_sum_XiY1 += log(params_lst[item.index(ele)][3])

            # print([log_sum_XiY0, log_sum_XiY1])
            if argmax([log_sum_XiY0, log_sum_XiY1]) == 0:
                result_list.append(0)
            else:
                result_list.append(1)
    print("finished predicting :)")
    # print(f"Predicted outcomes: {result_list}")

    return result_list


# Check the accuracy of the prediction
def checkAccuracy(predicted_list, test_list):
    test_list = [int(item) for item in test_list[:, -1]]
    correctly_predict_0 = sum(
        1 for i in range(len(test_list)) if test_list[i] == 0 and predicted_list[i] == 0
    )
    correctly_predict_1 = sum(
        1 for i in range(len(test_list)) if test_list[i] == 1 and predicted_list[i] == 1
    )
    class_type, class_count = np.unique(test_list, return_counts=True)

    print(
        f"Class 0: tested {class_count[0]}, correctly classified {correctly_predict_0}\nClass 1: tested {class_count[1]}, correctly classified {correctly_predict_1}\nOverall: tested {class_count[0] + class_count[1]}, correctly classified {correctly_predict_0 + correctly_predict_1}\nAccuracy: {(correctly_predict_0 + correctly_predict_1)/(class_count[0] + class_count[1])}"
    )


train_list = txtToNpList(r"pset6\simple-train.txt")
test_list = txtToNpList(r"pset6\simple-test.txt")
# print(test_list)
params = calculatingParameters(train_list, "MAP")
# print(params)
prediction = predictingOutput(test_list, params, probY(train_list, "MAP"))
# print(test_list[:, -1])
checkAccuracy(prediction, test_list)
