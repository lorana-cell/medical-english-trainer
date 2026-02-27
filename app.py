import streamlit as st
import random

st.set_page_config(page_title="Medical English Trainer", page_icon="👩🏻‍⚕️")

st.title("👩🏻‍⚕️ Medical English Speaking Trainer")

st.markdown("Practice speaking with a foreign patient simulation.")

if "chat" not in st.session_state:
    st.session_state.chat = []

patient_cases = [
    "Hi doctor, I’ve been having chest pain since this morning.",
    "Doctor, I feel nauseous and have diarrhea since yesterday.",
    "I have a terrible headache and feel dizzy.",
    "I’ve been coughing for 5 days and it’s getting worse."
]

if st.button("Start Consultation"):
    case = random.choice(patient_cases)
    st.session_state.chat = [("Patient", case)]

for speaker, message in st.session_state.chat:
    st.write(f"**{speaker}:** {message}")

user_input = st.text_input("Your response as the doctor:")

if user_input:
    st.session_state.chat.append(("Doctor", user_input))
    response = "Thank you for explaining. Can you tell me more about your symptoms?"
    st.session_state.chat.append(("Patient", response))
    st.rerun()
