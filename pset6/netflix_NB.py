from math import log
import numpy as np
from tqdm import tqdm
from naive_bayes_algo import (
    txtToNpList,
    probY,
    calculatingParameters,
    argmax,
    predictingOutput,
    checkAccuracy,
)

netflix_train_list = txtToNpList(r"pset6\netflix-train.txt")
netflix_test_list = txtToNpList(r"pset6\netflix-test.txt")
# print(netflix_train_list)
print(probY(netflix_train_list, "MLE"))
params = calculatingParameters(netflix_train_list, "MLE")
# print(len(params))
prediction = predictingOutput(
    netflix_test_list, params, probY(netflix_train_list, "MLE")
)
checkAccuracy(prediction, netflix_test_list)
