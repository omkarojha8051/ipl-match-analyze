import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")


def load_data():
    """Load IPL dataset from CSV file."""
    df = pd.read_csv("ipl_data.csv")
    return df


def clean_data(df): 
    """Standardize team and city name inconsistencies across all columns."""
    name_fixes = {
    'Royal Challengers Bangalore': 'Royal Challengers Bengaluru',
    'Delhi Daredevils': 'Delhi Capitals',
    'Rising Pune Supergiant': 'Rising Pune Supergiants'
    }

    for col in ['team1', 'team2', 'winner', 'toss_winner']:
        df[col] = df[col].replace(name_fixes)
    df['city'] = df['city'].replace('Bangalore','Bengaluru')
    # 25 matches have no winner: 16 ties (Super Over not recorded) + 9 rain-abandoned
# Decision: exclude winner=NaN rows only in win-count analysis, keep full dataset intac
    return df


  
 
def analyze_team_wins(df):
    """Analyze and visualize total wins per team across all IPL seasons."""
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



def analyze_toss_impact(df):
    """Analyze and visualize the impact of toss across all IPL seasons."""

    df['toss_win_helped'] = df['toss_winner'] == df['winner']
    print(df['toss_win_helped'].value_counts())

    total =  df['toss_win_helped'].value_counts().sum()
    pct = (df['toss_win_helped'].sum() / total ) * 100
    print(f"Toss winner won the match {pct:.1f}% times")
 
    print(df[(df['toss_win_helped'] == True)] ['toss_decision'].value_counts())



    toss = df['toss_decision'].value_counts()
    plt.figure(figsize=(12,6))
    plt.pie(toss, labels=toss.index, autopct='%1.1f%%')
    plt.title("Impact of decision ")
    plt.tight_layout()
    plt.savefig("toss_decision.png")
    plt.show()
    return df

 

def analyze_player_of_match(df):
    """Analyze and visualize most player of the match across all IPL seasons."""
    print(df['player_of_match'].value_counts().head(10))
    player = df['player_of_match'].value_counts().head(10)
    plt.figure(figsize=(12,6))
    plt.bar(player.index,player.values)
    plt.title("Top 10 player of the matches in the ipl")
    plt.xlabel("Players Name")
    plt.ylabel("no of player of matches")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("player_of_match.png")
    plt.show()
    return df


def analyze_venue_scores(df):
    """Analyze and visualize most runs on a venue ."""
    venue_impact = df.groupby('venue')['team1_runs'].mean().sort_values(ascending=False).head(10)
    venue_impact.index = venue_impact.index.str.split(',').str[0]


    plt.figure(figsize=(12,6))
    plt.bar(venue_impact.index,venue_impact.values)
    plt.title("Top 10 avg first inning score on venues ")
    plt.xlabel("Venue")
    plt.ylabel("Runs")
    plt.xticks(rotation=45,ha='right')
    plt.ylim(170, 230)
    plt.tight_layout()
    plt.savefig("venue_avg_score.png")
    plt.show()
    return df




def  analyze_season_runs(df):
    """Analyze and visualize total runs per season across all IPL seasons."""
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
    """Analyze and visualize win margin trend ."""
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

    
def analyze_wins_heatmap(df):
    """Analyze and visualize most wins by a team per season."""
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
