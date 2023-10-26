import streamlit as st
import send_email

import pandas as pd

topics = pd.read_csv('topics.csv')


st.title("Contact Us")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email")
    user_topic = st.selectbox("Select a topic", topics['topic'])
    user_message = st.text_area("Your message")
    submitted = st.form_submit_button("Submit")
    message = f"""Subject: Contact form

From: {user_email}
Topic: {user_topic}
{user_message}
"""
    if submitted:
        send_email.send_email(message)
        st.info("Submitted!")
