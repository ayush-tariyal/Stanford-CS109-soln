from random import randint
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


sum_S = 0
iteration = 100000  # set iterations

# stores player's numbers
p1 = []
p2 = []

# stores no. of "Wins" by the player
p1_win = []
p2_win = []

# stores the win count at each iteration
p1_count = []
p2_count = []

# win counters
p1_win_count = 0
p2_win_count = 0

while iteration > 0:
    while sum_S >= 0:
        rand = randint(1, 100)
        sum_S += rand
        p1.append(rand)
        if sum_S > 100:
            break

    while sum_S > 100:
        rand = randint(1, 100)
        sum_S += rand
        p2.append(rand)
        if sum_S > 200:
            break

    if p1[-1] > p2[-1]:
        p1_win.append("Win")
        p1_win_count += 1
        p1_count.append(p1_win_count)
        p2_count.append(p2_win_count)
    else:
        p2_win.append("Win")
        p2_win_count += 1
        p2_count.append(p2_win_count)
        p1_count.append(p1_win_count)

    sum_S -= sum_S
    p1.clear()
    p2.clear()
    iteration -= 1


print(
    f"Probability of first player winning = {len(p1_win)/(len(p1_win) + len(p2_win))}"
)
print(
    f"Probability of second player winning = {len(p2_win)/(len(p1_win) + len(p2_win))}"
)

#
game_df = pd.DataFrame({"P1_Win": p1_count, "P2_Win": p2_count})

# Plotting the distribution of Player 1 and 2
with sns.axes_style("darkgrid"):
    sns.lineplot(game_df)

plt.title("Player 1 vs Player 2")
plt.show()
