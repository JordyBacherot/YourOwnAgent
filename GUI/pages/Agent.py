import streamlit as st
from streamlit import selectbox
import sys
import os
# Agent.py

import sys
import os

# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Importer la fonction depuis ToJson.py
from Utils.Tojson import get_key, add_key

@st.dialog("Create an agent with Groq")
def dialog_create_groq_agent():
    key = get_key("groqkey")
    col1, col2 = st.columns(2)
    if key is not None:
        st.session_state.key = selectbox("Choose a key", key)
    st.divider()
    st.write("If you want to add a key :")
    st.session_state.newkeyname = st.text_input("Please enter your name key")
    st.session_state.newkey = st.text_input("Please enter your key")
    col1, col2 = st.columns(2)
    if st.button("Add the key") :
        add_key("groqkey", st.session_state.newkeyname, st.session_state.newkey)
        st.rerun()
    if st.button("Where can I find my key ?") :
        st.info("You have to create an account on the website Groq and go to the API section to get your key")
    st.divider()
    model_ids = [
        "gemma2-9b-it",
        "llama3-70b-8192",
        "llama3-8b-8192",
        "mixtral-8x7b-32768",
    ]
    st.session_state.model = st.selectbox("Please enter the model you want to use", model_ids)
    if st.button("Create the agent"):
        st.session_state.dialog.close()

if st.button("Click here to add a Groq agent") :
    dialog_create_groq_agent()