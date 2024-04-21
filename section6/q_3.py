import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import copy
from tqdm import tqdm
import pandas as pd

ITERATION = 100000
OBSERVED_DIFF = 3

isl_A = [
    13,
    12,
    7,
    16,
    9,
    11,
    7,
    10,
    9,
    8,
    9,
    7,
    16,
    7,
    9,
    8,
    13,
    10,
    11,
    9,
    13,
    13,
    10,
    10,
    9,
    7,
    7,
    6,
    7,
    8,
    12,
    13,
    9,
    6,
    9,
    11,
    10,
    8,
    12,
    10,
    9,
    10,
    8,
    14,
    13,
    13,
    10,
    11,
    12,
    9,
]

isl_B = [
    8,
    8,
    16,
    16,
    9,
    13,
    14,
    13,
    10,
    12,
    10,
    6,
    14,
    8,
    13,
    14,
    7,
    13,
    7,
    8,
    4,
    11,
    7,
    12,
    8,
    9,
    12,
    8,
    11,
    10,
    12,
    6,
    10,
    15,
    11,
    12,
    3,
    8,
    11,
    10,
    10,
    8,
    12,
    8,
    11,
    6,
    7,
    10,
    8,
    5,
]


def resample(total_pol, length):
    return np.random.choice(total_pol, length, replace=True)


def calcSampleVariance(sample):
    s_mean = np.mean(sample)
    summation = sum((item - s_mean) ** 2 for item in sample)
    return summation / (len(sample) - 1)


def visualizeHistplot(data):
    hist_data = pd.DataFrame(data)
    with sns.axes_style("darkgrid"):
        sns.histplot(hist_data, bins=50)

    plt.ylabel("Bootstrap Iterations")
    plt.xlabel("Difference in Sample Variance")
    plt.show()


def bootstrap(pop1, pop2):
    total_pop = copy.deepcopy(pop1)
    total_pop.extend(pop2)

    diff_greater_than_count = 0
    vis_distribution = []

    for i in tqdm(range(ITERATION)):
        sample1 = resample(total_pop, len(pop1))
        sample2 = resample(total_pop, len(pop2))
        s_variance1 = calcSampleVariance(sample1)
        s_variance2 = calcSampleVariance(sample2)

        diff = abs(s_variance1 - s_variance2)
        vis_distribution.append(diff)

        if diff >= OBSERVED_DIFF:
            diff_greater_than_count += 1

    p_value = diff_greater_than_count / ITERATION
    print(p_value)

    visualizeHistplot(vis_distribution)


bootstrap(isl_A, isl_B)
