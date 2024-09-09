import streamlit as st
import time
import os
import sys

# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Importer la fonction depuis ToJson.py
from Utils.Tojson import gethistorique

def generate_chat():
    # Display chat messages from history on app rerun
    long = len(st.session_state.historique)
    i = 0
    for elmt in st.session_state.historique:
        with (st.chat_message(elmt["role"])):
            if elmt == st.session_state.historique[long - 1] and type(elmt["content"]) != str:
                content = st.write_stream(elmt["content"])
                elmt["content"] = content + "\n"
                st.session_state.audiopath.append("")
            else:
                st.write('<p>' + elmt["content"] + '</p>', unsafe_allow_html=True)
            i += 1
    # React to user input
    if prompt := st.chat_input("Intervention de l'Animateur :"):
        # Add user message to chat history
        # intervention_animateur(prompt)
        st.rerun()

if 'agentname' not in st.session_state:
    st.header("You don't have an agent in charge")
    with st.spinner('Redirection in progress'):
        time.sleep(3)
    st.switch_page("subpages/Agents.py")

with st.sidebar:
    st.header("Your conversation histories")

st.title(f"Your agent : {st.session_state.agentname}")
st.header(f"Your Api Base : {st.session_state.apibase}")
st.header(f"Model : {st.session_state.agentmodel}")


st.session_state.historique = gethistorique(st.session_state.agentname, "1")
with st.container(border=True, height=800):
    generate_chat()




