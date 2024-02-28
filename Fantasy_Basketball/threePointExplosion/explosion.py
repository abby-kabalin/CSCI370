# Abby Kabalin
# 2/21/2024
# 3-Point Explosion
# -------------------------------------------------------------------------------------------------------------------------
# The 3-point explosion is evident in the line plots. The number of 3-point attempts and makes has increased significantly
# since the introduction of the 3-point line in the 1979-80 season. This trend is consistent across all NBA teams.
# The line plots provide a visual representation of the 3-point explosion and highlight the impact of the 3-point shot
# on modern basketball.
# -------------------------------------------------------------------------------------------------------------------------
# Imports
import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.static import teams as teams
from nba_api.stats.static import players as players
from nba_api.stats.endpoints import teamyearbyyearstats

# Get all NBA teams
nba_teams = teams.get_teams()
df_nba_teams = pd.DataFrame(nba_teams)


# Create a line plot to visualize the 3-point explosion
def plot3PA():
    plt.figure(figsize=(30, 20))
    plt.title("3 Point Explosion")
    plt.xlabel("Year")
    plt.ylabel("3 Point Attempts")

    # Iterate over each team
    for team in nba_teams:
        teamId = team["id"]
        name = team["full_name"]

        try:
            # Get the team's 3-point attempts and makes for each season
            all_teams = teamyearbyyearstats.TeamYearByYearStats(team_id=teamId)
            df_all_teams = pd.DataFrame(all_teams.get_data_frames()[0])
            df_team = df_all_teams[df_all_teams["TEAM_ID"] == teamId]

            # Filter the data to include only the seasons after the introduction of the 3-point line
            df_team = df_team[df_team["YEAR"] >= "1979-80"]

            # Calculate the total 3-point attempts and makes for each season
            df_team["3PA"] = df_team["FG3A"]
            df_team["3PM"] = df_team["FG3M"]

            # Plot the team's data
            plt.plot(df_team["YEAR"], df_team["3PA"], label=name)

            # Set x ticks every 5 years
            plt.xticks(df_team["YEAR"][::5])

        except KeyError:
            continue

    plt.legend()


def plot3PM():
    plt.figure(figsize=(30, 20))
    plt.title("3 Point Explosion")
    plt.xlabel("Year")
    plt.ylabel("3 Point Makes")

    # Iterate over each team
    for team in nba_teams:
        teamId = team["id"]
        name = team["full_name"]

        try:
            # Get the team's 3-point attempts and makes for each season
            all_teams = teamyearbyyearstats.TeamYearByYearStats(team_id=teamId)
            df_all_teams = pd.DataFrame(all_teams.get_data_frames()[0])
            df_team = df_all_teams[df_all_teams["TEAM_ID"] == teamId]

            # Filter the data to include only the seasons after the introduction of the 3-point line
            df_team = df_team[df_team["YEAR"] >= "1979-80"]

            # Calculate the total 3-point attempts and makes for each season
            df_team["3PA"] = df_team["FG3A"]
            df_team["3PM"] = df_team["FG3M"]

            # Plot the team's data
            plt.plot(df_team["YEAR"], df_team["3PM"], label=name)

            # Set x ticks every 5 years
            plt.xticks(df_team["YEAR"][::5])

        except KeyError:
            continue

    plt.legend()


plot3PA()
plot3PM()
plt.show()
