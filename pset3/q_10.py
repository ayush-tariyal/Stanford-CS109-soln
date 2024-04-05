from math import sqrt

# converting txt files to lists
with open(r"pset3\ditherSequence1.txt") as f1:
    file_1 = f1.read()
    f1_list = [item for item in file_1]

with open(r"pset3\ditherSequence2.txt") as f2:
    file_2 = f2.read()
    f2_list = [item for item in file_2]

# sums all the values of "H" or "T"
f1_H_sum = sum(item == "H" for item in f1_list)
f1_T_sum = sum(item == "T" for item in f1_list)
f2_H_sum = sum(item == "H" for item in f2_list)
f2_T_sum = sum(item == "T" for item in f2_list)

print(f"File 1 'H' probability: {f1_H_sum / (f1_H_sum + f1_T_sum)}")
print(f"File 1 'T' probability: {f1_T_sum / (f1_H_sum + f1_T_sum)}")
print(f"File 2 'H' probability: {f2_H_sum / (f2_H_sum + f2_T_sum)}")
print(f"File 2 'T' probability: {f2_T_sum / (f2_H_sum + f2_T_sum)}")

# "H" and "T" probabilities
f1_H_prob = f1_H_sum / (f1_H_sum + f1_T_sum)
f2_H_prob = f2_H_sum / (f2_H_sum + f2_T_sum)

# Variance = np(1 - p)
print(f"Variance of File 1: {300 * f1_H_prob * (1-f1_H_prob)}")
print(f"Variance of File 2: {300 * f2_H_prob * (1-f2_H_prob)}")

# Standard deviation = sqrt(Variance)
print(f"Standard Deviation of File 1: {sqrt(300 * f1_H_prob * (1-f1_H_prob))}")
print(f"Standard Deviation of File 2: {sqrt(300 * f2_H_prob * (1-f2_H_prob))}")
