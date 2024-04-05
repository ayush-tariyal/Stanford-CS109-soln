import numpy as np

# csv to numpy 2D array
bats_data = np.genfromtxt(r"pset2\bats.csv", delimiter=",", dtype="str")

# counters
T_count = 0
G1_count = 0
G2_count = 0
G3_count = 0
G4_count = 0
G5_count = 0

T_and_G1_count = 0
T_and_G2_count = 0
T_and_G3_count = 0
T_and_G4_count = 0
T_and_G5_count = 0

for row in bats_data:
    if row[0] == "True":
        G1_count += 1
    if row[1] == "True":
        G2_count += 1
    if row[2] == "True":
        G3_count += 1
    if row[3] == "True":
        G4_count += 1
    if row[4] == "True":
        G5_count += 1
    if row[5] == "True":
        T_count += 1

    if row[0] == "True" and row[5] == "True":
        T_and_G1_count += 1
    if row[1] == "True" and row[5] == "True":
        T_and_G2_count += 1
    if row[2] == "True" and row[5] == "True":
        T_and_G3_count += 1
    if row[3] == "True" and row[5] == "True":
        T_and_G4_count += 1
    if row[4] == "True" and row[5] == "True":
        T_and_G5_count += 1

# calc probabilities
T_prob = T_count / bats_data.shape[0]
G1_prob = G1_count / bats_data.shape[0]
G2_prob = G2_count / bats_data.shape[0]
G3_prob = G3_count / bats_data.shape[0]
G4_prob = G4_count / bats_data.shape[0]
G5_prob = G5_count / bats_data.shape[0]

T_and_G1_prob = T_and_G1_count / bats_data.shape[0]
T_and_G2_prob = T_and_G2_count / bats_data.shape[0]
T_and_G3_prob = T_and_G3_count / bats_data.shape[0]
T_and_G4_prob = T_and_G4_count / bats_data.shape[0]
T_and_G5_prob = T_and_G5_count / bats_data.shape[0]


print(f"p(G1): {G1_prob}")
print(f"p(G2): {G2_prob}")
print(f"p(G3): {G3_prob}")
print(f"p(G4): {G4_prob}")
print(f"p(G5): {G5_prob}")
print(f"p(T): {T_prob}")

print(f"p(T and G1): {T_and_G1_prob}, p(T)*p(G1): {T_prob * G1_prob}")
print(f"p(T and G2): {T_and_G2_prob}, p(T)*p(G2): {T_prob * G2_prob}")
print(f"p(T and G3): {T_and_G3_prob}, p(T)*p(G3): {T_prob * G3_prob}")
print(f"p(T and G4): {T_and_G4_prob}, p(T)*p(G4): {T_prob * G4_prob}")
print(f"p(T and G5): {T_and_G5_prob}, p(T)*p(G5): {T_prob * G5_prob}")

print(f"p(T|G3): {T_and_G3_prob * G3_prob}")
print(f"p(T|G4): {T_and_G4_prob * G4_prob}")
print(f"p(T|G5): {T_and_G5_prob * G5_prob}")
