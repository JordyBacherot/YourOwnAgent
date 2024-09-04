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
    with col1:
        if key is not None:
            st.session_state.key = selectbox("Pick the key", key)
    with col2 :
        st.write("Add a key")
        st.session_state.newkeyname = st.text_input("Please enter your name key")
        st.session_state.newkey = st.text_input("Please enter your key")
        if st.button("Add the key") :
            add_key("groqkey", st.session_state.newkeyname, st.session_state.newkey)
            st.empty()

if st.button("Click here to add an Groq agent") :
    dialog_create_groq_agent()