# Abby Kabalin
# 2/20/24
# This file contains the my FantasyAnalyzer, which is used to analyze fantasy basketball data.
# I brute-forced the EFG, Usage Rate, Fantasy Points Per Minute, and Games Played Per Month calculations.
# ----------------------------------------------------------------------------------------
# Imports
import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams as teams
from nba_api.stats.static import players as players
from nba_api.stats.endpoints import commonplayerinfo as cpi
from nba_api.stats.endpoints import playergamelog

# Printing Runtime Disclaimer to Terminal
print("Runtime Disclaimer: This program may take a few minutes to run.")
# ----------------------------------------------------------------------------------------
# pulling players
nba_players = players.get_players()
df_players = pd.DataFrame(nba_players)

# ----------------------------------------------------------------------------------------
# pulling players from my fantasy team
my_players = []

for player in nba_players:
    if player["full_name"] == "De'Aaron Fox":
        my_players.append(player)
    if player["full_name"] == "Brandin Podziemski":
        my_players.append(player)
    if player["full_name"] == "Cameron Johnson":
        my_players.append(player)
    if player["full_name"] == "Isaiah Hartenstein":
        my_players.append(player)
    if player["full_name"] == "Jamal Murray":
        my_players.append(player)
    if player["full_name"] == "Chet Holmgren":
        my_players.append(player)
    if player["full_name"] == "Dereck Lively II":
        my_players.append(player)
    if player["full_name"] == "Precious Achiuwa":
        my_players.append(player)
    if player["full_name"] == "Bennedict Mathurin":
        my_players.append(player)
    if player["full_name"] == "GG Jackson":
        my_players.append(player)
    if player["full_name"] == "Ayo Dosunmu":
        my_players.append(player)
    if player["full_name"] == "Marvin Bagley III":
        my_players.append(player)

df_my_players = pd.DataFrame(my_players)

# ----------------------------------------------------------------------------------------
# creating a dataframe of player ids and names

team_vals = []
for i in my_players:
    player_info = cpi.CommonPlayerInfo(player_id=i["id"])
    player_info = player_info.get_data_frames()[0]
    id_name = player_info[["PERSON_ID", "DISPLAY_FIRST_LAST"]]
    team_vals.append(dict(zip(id_name.columns, id_name.values[0])))

team = pd.DataFrame(team_vals)
print(team)

# ----------------------------------------------------------------------------------------
# pulling player game logs

player = team["PERSON_ID"]
name = team["DISPLAY_FIRST_LAST"]

gamelog = []
for i in team["PERSON_ID"]:
    gamelog.append(
        playergamelog.PlayerGameLog(player_id=i, season="2023").get_data_frames()[0]
    )
# ----------------------------------------------------------------------------------------
# Standard Stats

for category in gamelog[0].columns[6:19]:
    print(category)

    player = team["PERSON_ID"]
    name = team["DISPLAY_FIRST_LAST"]

    fig, axs = plt.subplots(3, 4, constrained_layout=True)
    fig.suptitle("Fantasy Analyzer: " + category)
    for i in range(4):
        for j in range(4):
            if i * 4 + j < len(player):
                pts = gamelog[i * 4 + j][category]  # Convert numpy array to list
                axs[i, j].plot(pts, color="pink")
                axs[i, j].set_title(name[i * 4 + j])
                axs[i, j].set_ylabel([category])
                axs[i, j].get_ylim()
                axs[i, j].set_xticks([])


# ----------------------------------------------------------------------------------------
# Calculate and plot EFG

