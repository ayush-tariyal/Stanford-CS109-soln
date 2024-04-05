import numpy as np
from scipy.stats import binom
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from random import random, choice, uniform
import math


# binomial distribution
def simulateBinomial(n, p):
    s = [sum(random() < p for _ in range(n)) for _ in range(100)]
    print(s)


# geometric distribution
def simulateGeometric(p):
    count = 0
    c_list = []
    for _ in range(20):
        while True:
            if random() < p:
                count += 1
            else:
                c_list.append(count)
                count = 0
                break

    print(c_list)

    # another way
    # s = [sum(1 for _ in iter(lambda: random() > p, True)) for _ in range(20)]
    # print(s)


# hypergeometric distribution
def simulateHyperGeometric(N, K, n):
    s = [
        sum(random.choice([True] * K + [False] * (N - K)) for _ in range(n))
        for _ in range(1000)
    ]
    print(s)


# poisson distribution
def simulatePoisson(lam):
    s = [sum(random() < lam / 60000 for _ in range(60000)) for _ in range(10000)]
    print(s)
    pssn_df = pd.DataFrame(s)
    with sns.axes_style("darkgrid"):
        # sns.histplot(data=bin_df, bins=15)
        sns.displot(data=pssn_df, bins=15)
    plt.title("Poisson Distribution")
    plt.show()


# another way
lambda_ = 3.1


def poisson(lambda_):
    L = math.exp(-lambda_)
    k = 0
    p = 1
    while p > L:
        k += 1
        p *= uniform(0, 1)
    return k - 1


# s = [poisson(lambda_) for _ in range(10000)]
# print(s)


# exponential distribution
def simulateExponential(lam):
    pass
