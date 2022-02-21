from PIL import Image
import streamlit as st
import altair as alt
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
from utils import download_file

st.title("NBA PLAYER STATS EXPLORER")

st.markdown("""
    This app performs simple webscraping of NBA player stats 
    * **Python libraries:** base64, pandas, streamlit
    * **Data Source:** [Basketball-reference] (https://www.basketball-reference.com/)
    * **Credit:** Project guided by dataprofessor on freeCodeCamp.org, tutorial link: (https://www.youtube.com/watch?v=JwSS70SZdyM&t=11s)
""")

st.sidebar.header("User Input Features")

selected_year = st.sidebar.selectbox("Year", list(reversed(range(1950, 2021))))

@st.cache

def load_data(year):
    url = f"https://www.basketball-reference.com/leagues/NBA_{str(year)}_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == "Age"].index)
    raw = raw.fillna(0)
    playstats = raw.drop(["Rk"], axis=1)
    return playstats

# Sidebar Team Selection
    sorted_unique_team = sorted(playstats.Tm.unique())
    selected_team = st.sidebar.multiselect("Team", sorted_unique_team, sorted_unique_team)

# Sidebar Position Selection 

    unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
    selected_pos = st.sidebar.multiselect("Position", unique_pos, unique_pos)

# Filtering data
    df_selected_team = playstats[(playstats.Tm.isin(selected_team) ) & (playstats.Pos.isin(selected_pos))]

    st.header("Display player stats of selected team (s)") 
    st.write(f'Data Dimension: {df_selected_team.shape[0]} rows and {df_selected_team.shape[1]} columns.')
st.dataframe(df_selected_team)


st.markdown(download_file(df_selected_team, f"{selected_team}_{selected_year}_{selected_pos}_player_stats"), unsafe_allow_html=True)

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot()