gamelog[0]["EFG"] = (gamelog[0]["FGM"] + 0.5 * gamelog[0]["FG3M"]) / gamelog[0]["FGA"]
gamelog[1]["EFG"] = (gamelog[1]["FGM"] + 0.5 * gamelog[1]["FG3M"]) / gamelog[1]["FGA"]
gamelog[2]["EFG"] = (gamelog[2]["FGM"] + 0.5 * gamelog[2]["FG3M"]) / gamelog[2]["FGA"]
gamelog[3]["EFG"] = (gamelog[3]["FGM"] + 0.5 * gamelog[3]["FG3M"]) / gamelog[3]["FGA"]
gamelog[4]["EFG"] = (gamelog[4]["FGM"] + 0.5 * gamelog[4]["FG3M"]) / gamelog[4]["FGA"]
gamelog[5]["EFG"] = (gamelog[5]["FGM"] + 0.5 * gamelog[5]["FG3M"]) / gamelog[5]["FGA"]
gamelog[6]["EFG"] = (gamelog[6]["FGM"] + 0.5 * gamelog[6]["FG3M"]) / gamelog[6]["FGA"]
gamelog[7]["EFG"] = (gamelog[7]["FGM"] + 0.5 * gamelog[7]["FG3M"]) / gamelog[7]["FGA"]
gamelog[8]["EFG"] = (gamelog[8]["FGM"] + 0.5 * gamelog[8]["FG3M"]) / gamelog[8]["FGA"]
gamelog[9]["EFG"] = (gamelog[9]["FGM"] + 0.5 * gamelog[9]["FG3M"]) / gamelog[9]["FGA"]
gamelog[10]["EFG"] = (gamelog[10]["FGM"] + 0.5 * gamelog[10]["FG3M"]) / gamelog[10][
    "FGA"
]
gamelog[11]["EFG"] = (gamelog[11]["FGM"] + 0.5 * gamelog[11]["FG3M"]) / gamelog[11][
    "FGA"
]

fig, axs = plt.subplots(3, 4, figsize=(11, 11))
fig.suptitle("Fantasy Analyzer: Player EFG")
for i in range(4):
    for j in range(4):
        if i * 4 + j < len(player):
            pts = gamelog[i * 4 + j]["EFG"]
            axs[i, j].plot(pts, color="pink")
            axs[i, j].set_title(name[i * 4 + j])
            axs[i, j].set_ylabel("Player EFG")
            axs[i, j].get_ylim()
            axs[i, j].set_xticks([])


# ----------------------------------------------------------------------------------------
# Calculate and plot Usage Rate

gamelog[0]["USG"] = (gamelog[0]["FTA"] * 0.44) + gamelog[0]["FGA"] + gamelog[0]["TOV"]
gamelog[1]["USG"] = (gamelog[1]["FTA"] * 0.44) + gamelog[1]["FGA"] + gamelog[1]["TOV"]
gamelog[2]["USG"] = (gamelog[2]["FTA"] * 0.44) + gamelog[2]["FGA"] + gamelog[2]["TOV"]
gamelog[3]["USG"] = (gamelog[3]["FTA"] * 0.44) + gamelog[3]["FGA"] + gamelog[3]["TOV"]
gamelog[4]["USG"] = (gamelog[4]["FTA"] * 0.44) + gamelog[4]["FGA"] + gamelog[4]["TOV"]
gamelog[5]["USG"] = (gamelog[5]["FTA"] * 0.44) + gamelog[5]["FGA"] + gamelog[5]["TOV"]
gamelog[6]["USG"] = (gamelog[6]["FTA"] * 0.44) + gamelog[6]["FGA"] + gamelog[6]["TOV"]
gamelog[7]["USG"] = (gamelog[7]["FTA"] * 0.44) + gamelog[7]["FGA"] + gamelog[7]["TOV"]
gamelog[8]["USG"] = (gamelog[8]["FTA"] * 0.44) + gamelog[8]["FGA"] + gamelog[8]["TOV"]
gamelog[9]["USG"] = (gamelog[9]["FTA"] * 0.44) + gamelog[9]["FGA"] + gamelog[9]["TOV"]
gamelog[10]["USG"] = (
    (gamelog[10]["FTA"] * 0.44) + gamelog[10]["FGA"] + gamelog[10]["TOV"]
)
gamelog[11]["USG"] = (
    (gamelog[11]["FTA"] * 0.44) + gamelog[11]["FGA"] + gamelog[11]["TOV"]
)

fig, axs = plt.subplots(3, 4, constrained_layout=True)
fig.suptitle("Fantasy Analyzer: Player Usage Rate")
for i in range(4):
    for j in range(4):
        if i * 4 + j < len(player):
            pts = gamelog[i * 4 + j]["USG"]
            axs[i, j].plot(pts, color="pink")
            axs[i, j].set_title(name[i * 4 + j])
            axs[i, j].set_ylabel("Player Usage Rate")
            axs[i, j].get_ylim()
            axs[i, j].set_xticks([])


