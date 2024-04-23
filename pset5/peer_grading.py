import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
import seaborn as sns

ITERATIONS = 100000
LENGTH = 5

# converting csv to lists
data = pd.read_csv(r"pset5\peerGrades.csv")
d_list = [ele[0] for ele in data.values.tolist()]


def calcSampleMean(sample):
    return np.mean(sample)


def calcSampleMedian(sample):
    return np.median(sample)


def calcSampleVariance(sample):
    s_mean = np.mean(sample)
    summation = sum((item - s_mean) ** 2 for item in sample)
    return summation / (len(sample) - 1)


def pltHistplot(data):
    hist_data = pd.DataFrame(data)
    with sns.axes_style("darkgrid"):
        sns.histplot(hist_data, bins=40)

    plt.show()


def resample(total_sample, length):
    return np.random.choice(total_sample, length, replace=True)


def simulate(sample_data):
    vis_mean = []
    vis_median = []
    for i in tqdm(range(ITERATIONS)):
        sample = resample(sample_data, LENGTH)
        s_mean = calcSampleMean(sample)
        s_median = calcSampleMedian(sample)

        vis_mean.append(s_mean)
        vis_median.append(s_median)

    print(f"Variance of the Mean: {calcSampleVariance(vis_mean)}")
    print(f"Variance of the Median: {calcSampleVariance(vis_median)}")

    pltHistplot(vis_mean)
    pltHistplot(vis_median)


print(calcSampleMean(d_list))
print(calcSampleMedian(d_list))
simulate(d_list)
