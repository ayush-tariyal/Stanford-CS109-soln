import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from math import sqrt

# converting txt files to lists
with open(r"pset4\personKeyTimingA.txt") as f1:
    file_1 = f1.readlines()
    person_A = [letter.replace("\n", "").split(",")[0] for letter in file_1]

with open(r"pset4\personKeyTimingB.txt") as f2:
    file_2 = f2.readlines()
    person_B = [letter.replace("\n", "").split(",")[0] for letter in file_2]


# returns a list with individual key stroke durations
def keystrokeDuration(person):
    i = len(person) - 1
    while i > 0:
        person[i] = round(float(person[i]) - float(person[i - 1]), 1)
        i -= 1

    person[0] = float(person[0])

    return person


person_A = keystrokeDuration(person_A)
person_B = keystrokeDuration(person_B)


# returns E[X]
def calcExp(person):
    keystroke_duration = sum(item for item in person)
    return keystroke_duration / len(person)


# returns E[X^2]
def calcExp2(person):
    duration_squared = sum(item**2 for item in person)
    return duration_squared / len(person)


# returns Var(X)
def calcVariance(exp, exp2):
    return exp2 - (exp**2)


# plots normal distribution
def plotNormal(mean, std):
    x = np.linspace(-2, 2, 1000)
    plt.plot(
        x,
        norm.pdf(x, mean, std),
        "r-",
        lw=5,
        alpha=0.6,
    )
    plt.title("Normal distribution")
    plt.show()


print(
    f"E[X] of Person A: {calcExp(person_A)}\nE[X2] of Person A: {calcExp2(person_A)}\nVar(X): {calcVariance(calcExp(person_A), calcExp2(person_A))}"
)

print(
    f"E[Y] of Person B: {calcExp(person_B)}\nE[Y2] of Person B: {calcExp2(person_B)}\nVar(Y): {calcVariance(calcExp(person_B), calcExp2(person_B))}"
)
