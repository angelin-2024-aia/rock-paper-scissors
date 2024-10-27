import streamlit as st
import random

st.title("Rock, Paper, Scissors Game")

st.write("Choose Rock, Paper, or Scissors and see if you can beat the computer!")

choices = ["Rock", "Paper", "Scissors"]

user_choice = st.selectbox("Your Choice:", choices)

if st.button("Play"):
    computer_choice = random.choice(choices)
    st.write("Computer chose: ",computer_choice)
    if user_choice == computer_choice:
        st.write("It's a draw!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.write("You win!")
    else:
        st.write("You lose!")
if st.button("Play Again"):
    st.write("Make another choice to play again!")