import pandas as pd
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
import seaborn as sns

# converting csv to DataFrame
titanic_dataset = pd.read_csv(r"pset4\titanic.csv")
new_df = titanic_dataset[["Survived", "Pclass", "Sex", "Age", "Fare"]]
# converting df to list
titanic_list = new_df.values.tolist()


# check for observations in the sample
def check_obs(sample, obs):
    if sample[1:3] == obs:
        return True
    else:
        return False


# returns P(S=1|Obs)
def probSurvivedGivenObs(samples, obs):
    keep_sample = [sample for sample in samples if check_obs(sample, obs)]
    survive_sum = sum(sample[0] == 1 for sample in keep_sample)

    return survive_sum / len(keep_sample)


# returns P(S=1|A<=10, C=3)
# also plots beta distribution
def probChildSurvivedGivenPclass3(samples):
    keep_sample = [sample for sample in samples if sample[1] == 3 and sample[3] <= 10]
    survive_sum = sum(sample[0] == 1 for sample in keep_sample)

    a = survive_sum + 1
    b = len(keep_sample) - survive_sum + 1

    print(f"Expected probability of survival using Beta Distribution: {a / (a + b)}")

    x = np.linspace(beta.ppf(0.01, a, b), beta.ppf(0.99, a, b), 100)

    plt.plot(x, beta.pdf(x, a, b), "r-", lw=5, alpha=0.6, label="beta pdf")
    plt.title("Beta Distribution")
    plt.show()


# returns E[X|C]
def expectedFare(samples, pclass):
    keep_sample = [sample for sample in samples if sample[1] == pclass]
    total_fare = sum(sample[4] for sample in keep_sample)

    return total_fare / len(keep_sample)


p_sur_given_female_1 = probSurvivedGivenObs(titanic_list, [1, "female"])
p_sur_given_female_2 = probSurvivedGivenObs(titanic_list, [2, "female"])
p_sur_given_female_3 = probSurvivedGivenObs(titanic_list, [3, "female"])
p_sur_given_male_1 = probSurvivedGivenObs(titanic_list, [1, "male"])
p_sur_given_male_2 = probSurvivedGivenObs(titanic_list, [2, "male"])
p_sur_given_male_3 = probSurvivedGivenObs(titanic_list, [3, "male"])

# print(f"P(S = true | G = female, C = 1): {p_sur_given_female_1}")
# print(f"P(S = true | G = female, C = 2): {p_sur_given_female_2}")
# print(f"P(S = true | G = female, C = 3): {p_sur_given_female_3}")
# print(f"P(S = true | G = male, C = 1): {p_sur_given_male_1}")
# print(f"P(S = true | G = male, C = 2): {p_sur_given_male_2}")
# print(f"P(S = true | G = male, C = 3): {p_sur_given_male_3}")

E_fare_1 = expectedFare(titanic_list, 1)
E_fare_2 = expectedFare(titanic_list, 2)
E_fare_3 = expectedFare(titanic_list, 3)

# print(E_fare_1)
# print(E_fare_2)
# print(E_fare_3)

probChildSurvivedGivenPclass3(titanic_list)
