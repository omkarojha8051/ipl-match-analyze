import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")

# Load the dataset
def load_data():
    df = pd.read_csv("ipl_data.csv")
    return df

#Cleaning the data 
def clean_data(df): 
    name_fixes = {
    'Royal Challengers Bangalore': 'Royal Challengers Bengaluru',
    'Delhi Daredevils': 'Delhi Capitals',
    'Rising Pune Supergiant': 'Rising Pune Supergiants'
    }

    for col in ['team1', 'team2', 'winner', 'toss_winner']:
        df[col] = df[col].replace(name_fixes)
    df['city'] = df['city'].replace('Bangalore','Bengaluru')
    return df
  
# Finding the winning pattern 
def analyze_team_wins(df):
    wins =  df['winner'].dropna().value_counts()
    print(" Team win count ")
    print(wins)
    plt.figure(figsize=(12,6))
    plt.bar(wins.index,wins.values)
    plt.title("Chart of ipl Wins ")
    plt.xlabel("Teams")
    plt.ylabel("No of wins")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("team_wins_fig.png")
    plt.show()

    return df


#finding role of toss
def analyze_toss_impact(df):
    df['toss_win_helped'] = df['toss_winner'] == df['winner']
    print(df['toss_win_helped'].value_counts())

    total =  df['toss_win_helped'].value_counts().sum()
    pct = (df['toss_win_helped'].sum() / total ) * 100
    print(f"Toss winner won the match {pct:.1f}% times")
 
    print(df[(df['toss_win_helped'] == True)] ['toss_decision'].value_counts())

# piechart

    toss = df['toss_decision'].value_counts()
    plt.figure(figsize=(12,6))
    plt.pie(toss, labels=toss.index, autopct='%1.1f%%')
    plt.title("Impact of decision ")
    plt.tight_layout()
    plt.savefig("toss_decision.png")
    plt.show()
    return df

 
#most player of the match
def analyze_player_of_match(df):
    print(df['player_of_match'].value_counts().head(10))
    clumsy = df['player_of_match'].value_counts().head(10)
    plt.figure(figsize=(12,6))
    plt.bar(clumsy.index,clumsy.values)
    plt.title("Top 10 player of the matches in the ipl")
    plt.xlabel("Players Name")
    plt.ylabel("no of player of matches")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("player_of_match.png")
    plt.show()
    return df


def analyze_venue_scores(df):
    cucumber = df.groupby('venue')['team1_runs'].mean().sort_values(ascending=False).head(10)
    cucumber.index = cucumber.index.str.split(',').str[0]

# barchart for venue

    plt.figure(figsize=(12,6))
    plt.bar(cucumber.index,cucumber.values)
    plt.title("Top 10 avg first inning score on venues ")
    plt.xlabel("Venue")
    plt.ylabel("Runs")
    plt.xticks(rotation=45,ha='right')
    plt.ylim(170, 230)
    plt.tight_layout()
    plt.savefig("venue_avg_score.png")
    plt.show()
    return df



# Finding the recent changes in ipl based on the data 
def  analyze_season_runs(df):
    df['total_runs'] =  df['team1_runs'] + df['team2_runs']
    season_runs =  df.groupby('season')['total_runs'].mean()
    print(season_runs)
    plt.figure(figsize=(12,6))
    plt.plot(season_runs.index,season_runs.values,marker='o',ms=6,color='red',linestyle='--',linewidth=2)
    plt.title("Trend of IPL runs per season")
    plt.xlabel("season")
    plt.ylabel("Average match per Season")
    plt.xticks(rotation=45,ha='right')
    plt.tight_layout()
    plt.savefig("season_runs.png")
    plt.show()
    return df


def analyze_win_margins(df):
    win_margin= df[df['win_by_runs'] != 0].groupby('season')['win_by_runs'].mean()
    win_margin = win_margin.round(2)
    print(win_margin)

    plt.figure(figsize=(12,6))
    plt.plot(win_margin.index,win_margin.values,color='black',marker='o',ms=6,linewidth=2)
    plt.title("Trend of IPL win margin per season")
    plt.xlabel("season")
    plt.ylabel("Average win per Season")
    plt.xticks(rotation=45,ha='right')
    plt.tight_layout()
    plt.savefig("season_win_margin.png")
    plt.show()
    return df 

    #Wins analsis on heatmap
def analyze_wins_heatmap(df):
    heatmap_data = df[df['winner'].notna()].pivot_table(
        index='winner',
        columns='season',
        aggfunc='size',
        fill_value=0
    )
    print(heatmap_data)
    plt.figure(figsize=(16, 8))
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlOrRd')
    plt.title("Team Wins per Season - Heatmap")
    plt.xlabel("Season")
    plt.ylabel("Team")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("wins_heatmap.png")
    plt.show()
    return df

if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    df = analyze_team_wins(df)
    df = analyze_toss_impact(df)
    df = analyze_player_of_match(df)
    df = analyze_venue_scores(df)
    df = analyze_season_runs(df)
    df = analyze_win_margins(df)
    df = analyze_wins_heatmap(df)
    print(df['winner'].dropna().value_counts())
