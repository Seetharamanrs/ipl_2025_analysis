# `IPL 2025 Analysis`
- This project analyzes ball-by-ball data from the **IPL 2025 Season**, offering comphensive insights through data cleaning and visualization. 
- This analysis cover individual player performances, team statistics and overall tournament trends.

## Datset summary   
- **Total Samples:** 17246
- **Features:** 20

### The Feature with missing value
- **wicket type:** 16373 `Values present Only when wicket occurs`
- **player_dismissed:**  16373 ` Record only present only when player is dismissed ` 
- **fielder:** 16566 `Only filled when fielder involved in Catch or Run outs `

## Key Analysis

### **Wicket Types**
- Visualized the types of dismissals(caught, bowled, stumped, lbw, runout, retired out, retired hurt, hit wicket)
- counted each dismissals type across the tournament

### **Top Batsmen**
- Identified top batsmen by:
**Total run scored**, **Total Balls Faced**
### **Bowling Statistics**
- Top bolwers by:
**Wickets taken**, 
, **Wide balls**, **No balls.**
### **Team-Wise Performance**
- Total runs scored by each team.
- Analyzed wide balls and wickets for specific teams 
- Highlighted Best CSK bowler and batsmen.
### **Boundary Analysis**
- Number of **Fours(4s)**and **sixes(6s)** hiy by CSK batsmen.
## Visulization 
The notebook includes seaborn/matplotlib visualizations such as:
- Barchats for:
    - Wickets types
    - Top runs scores 
    - Most wides and no balls
    - Team total scores
## Technologies used

- **Python 3**
- **Pandas** for data manipulation
- **Matplotlib & Seaborn** for visualizations
- **Jupyter Notebook** for interactive analysis