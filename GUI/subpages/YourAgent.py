import streamlit as st
import time
import os
import sys

# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Importer la fonction depuis ToJson.py
from Utils.Tojson import gethistorique, addtohistorique, getconversations, addconversation, getfirstconversation
from Utils.LLM import call_llm

@st.dialog("Add a conversation")
def dialogtoaddconversation():
    st.session_state.newconversationname = st.text_input("Please enter the name of the conversation")
    st.session_state.newcontext = st.text_area("Please enter the context of the conversation", value = "Tu es un chatbot d'assistance à un humain.")
    if st.button("Add the conversation") and st.session_state.newconversationname != "" and st.session_state.newcontext != "":
        addconversation(st.session_state.agentname, st.session_state.newconversationname, st.session_state.newcontext)
        st.session_state.nameconversation = st.session_state.newconversationname
        st.session_state.historique = gethistorique(st.session_state.agentname, st.session_state.nameconversation)
        st.rerun()
    else :
        st.warning("Please fill the name of the conversation and the context")




def generate_chat():
    # Display chat messages from history on app rerun
    long = len(historique)
    i = 0
    for elmt in historique:
        with (st.chat_message(elmt["role"])):
            if elmt == historique[long - 1] and type(elmt["content"]) != str:
                content = st.write_stream(elmt["content"])
                elmt["content"] = content + "\n"
                st.session_state.audiopath.append("")
            else:
                st.write('<p>' + elmt["content"] + '</p>', unsafe_allow_html=True)
            i += 1
    # React to user input
    if message := st.chat_input("Intervention de l'Animateur :"):
        # Add user message to chat historique
        print(historique)
        addtohistorique(st.session_state.agentname, st.session_state.nameconversation, "human", message)
        try :
            response = call_llm(message, st.session_state.apibase, st.session_state.agentmodel, st.session_state.agentkey, historique, st.session_state.context)
            addtohistorique(st.session_state.agentname, st.session_state.nameconversation, "assistant", response)
        except Exception as error:
            st.warning("Error in the call of LLM")
            print(error)

        st.rerun()

if 'agentname' not in st.session_state:
    st.header("You don't have an agent in charge")
    with st.spinner('Redirection in progress'):
        time.sleep(2)
    st.switch_page("subpages/Agents.py")

with st.sidebar:
    st.header("Your conversation histories")
    conversations = getconversations(st.session_state.agentname)
    for conversation in conversations:
        if st.button(conversation):
            st.session_state.nameconversation = conversation
            st.session_state.historique = gethistorique(st.session_state.agentname, st.session_state.nameconversation)
    if st.button("Add a conversation"):
        dialogtoaddconversation()

st.title(f"Your agent : {st.session_state.agentname}")
st.header(f"Your Api Base : {st.session_state.apibase}")
st.header(f"Model : {st.session_state.agentmodel}")

if 'nameconversation' not in st.session_state:
    st.session_state.nameconversation = getfirstconversation(st.session_state.agentname)

st.session_state.context = "Tu es un assistant d'aide"
historique = gethistorique(st.session_state.agentname, st.session_state.nameconversation)
with st.container(border=True, height=800):
    generate_chat()




