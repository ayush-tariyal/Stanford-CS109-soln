import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm
from tqdm import tqdm
import pandas as pd
import seaborn as sns
import plotly.express as px
import math

ITERATIONS = 100000
MEAN = 50
VARIANCE = 100 / 12


def sum100Uniform():
    total = sum(uniform.rvs(0, 1) for _ in range(100))
    return round(total)


def pltHistplot(data):
    hist_data = pd.DataFrame(data)
    with sns.axes_style("darkgrid"):
        sns.histplot(hist_data, bins=40)

    plt.show()


def simulateUniform():
    sim_total = [sum100Uniform() for i in tqdm(range(ITERATIONS))]
    return sim_total


def pltBar(simulation_total):
    x_axis, y_axis = np.unique(simulation_total, return_counts=True)
    data = pd.DataFrame({"Values": x_axis, "Probability": y_axis / ITERATIONS})

    fig = px.bar(data, x="Values", y="Probability", color="Probability")
    fig.show()


def findProb():
    print(
        norm.cdf(48.5, MEAN, math.sqrt(VARIANCE))
        - norm.cdf(47.5, MEAN, math.sqrt(VARIANCE))
    )


pltBar(simulateUniform())
findProb()
