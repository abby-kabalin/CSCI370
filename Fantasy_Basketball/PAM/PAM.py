# Abby Kabalin
# 3/5/24
# Calculate the points above median for each Sacramento Kings
# player.
# ----------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import tabulate

# ----------------------------------------------------------------------
# Read in the data

kings = pd.read_excel("KingsData.xlsx")
print(kings)

players = kings["Player"]

print(players)
# ----------------------------------------------------------------------
# Calculate the points above median for each player
# PAM = points - .96 x (FGA + 0.475 x FTA)

points = kings["PTS"]
FGA = kings["FGA"]
FTA = kings["FTA"]
kings["PAM"] = kings["PTS"] - 0.96 * (kings["FGA"] + 0.475 * kings["FTA"])
print(kings)

# ----------------------------------------------------------------------
# record points above median for each player in a table

table = pd.DataFrame({"Player": kings["Player"], "PAM": kings["PAM"]})
print(tabulate.tabulate(table, headers="keys", tablefmt="fancy_grid"))
# print(tabulate(table, headers="keys", tablefmt="fancy_grid"))

# ----------------------------------------------------------------------
# Plot on line graph

plt.plot(kings["Player"], kings["PAM"])
plt.title("Points Above Median")
plt.xlabel("Player")
plt.ylabel("PAM")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
# ----------------------------------------------------------------------
# Analysis
# The graph shows the points above median for each player.
# The player with the highest PAM is De'Aaron Fox, and the player with
# the lowest PAM is Justin James. This graph shows the value of each player
# in terms of points above median.

# This calculation could be potentially more valuable in the NBA than in
# college basketball, considering contracts and a lot more money is on the line.

# These calculations tell me that on average De'Aaron Fox is the most valuable
# in terms of point scoring, which also tells me as a defensive coach that he would
# be the main focus of the defense.
