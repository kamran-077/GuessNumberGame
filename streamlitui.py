import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize game state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.write("Guess a number between **1 and 100**")

guess = st.number_input(
    "Enter the number:",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.warning("Too low ⬇️")
    elif guess > st.session_state.number:
        st.warning("Too high ⬆️")
    else:
        st.success("🎉 GOLU WON THE GAME 🎉")
        st.info(f"Attempts: {st.session_state.attempts}")

        # 🎈🎆 Celebration effects
        st.balloons()   # bubbles
        st.snow()       # crackers / confetti feel

        st.session_state.game_over = True

# Restart button
if st.session_state.game_over:
    if st.button("Play Again 🔄"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False