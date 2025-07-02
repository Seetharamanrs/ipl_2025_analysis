import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config("Wide")
st.title('IPL_Analysis')
path="D:\my_git\ipl_2025_analysis\data\ipl_2025_deliveries.csv"
df=pd.read_csv(path)

st.sidebar.header( "Filter")
s_t=st.sidebar.selectbox("Select Team",df['batting_team'].unique())

st.subheader("Wicket Types")
t_wickets = df[(df["wicket_type"].notnull())&(df['bowling_team']==s_t)]
wicket_count = t_wickets["wicket_type"].value_counts()

fig1, ax1 = plt.subplots(figsize=(10,6))
sns.barplot(x=wicket_count.index, y=wicket_count.values, ax=ax1)
# ax1.
ax1.set_title("Wicket Types")
st.pyplot(fig1)

st.subheader(f"{s_t} Total Runs")
t_df=df[df["batting_team"]==s_t]
top_batsmen=t_df.groupby('striker')['runs_of_bat'].sum()
top_batsmen=top_batsmen.sort_values(ascending=False).head(10)

fig2,ax2=plt.subplots(figsize=(10,6))
sns.barplot(x=top_batsmen.index, y=top_batsmen.values, ax=ax2)
ax2.set_title(f"Top Batsmen in {s_t}")
ax2.tick_params(axis='x', rotation=30)
st.pyplot(fig2)