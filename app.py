import streamlit as st
import statsapi
import pandas as pd

st.set_page_config(page_title="MLB Dashboard", layout="wide")
st.title("⚾ MLB Dashboard")

# ── LIVE SCORES ──────────────────────────────────────────
st.header("Today's Games")

games = statsapi.schedule(sportId=1)

if not games:
    st.write("No games today.")
else:
    for game in games:
        home = game['home_name']
        away = game['away_name']
        status = game['status']
        home_score = game['home_score']
        away_score = game['away_score']
        current_inning = game['current_inning']
        inning_state = game['inning_state']
        venue_name = game['venue_name']

        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        with col1:
            st.write(f"**{away}** @ **{home}**")
        with col2:
            st.write(f"{away_score} - {home_score}")
        with col3:
            st.write(status)
        with col4:
            # Only show inning state and current inning when game is in progress
            if isinstance(status, str) and status.lower() == 'in progress':
                st.write(f"{inning_state} {current_inning}")
            else:
                st.write("")
        
            

# ── STANDINGS ────────────────────────────────────────────
st.header("Standings")

standings = statsapi.standings_data()

divisions = {
    201: "AL East", 200: "AL West", 202: "AL Central",
    204: "NL East", 203: "NL West", 205: "NL Central"
}

al_divs = [201, 200, 202]
nl_divs = [204, 203, 205]

def render_division(div_id, div_name):
    teams = standings[div_id]['teams']
    df = pd.DataFrame([{
        "Team": t['name'],
        "W": t['w'],
        "L": t['l'],
        "GB": t['gb']
    } for t in teams])
    st.subheader(div_name)
    st.dataframe(df, hide_index=True, use_container_width=True)

st.subheader("American League")
cols = st.columns(3)
for col, div_id in zip(cols, al_divs):
    with col:
        render_division(div_id, divisions[div_id])

st.subheader("National League")
cols = st.columns(3)
for col, div_id in zip(cols, nl_divs):
    with col:
        render_division(div_id, divisions[div_id])