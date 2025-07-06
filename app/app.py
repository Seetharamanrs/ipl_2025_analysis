import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config("Wide")
st.title('IPL_Analysis')
path="D:\my_git\ipl_2025_analysis\data\ipl_2025_deliveries.csv"
df=pd.read_csv(path)
team_colors = {
    'RCB': '#D50032',
    'KKR': '#4B2153',
    'RR': '#004C93',
    'SRH': '#F05A28',
    'CSK': '#FAD201',
    'MI': '#004BA0',
    'DC': '#004C93',
    'LSG': '#F5D547',
    'GT': '#008080',
    'PBKS': '#E41D44'
}
st.sidebar.header( "Filter")
s_t=st.sidebar.selectbox("Select Team",df['batting_team'].unique())
t_df=df[df["batting_team"]==s_t]
st.subheader("Wicket Types")
t_wickets = df[(df["wicket_type"].notnull())&(df['bowling_team']==s_t)]
wicket_count = t_wickets["wicket_type"].value_counts()

fig1, ax1 = plt.subplots(figsize=(10,6))
sns.barplot(x=wicket_count.index, y=wicket_count.values, ax=ax1)
# ax1.
ax1.set_title("Wicket Types")
st.pyplot(fig1)

st.subheader(f"{s_t} Total Runs")

top_batsmen=t_df.groupby('striker')['runs_of_bat'].sum()
top_batsmen=top_batsmen.sort_values(ascending=False).head(10)

fig2,ax2=plt.subplots(figsize=(10,6))
sns.barplot(x=top_batsmen.index, y=top_batsmen.values, ax=ax2)
ax2.set_title(f"Top Batsmen in {s_t}")
ax2.tick_params(axis='x', rotation=30)
st.pyplot(fig2)

st.subheader("Total wicket taken by bolwers")
team_wick=df[(df['bowling_team']==s_t) & (df['player_dismissed'].notnull())]
team_wick=team_wick.groupby('bowler')['player_dismissed'].count().sort_values(ascending=False)
team_wick=pd.DataFrame(team_wick)
fig4,ax4=plt.subplots(figsize=(10,6))
sns.barplot(x=team_wick.index,y=team_wick['player_dismissed'],ax=ax4)
ax4.set_title("Total wicket taken in tournament")
ax4.tick_params(axis='x',rotation=30)
ax4.set_ylabel('Wicket Taken')
st.pyplot(fig4)


st.header("Score Of Team in Entire Tournament")
df["total_run"] = df["runs_of_bat"] + df["extras"]
team_total = df.groupby("batting_team")["total_run"].sum().sort_values(ascending=False)

fig3, ax3 = plt.subplots()
sns.barplot(x=team_total.index, y=team_total.values, ax=ax3,palette=team_colors)
ax3.set_title("Total Team Scores in IPL 2025")
ax3.set_xlabel('Team Name ')
ax3.set_ylabel('Runs Scored')
st.pyplot(fig3)

