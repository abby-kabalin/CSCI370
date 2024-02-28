# Import Stmts
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------------------------
# Montana Players that played over 10 minutes
# IDs are built by myself

team = {
    "Aanen Moody": 0,
    "Dischon Thomas": 1,
    "Josh Vasquez": 2,
    "Laolu Oke": 3,
    "Brandon Whitney": 4,
    "Jaxon Nap": 5,
}

for i in team:
    print("Player ID: %8d %s" % (team[i], i))

gameStats = pd.read_excel("MTplayers.xlsx", "Sheet1")


gameStats["TS%"] = (0.5 * gameStats["PTS"]) / (
    gameStats["FGA"] + 0.475 * gameStats["FTA"]
)


gameStats["%SO"] = gameStats["FGA"] + 0.475 * gameStats["FTA"]
print(gameStats)

seasonStats = pd.read_excel("MTplayers.xlsx", "Sheet2")

seasonStats["Season_TS%"] = (0.5 * seasonStats["PTS"]) / (
    seasonStats["FGA"] + 0.475 * seasonStats["FTA"]
)

seasonStats["Szn_%SO_AVG"] = (
    seasonStats["FGA"] + 0.475 * seasonStats["FTA"]
) / seasonStats["GP"]
print(seasonStats)

# ----------------------------------------------------------------------------------------------------------
# Plotting True Shooting Percentage vs % Shot Opportunities for each player

name = gameStats["Player"]

fig, axs = plt.subplots(2, 3, constrained_layout=True, figsize=(10, 10))
fig.suptitle("True Shooting Percentage vs % Shot Opportunities")

for i in range(2):
    for j in range(3):
        if i * 3 + j < len(team):
            tsp = gameStats.loc[i * 3 + j, "TS%"]
            so = gameStats.loc[i * 3 + j, "%SO"]
            seasonTSP = seasonStats.loc[i * 3 + j, "Season_TS%"]
            seasonSO = seasonStats.loc[i * 3 + j, "Szn_%SO_AVG"]
            axs[i, j].bar(
                ["TS%", "%SO", "Season_TS%", "Szn_%SO_AVG"],
                [tsp, so, seasonTSP, seasonSO],
                color=["blue", "gold", "grey", "maroon"],
            )

            axs[i, j].set_title(name[i * 3 + j])
            if tsp > seasonTSP:
                axs[i, j].arrow(
                    0,
                    tsp,
                    2,
                    seasonTSP - tsp,
                    head_width=0.1,
                    head_length=0.2,
                    fc="red",
                    ec="red",
                    label="Game better than season",
                )
                axs[i, j].legend()
            elif tsp < seasonTSP:
                axs[i, j].arrow(
                    0,
                    tsp,
                    2,
                    seasonTSP - tsp,
                    head_width=0.1,
                    head_length=0.2,
                    fc="green",
                    ec="green",
                    label="Season better than game",
                )
                axs[i, j].legend()
            if so > seasonSO:
                axs[i, j].arrow(
                    1,
                    so,
                    2,
                    seasonSO - so,
                    head_width=0.1,
                    head_length=0.2,
                    fc="red",
                    ec="red",
                    label="Game better than season",
                )
                axs[i, j].legend()
            elif so < seasonSO:
                axs[i, j].arrow(
                    1,
                    so,
                    2,
                    seasonSO - so,
                    head_width=0.1,
                    head_length=0.2,
                    fc="green",
                    ec="green",
                    label="Season better than game",
                )
                axs[i, j].legend()
            axs[i, j].bar_label(axs[i, j].containers[0], fmt="%.2f", label_type="edge")
plt.show()