# ----------------------------------------------------------------------------------------
# Calculate Fantasy Points/Min

gamelog[0]["FPPM"] = (
    (gamelog[0]["FG3M"] * 3)
    + (gamelog[0]["FGM"] * 2)
    + (gamelog[0]["FTM"])
    + (gamelog[0]["REB"] * 1.2)
    + (gamelog[0]["AST"] * 1.5)
    + (gamelog[0]["STL"] * 2)
    + (gamelog[0]["BLK"] * 2)
    - (gamelog[0]["TOV"])
) / gamelog[0]["MIN"]
gamelog[1]["FPPM"] = (
    (gamelog[1]["FG3M"] * 3)
    + (gamelog[1]["FGM"] * 2)
    + (gamelog[1]["FTM"])
    + (gamelog[1]["REB"] * 1.2)
    + (gamelog[1]["AST"] * 1.5)
    + (gamelog[1]["STL"] * 2)
    + (gamelog[1]["BLK"] * 2)
    - (gamelog[1]["TOV"])
) / gamelog[1]["MIN"]
gamelog[2]["FPPM"] = (
    (gamelog[2]["FG3M"] * 3)
    + (gamelog[2]["FGM"] * 2)
    + (gamelog[2]["FTM"])
    + (gamelog[2]["REB"] * 1.2)
    + (gamelog[2]["AST"] * 1.5)
    + (gamelog[2]["STL"] * 2)
    + (gamelog[2]["BLK"] * 2)
    - (gamelog[2]["TOV"])
) / gamelog[2]["MIN"]
gamelog[3]["FPPM"] = (
    (gamelog[3]["FG3M"] * 3)
    + (gamelog[3]["FGM"] * 2)
    + (gamelog[3]["FTM"])
    + (gamelog[3]["REB"] * 1.2)
    + (gamelog[3]["AST"] * 1.5)
    + (gamelog[3]["STL"] * 2)
    + (gamelog[3]["BLK"] * 2)
    - (gamelog[3]["TOV"])
) / gamelog[3]["MIN"]
gamelog[4]["FPPM"] = (
    (gamelog[4]["FG3M"] * 3)
    + (gamelog[4]["FGM"] * 2)
    + (gamelog[4]["FTM"])
    + (gamelog[4]["REB"] * 1.2)
    + (gamelog[4]["AST"] * 1.5)
    + (gamelog[4]["STL"] * 2)
    + (gamelog[4]["BLK"] * 2)
    - (gamelog[4]["TOV"])
) / gamelog[4]["MIN"]
gamelog[5]["FPPM"] = (
    (gamelog[5]["FG3M"] * 3)
    + (gamelog[5]["FGM"] * 2)
    + (gamelog[5]["FTM"])
    + (gamelog[5]["REB"] * 1.2)
    + (gamelog[5]["AST"] * 1.5)
    + (gamelog[5]["STL"] * 2)
    + (gamelog[5]["BLK"] * 2)
    - (gamelog[5]["TOV"])
) / gamelog[5]["MIN"]
gamelog[6]["FPPM"] = (
    (gamelog[6]["FG3M"] * 3)
    + (gamelog[6]["FGM"] * 2)
    + (gamelog[6]["FTM"])
    + (gamelog[6]["REB"] * 1.2)
    + (gamelog[6]["AST"] * 1.5)
    + (gamelog[6]["STL"] * 2)
    + (gamelog[6]["BLK"] * 2)
    - (gamelog[6]["TOV"])
) / gamelog[6]["MIN"]
gamelog[7]["FPPM"] = (
    (gamelog[7]["FG3M"] * 3)
    + (gamelog[7]["FGM"] * 2)
    + (gamelog[7]["FTM"])
    + (gamelog[7]["REB"] * 1.2)
    + (gamelog[7]["AST"] * 1.5)
    + (gamelog[7]["STL"] * 2)
    + (gamelog[7]["BLK"] * 2)
    - (gamelog[7]["TOV"])
) / gamelog[7]["MIN"]
gamelog[8]["FPPM"] = (
    (gamelog[8]["FG3M"] * 3)
    + (gamelog[8]["FGM"] * 2)
    + (gamelog[8]["FTM"])
    + (gamelog[8]["REB"] * 1.2)
    + (gamelog[8]["AST"] * 1.5)
    + (gamelog[8]["STL"] * 2)
    + (gamelog[8]["BLK"] * 2)
    - (gamelog[8]["TOV"])
) / gamelog[8]["MIN"]
gamelog[9]["FPPM"] = (
    (gamelog[9]["FG3M"] * 3)
    + (gamelog[9]["FGM"] * 2)
    + (gamelog[9]["FTM"])
    + (gamelog[9]["REB"] * 1.2)
    + (gamelog[9]["AST"] * 1.5)
    + (gamelog[9]["STL"] * 2)
    + (gamelog[9]["BLK"] * 2)
    - (gamelog[9]["TOV"])
) / gamelog[9]["MIN"]
gamelog[10]["FPPM"] = (
    (gamelog[10]["FG3M"] * 3)
    + (gamelog[10]["FGM"] * 2)
    + (gamelog[10]["FTM"])
    + (gamelog[10]["REB"] * 1.2)
    + (gamelog[10]["AST"] * 1.5)
    + (gamelog[10]["STL"] * 2)
    + (gamelog[10]["BLK"] * 2)
    - (gamelog[10]["TOV"])
) / gamelog[10]["MIN"]
gamelog[11]["FPPM"] = (
    (gamelog[11]["FG3M"] * 3)
    + (gamelog[11]["FGM"] * 2)
    + (gamelog[11]["FTM"])
    + (gamelog[11]["REB"] * 1.2)
    + (gamelog[11]["AST"] * 1.5)
    + (gamelog[11]["STL"] * 2)
    + (gamelog[11]["BLK"] * 2)
    - (gamelog[11]["TOV"])
) / gamelog[11]["MIN"]

