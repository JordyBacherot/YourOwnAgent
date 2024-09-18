import streamlit as st
import time
import os
import sys

# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Importer la fonction depuis ToJson.py
from Utils.Tojson import gethistorique, addtohistorique, getconversations, addconversation, getfirstconversation, \
    deleteconversation, get_context, set_context
from Utils.LLM import call_llm, download_model_ollama



# Functions
#-------------------------------------------------#

@st.dialog("Add a conversation")
def dialogtoaddconversation():
    st.session_state.newconversationname = st.text_input("Please enter the name of the conversation")
    st.session_state.newcontext = st.text_area("Please enter the context of the conversation", value = "Réponds en Français. Tu es un chatbot d'assistance à un humain.")
    if st.button("Add the conversation") and st.session_state.newconversationname != "" and st.session_state.newcontext != "":
        addconversation(st.session_state.agentname, st.session_state.newconversationname, st.session_state.newcontext)
        st.session_state.nameconversation = st.session_state.newconversationname
        st.session_state.historique = gethistorique(st.session_state.agentname, st.session_state.nameconversation)
        st.rerun()
    else :
        st.warning("Please fill the name of the conversation and the context")

def generate_chat_stream():
    # Display chat messages from historique on app
    long = len(st.session_state.historique)
    i = 0
    for elmt in st.session_state.historique:
        with (st.chat_message(elmt["role"])):
                if elmt == st.session_state.historique[long - 1] and type(elmt["content"]) != str:
                    content = st.write_stream(elmt["content"])
                    elmt["content"] = content + "\n"
                    addtohistorique(st.session_state.agentname, st.session_state.nameconversation, "assistant",
                                    elmt["content"])
                else:
                    st.write('<p>' + elmt["content"] + '</p>', unsafe_allow_html=True)
                c1, c2 = st.columns([2,1])
                i += 1
    # React to user input
    if message := st.chat_input("Intervention de l'Animateur :"):
        # Add user message to chat historique
        addtohistorique(st.session_state.agentname, st.session_state.nameconversation, "human", message)
        if st.session_state.apibase == "ollama":
            response = call_llm(message, st.session_state.apibase, st.session_state.agentmodel, st.session_state.historique,
                                st.session_state.context)
        else:
            response = call_llm(message, st.session_state.apibase, st.session_state.agentmodel, st.session_state.historique,
                                st.session_state.context, st.session_state.agentkey)
        if response == "The model you are trying is not downloaded, start of the download":
            st.warning("The model you are trying is not downloaded, start of the download")
            with st.spinner("The model is downloading, it can be long, depending on your connection speed"):
                download_model_ollama(st.session_state.agentmodel)
        elif response == "An error occured in the call of the LLM":
            st.warning("An error occured in the call of the LLM")
        else:
            st.session_state.save_reply = response
        st.rerun()

# End of functions
#-------------------------------------------------#

st.title("🤖 Your Own Agent")
st.header("Your Agents")

if 'agentname' not in st.session_state:
    st.header("You don't have an agent in charge")
    with st.spinner('Redirection in progress'):
        time.sleep(2)
    st.switch_page("subpages/Agents.py")

with st.sidebar:
    st.header("Your conversation histories")
    conversations = getconversations(st.session_state.agentname)
    for conversation in conversations:
        with st.container(height=100):
            if st.button(f"Go to {conversation}"):
                st.session_state.nameconversation = conversation
                st.session_state.historique = gethistorique(st.session_state.agentname, st.session_state.nameconversation)
                st.rerun()
            if st.button(f"Delete {conversation}"):
                deleteconversation(st.session_state.agentname, conversation)
                st.session_state.nameconversation = getfirstconversation(st.session_state.agentname)
                st.session_state.historique = gethistorique(st.session_state.agentname, st.session_state.nameconversation)
                st.rerun()
    if st.button("Add a conversation"):
        dialogtoaddconversation()

st.title(f"Your agent : {st.session_state.agentname}")
st.header(f"Your Api Base : {st.session_state.apibase}")
st.header(f"Model : {st.session_state.agentmodel}")

if 'nameconversation' not in st.session_state:
    st.session_state.nameconversation = getfirstconversation(st.session_state.agentname)

st.session_state.context = get_context(st.session_state.agentname, st.session_state.nameconversation)
st.session_state.newcontext = st.text_area(label = "Context Window (permit to give to LLM a context for the conversation) ", value = st.session_state.context)
if st.button("Update the context"):
    set_context(st.session_state.agentname, st.session_state.nameconversation, st.session_state.newcontext)
    st.rerun()

with st.container(border=True, height=800):
    generate_chat_stream()





