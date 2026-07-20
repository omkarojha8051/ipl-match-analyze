
# 🏏 IPL Match Analyzer

An end-to-end data analysis project exploring every IPL match from **2008–2026** using **Python, Pandas, NumPy, Matplotlib, and Seaborn**.

The project uncovers insights into team performance, toss impact, venue influence, scoring trends, and player achievements using real IPL match data.



## Key Insights

- IPL scoring has surged since 2022 — average runs per match jumped from ~315 (2021) to ~375+ (2026), reflecting more aggressive batting and shorter boundaries.

- Toss impact in IPL is minimal — only 50.5% of toss winners go on to win the match, barely better than a coin flip. Interestingly, 70% of toss winners chose to field first, suggesting the toss decision matters more than winning the toss itself.

- Venue significantly impacts scoring — stadiums with shorter boundaries (like Maharaja Yadavindra Singh Stadium) average ~220 runs, while larger grounds average notably lower.

- Scoring remained largely stable from 2014 to 2021, but surged by roughly 20% between 2008 and 2026 — driven by factors like the Impact Player rule, flatter pitches, and a shift toward more aggressive modern batting.

- Mumbai Indians lead all-time wins (155), while AB de Villiers holds the most Player of the Match awards (25) — both confirmed through data, not reputation.

## Sample Visualizations

![Team Wins](team_wins_fig.png)
![Wins Heatmap](wins_heatmap.png)
![Toss impact](toss_decision.png)
![Venue Impact](venue_avg_score.png)
![Season rus](season_runs.png)
![Winning Margin Trends](season_win_margin.png)
![Most Player Of The Matches](player_of_match.png)

## Dataset

- Source: Kaggle IPL Matches Dataset
- Matches: 1,243
- Seasons: 2008–2026
- Columns: 26

## What This Project Does

The dataset, sourced from Kaggle, contains **1,243 IPL matches (2008–2026)** across **26 columns**, including teams, venues, toss decisions, match outcomes, and player awards.

The raw dataset contained inconsistencies such as:

- Delhi Daredevils → Delhi Capitals
- Bangalore → Bengaluru

These inconsistencies were cleaned using **Pandas** before analysis.

The project uses:

- **Pandas** for cleaning and analysis
- **NumPy** for statistical calculations
- **Matplotlib** and **Seaborn** for visualizations

Overall, the project generates **7 visualizations** and several data-driven insights about IPL history.

## Challenges

### 1. Virtual Environment & PowerShell Issues
- This was my first project using a Python virtual environment. I initially faced several PowerShell-related issues while creating and activating the environment. During development, I also encountered terminal freezes and command interruptions, which I learned to resolve using shortcuts like Ctrl + C and reopening the terminal (Ctrl + `).

### 2. Similar Functions with Different Purposes
- Several pandas functions appeared very similar but served different purposes. Understanding the differences between functions such as:

- `isna()` vs `notna()`
- `dropna()` vs filtering
- `value_counts()` vs `groupby().size()`

helped me understand when each approach is appropriate.

### 3. Debugging a Data Cleaning Bug
- One of the biggest debugging challenges occurred when my name_fixes dictionary was accidentally commented out. Since the cleaning step never executed, inconsistent team names remained in the dataset, leading to incorrect analysis results. Finding this bug reinforced the importance of verifying preprocessing before trusting analytical results.

### 4. GitHub Authentication
- While pushing my project to GitHub for the first time, I encountered authentication issues. I wasn't sure whether to use browser-based authentication or a Personal Access Token (PAT), which prevented me from pushing my code successfully.

After understanding GitHub authentication and configuring Git correctly, I was able to push the project successfully. This provided valuable real-world experience beyond local Git usage.

## What I Learned
Throughout this project I gained hands-on experience with:

- Cleaning real-world datasets.
- Writing reusable Python functions.
- Using Pandas for filtering, grouping, aggregation, and data analysis.
- Performing statistical analysis with NumPy.
- Creating professional visualizations using Matplotlib and Seaborn.
- Debugging real programming issues.
- Using Git and GitHub for version control.
- Extracting meaningful insights from raw data instead of relying on assumptions.

## Tech Stack

- **Python** — core programming language
- **Pandas** — data cleaning, filtering, and aggregation
- **NumPy** — statistical calculations (mean, median, correlation)
- **Matplotlib** — bar, pie, and line chart visualizations
- **Seaborn** — heatmap visualization

## How to Run

1. Clone this repository:
```
git clone <your-repo-url>
cd ipl-analyzer
```

2. Create a virtual environment:
```
python -m venv venv
```

3. Activate it:
```
venv\Scripts\activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```

5. Run the script:
```
python main.py
```

## Future Improvements

- **Player-level analysis**: This project is currently match-centric. Adding ball-by-ball data (deliveries.csv) would enable deeper individual player statistics like strike rate, batting average, and bowling economy.
- **Super Over analysis**: The dataset doesn't record Super Over winners separately, so tied matches were excluded from win-count analysis. A dedicated Super Over dataset could resolve this gap.
- **Shot selection trends**: With ball-by-ball data, it would be interesting to analyze the shift toward unconventional shot selection (e.g., leg-side preference) among modern batters compared to earlier eras.