import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
import seaborn as sns
import math
import copy

ITERATION = 100000

# csv to DataFrame
data = pd.read_csv(r"pset5\learningOutcomes.csv")
bg_data = pd.read_csv(r"pset5\background.csv")

# DataFrame to list
data_list = data.values.tolist()
bg_list = bg_data.values.tolist()

# Activity lists
act_1 = [item[-1] for item in data_list if item[-2] == "activity1"]
act_2 = [item[-1] for item in data_list if item[-2] == "activity2"]


def filterBg(activity, bg):
    new_list = []
    for item in data_list:
        for ele in bg_list:
            if item[0] == ele[0] and ele[1] == bg:
                new_list.append(item)

    act_list = [item[-1] for item in new_list if item[-2] == activity]
    return act_list


# Student backgrounds
# Less exp
less_exp_act1 = filterBg("activity1", "less")
less_exp_act2 = filterBg("activity2", "less")

# Avg exp
avg_exp_act1 = filterBg("activity1", "average")
avg_exp_act2 = filterBg("activity2", "average")

# More exp
more_exp_act1 = filterBg("activity1", "more")
more_exp_act2 = filterBg("activity2", "more")


def calcSampleMean(sample):
    return np.mean(sample)


def resample(total_pol, length):
    return np.random.choice(total_pol, length, replace=True)


def visualizeHistplot(data):
    hist_data = pd.DataFrame(data)
    with sns.axes_style("darkgrid"):
        sns.histplot(hist_data, bins=50)

    plt.ylabel("Bootstrap Iterations")
    plt.xlabel("Difference in Sample Mean")
    plt.show()


# bootstrapping
def bootstrap(pop1, pop2, difference):
    total_pop = copy.deepcopy(pop1)
    total_pop.extend(pop2)

    diff_greater_than_count = 0
    vis_distribution = []

    for i in tqdm(range(ITERATION)):
        sample1 = resample(total_pop, len(pop1))
        sample2 = resample(total_pop, len(pop2))
        s_mean1 = calcSampleMean(sample1)
        s_mean2 = calcSampleMean(sample2)

        diff = abs(s_mean1 - s_mean2)
        vis_distribution.append(diff)

        if diff >= difference:
            diff_greater_than_count += 1

    p_value = diff_greater_than_count / ITERATION
    print(f"Difference in Sample Mean: {difference}")
    print(f"P-Value for the observed difference in mean: {p_value}")

    visualizeHistplot(vis_distribution)


bootstrap(act_1, act_2, abs(calcSampleMean(act_1) - calcSampleMean(act_2)))
bootstrap(
    more_exp_act1,
    more_exp_act2,
    abs(calcSampleMean(more_exp_act1) - calcSampleMean(more_exp_act2)),
)
