import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

coin = ["H", "T"]
head = []
tail = []

head_count = []
tail_count = []

# head and tail counter
h = 0
t = 0

a = 100  # set no. of iterations
while a > 0:
    event = random.choice(coin)
    if event == "H":
        head.append(event)
        tail_count.append(t)
        h += 1
        head_count.append(h)
    else:
        tail.append(event)
        head_count.append(h)
        t += 1
        tail_count.append(t)
    a -= 1


print(f"Probability of head: {len(head)/(len(head) + len(tail))}")
print(f"Probability of tail: {len(tail)/(len(head) + len(tail))}")

# converting list to df
coin_df = pd.DataFrame({"No. of Heads": head_count, "No. of Tails": tail_count})

# with sns.axes_style("darkgrid"):
#     sns.lineplot(coin_df, x="No. of Heads", y="No. of Tails")

# plots the distribution of no. of heads and tails
with sns.axes_style("darkgrid"):
    sns.lineplot(coin_df)

plt.title("Heads vs Tails")
plt.show()
