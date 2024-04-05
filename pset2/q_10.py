import numpy as np
import pandas as pd

obs_given_no_location = 15 / 16

# converting csv files to numpy 2D arrays
prior_data = np.genfromtxt(r"pset2\prior.csv", delimiter=",", dtype="float")
print(prior_data)

conditional_data = np.genfromtxt(r"pset2\conditional.csv", delimiter=",", dtype="float")
print(conditional_data)

# calc probability
new_probability = (conditional_data * prior_data) / (
    (conditional_data * prior_data) + (obs_given_no_location * (1 - prior_data))
)

print(new_probability)