fig, axs = plt.subplots(3, 4, constrained_layout=True)
fig.suptitle("Fantasy Analyzer: Player FPPM")
for i in range(4):
    for j in range(4):
        if i * 4 + j < len(player):
            pts = gamelog[i * 4 + j]["FPPM"]
            axs[i, j].plot(pts, color="pink")
            axs[i, j].set_title(name[i * 4 + j])
            axs[i, j].set_ylabel("Player FPPM")
            axs[i, j].get_ylim()
            axs[i, j].set_xticks([])


# ----------------------------------------------------------------------------------------
# Calculate and Plot Games Played Per Month

gamelog[0]["GPW"] = gamelog[0]["GAME_DATE"].str.split(" ", expand=True)[0]
gamelog[1]["GPW"] = gamelog[1]["GAME_DATE"].str.split(" ", expand=True)[0]
gamelog[2]["GPW"] = gamelog[2]["GAME_DATE"].str.split(" ", expand=True)[0]
gamelog[3]["GPW"] = gamelog[3]["GAME_DATE"].str.split(" ", expand=True)[0]
gamelog[4]["GPW"] = gamelog[4]["GAME_DATE"].str.split(" ", expand=True)[0]
gamelog[5]["GPW"] = gamelog[5]["GAME_DATE"].str.split(" ", expand=True)[0]
gamelog[6]["GPW"] = gamelog[6]["GAME_DATE"].str.split(" ", expand=True)[0]
gamelog[7]["GPW"] = gamelog[7]["GAME_DATE"].str.split(" ", expand=True)[0]
gamelog[8]["GPW"] = gamelog[8]["GAME_DATE"].str.split(" ", expand=True)[0]
gamelog[9]["GPW"] = gamelog[9]["GAME_DATE"].str.split(" ", expand=True)[0]
gamelog[10]["GPW"] = gamelog[10]["GAME_DATE"].str.split(" ", expand=True)[0]
gamelog[11]["GPW"] = gamelog[11]["GAME_DATE"].str.split(" ", expand=True)[0]

fig, axs = plt.subplots(3, 4, constrained_layout=True)
fig.suptitle("Fantasy Analyzer: Games Played Per Month")
for i in range(4):
    for j in range(4):
        if i * 4 + j < len(player):
            pts = gamelog[i * 4 + j]["GPW"].value_counts()
            pts = pts.sort_index()
            pts.plot(kind="bar", color="pink", ax=axs[i, j])
            axs[i, j].set_title(name[i * 4 + j])
            axs[i, j].set_ylabel("Games Played")
            axs[i, j].set_xlabel("Month")


plt.show()
