import streamlit as st
from streamlit import selectbox
import json
import sys
import os

# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Importer la fonction depuis ToJson.py
from Utils.Tojson import get_key, add_key, create_an_agent, get_all_agents


@st.dialog("Create an agent with Groq")
def dialog_create_groq_agent():
    keynames = get_key("groqkey")
    if keynames is not None:
        st.session_state.keyname = selectbox("Choose a key name", keynames)
        st.session_state.key = keynames[st.session_state.keyname]
    else :
        st.write("You have to add a key")
    st.button("Refresh the keys")
    st.divider()
    st.write("If you want to add a key :")
    st.session_state.newkeyname = st.text_input("Please enter your name key")
    st.session_state.newkey = st.text_input("Please enter your key")
    if st.button("Add the key") :
        verify = add_key("groqkey", st.session_state.newkeyname, st.session_state.newkey)
        if not verify:
            st.write("This key name already exist")
        else :
            st.write("The key has been added")
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
    st.session_state.agentname = st.text_input("Please enter the name of your agent")
    if st.button("Create the agent") :
        if st.session_state.keyname != "" and st.session_state.key != "" and st.session_state.agentname != "":
            verify = create_an_agent("groq", st.session_state.agentname, st.session_state.key, st.session_state.model)
            if verify is not None:
                st.rerun()
            else :
                st.warning("An agent with this name already exist")
        else :
            st.write("Key name : ", st.session_state.keyname)
            st.write("Key : ", st.session_state.key)
            st.write("Agent name : ", st.session_state.agentname)
            st.write("Model : ", st.session_state.model)
            st.warning("Please fill all the fields : Key Name, Key, Model and Agent name")


@st.dialog("Create an agent with OpenAI")
def dialog_create_openai_agent():
    keynames = get_key("openaikey")
    if keynames is not None:
        st.session_state.keyname = selectbox("Choose a key name", keynames)
        st.session_state.key = keynames[st.session_state.keyname]
    else:
        st.write("You have to add a key")
    st.divider()
    st.write("If you want to add a key :")
    st.session_state.newkeyname = st.text_input("Please enter your name key")
    st.session_state.newkey = st.text_input("Please enter your key")
    if st.button("Add the key") :
        verify = add_key("openaikey", st.session_state.newkeyname, st.session_state.newkey)
        if not verify:
            st.write("This key name already exist")
        else :
            st.write("The key has been added")
    if st.button("Where can I find my key ?") :
        st.info("You have to create an account on the website Groq and go to the API section to get your key")
    st.divider()
    model_ids = [
        "gpt-4o",
        "gpt-4o-turbo",
        "gpt-4o-mini",
        "gpt-4",
        "gpt-3.5-turbo"
    ]
    st.session_state.model = st.selectbox("Please enter the model you want to use", model_ids)
    st.session_state.agentname = st.text_input("Please enter the name of your agent")
    if st.button("Create the agent"):
        if st.session_state.keyname != "" and st.session_state.key != "" and st.session_state.agentname != "":
            verify = create_an_agent("openai", st.session_state.agentname, st.session_state.key, st.session_state.model)
            if verify:
                st.rerun()
            else:
                st.warning("An agent with this name already exist")
        else:
            st.warning("Please fill all the fields : Key Name, Key, Model and Agent name")

if st.button("Click here to add a Groq agent") :
    dialog_create_groq_agent()

if st.button("Click here to add an OpenAI Agent") :
    dialog_create_openai_agent()

dataAgents = get_all_agents()
for agent in dataAgents:
    st.button(agent["agentname"])