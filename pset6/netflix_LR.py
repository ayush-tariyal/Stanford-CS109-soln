import numpy as np
from tqdm import tqdm
from naive_bayes_algo import txtToNpList, checkAccuracy
from logistic_regression_algo import sigmoidFunction, optimization, predictingOutcomes

ITERATION = 10000
LEARNING_RATE = 0.0001

netflix_train_list = txtToNpList(r"pset6\netflix-train.txt")
netflix_test_list = txtToNpList(r"pset6\netflix-test.txt")

parameters = optimization(netflix_train_list, LEARNING_RATE, ITERATION)

output = predictingOutcomes(netflix_test_list, parameters)

checkAccuracy(output, netflix_test_list)
