import numpy as np
from scipy.stats import beta

# prior beta distribution of the two drugs
drug = [[1, 1], [1, 1]]


def sampleBeta(a, b):
    return beta.rvs(a, b)


def argmax(s_list):
    return s_list.index(np.max(s_list))


def giveDrug(i, d_list):
    # set probability
    if d_list[i] > 0.6:
        drug[i][0] += 1
    else:
        drug[i][1] += 1


for i in range(100):
    prob_list = [
        sampleBeta(drug[0][0], drug[0][1]),
        sampleBeta(drug[1][0], drug[1][1]),
    ]
    argm = argmax(prob_list)
    giveDrug(argm, prob_list)

# beta distribution after 100 iterations
print(drug)
