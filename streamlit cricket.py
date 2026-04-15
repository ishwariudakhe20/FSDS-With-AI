import streamlit as st
import pandas as pd
import numpy as np

# --- Title ---
st.title("🏏 Cricket Fan Dashboard")
st.write("Welcome to your personal cricket analytics app!")

# --- Sidebar ---
st.sidebar.header("🎯 Player Selection")

player_name = st.sidebar.text_input("Enter Player Name", "Virat Kohli")

format_type = st.sidebar.selectbox(
    "Select Format",
    ["T20", "ODI", "Test"]
)

matches = st.sidebar.slider("Matches Played", 1, 500, 100)

# --- Player Info ---
st.header(f"🔥 Player: {player_name}")
st.write(f"Format: {format_type} | Matches: {matches}")

# --- Generate Stats ---
runs = np.random.randint(1000, 15000)
avg = round(np.random.uniform(30, 60), 2)
strike_rate = round(np.random.uniform(70, 180), 2)

col1, col2, col3 = st.columns(3)

col1.metric("🏏 Total Runs", runs)
col2.metric("📊 Average", avg)
col3.metric("⚡ Strike Rate", strike_rate)

# --- Performance Data ---
st.subheader("📈 Match Performance")

performance = pd.DataFrame({
    "Match": range(1, 11),
    "Runs": np.random.randint(0, 150, 10)
})

st.line_chart(performance.set_index("Match"))

# --- Shot Selection ---
st.subheader("🎯 Shot Analysis")

shots = ["Cover Drive", "Pull Shot", "Cut Shot", "Straight Drive"]

shot_choice = st.selectbox("Select your favorite shot", shots)

st.write(f"You selected: **{shot_choice}** 🔥")

# --- Checkbox ---
if st.checkbox("Show Performance Data"):
    st.write(performance)

# --- Button ---
if st.button("Motivate Me 💪"):
    st.success("Push yourself! Every run counts! 🏆🔥")
else:
    st.write("Click the button for motivation!")

# --- Fun Section ---
st.subheader("🎲 Predict Your Score")

predicted_score = st.slider("Select expected score", 0, 200, 50)

if predicted_score > 100:
    st.success("Century Loading! 💯🔥")
elif predicted_score > 50:
    st.info("Good innings 👍")
else:
    st.warning("Need improvement 😅")
