import streamlit as st
import pandas as pd

st.set_page_config(page_title="Score Tracker", layout="centered")
st.title("🎯 Card Game Elimination Tracker Delta Section")

PLAYERS = ["Faheem", "Waseem", "Usama", "Waqar", "Wahab"]

# Initialize session state
if "scores" not in st.session_state:
    st.session_state.scores = {p: [] for p in PLAYERS}
if "history" not in st.session_state:
    st.session_state.history = []

# Display player statuses
cols = st.columns(len(PLAYERS))
active_count = 0

for i, name in enumerate(cols):
    player = PLAYERS[i]
    total = sum(st.session_state.scores[player])
    is_out = total >= 100

    with name:
        if is_out:
            st.metric(label=player, value=f"{total}", delta="OUT", delta_color="inverse")
        else:
            st.metric(label=player, value=f"{total}")
            active_count += 1

if active_count == 1:
    winner = [p for p in PLAYERS if sum(st.session_state.scores[p]) < 100][0]
    st.balloons()
    st.success(f"🏆 **{winner} wins the game!**")

# Input Form for New Round
st.subheader("Add Round Scores")
with st.form("round_form", clear_on_submit=True):
    input_cols = st.columns(len(PLAYERS))
    inputs = {}

    for i, col in enumerate(input_cols):
        player = PLAYERS[i]
        with col:
            if sum(st.session_state.scores[player]) < 100:
                inputs[player] = st.number_input(f"{player}", min_value=0, step=1, key=f"in_{player}")
            else:
                inputs[player] = None
                st.caption(f"~~{player} (Out)~~")

    submitted = st.form_submit_button("Record Round")
    if submitted:
        round_data = {"Round": f"R{len(st.session_state.history) + 1}"}
        for player in PLAYERS:
            val = inputs[player]
            if val is not None:
                st.session_state.scores[player].append(val)
                round_data[player] = val
            else:
                round_data[player] = "OUT"

        st.session_state.history.append(round_data)
        st.rerun()

# Log Table
if st.session_state.history:
    st.subheader("Round History")
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True, hide_index=True)

# Reset Button
if st.button("Reset Game"):
    st.session_state.scores = {p: [] for p in PLAYERS}
    st.session_state.history = []
    st.rerun()