import streamlit as st
import time
import os
import sys
from streamlit_extras.stylable_container import stylable_container

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
        with stylable_container(
                "add",
                css_styles="""
                    .stChatMessage {
                        border: 1px solid #ebc89d;
                    }""",
        ):
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

@st.dialog("Delete a conversation")
def confirm_delete_conversation(agentname, conversation):
    st.write("Are you sure you want to delete this conversation ?")
    with stylable_container(
            "delete_yes",
            css_styles="""
                button {
                    color: #b0362e;
                    border: 2px solid #b0362e;
                    height: 30px;
                }""",
    ):
        if st.button("Yes", use_container_width=True):
            deleteconversation(agentname, conversation)
            st.session_state.nameconversation = getfirstconversation(st.session_state.agentname)
            st.session_state.historique = gethistorique(st.session_state.agentname, st.session_state.nameconversation)
            st.rerun()
    with stylable_container(
            "delete_no",
            css_styles="""
                button {
                    color:  #84996a;
                    border: 2px solid #9CB380;
                    height: 30px;
                }""",
    ):
        if st.button("No", use_container_width=True):
            st.rerun()

# End of functions
#-------------------------------------------------#

st.title("🤖 Your Own Agent")

if 'agentname' not in st.session_state:
    st.header("You don't load any agent")
    with st.spinner('Redirection in progress'):
        time.sleep(3)
    st.switch_page("subpages/Agents.py")

st.header(f"Your Agent : {st.session_state.agentname} ", divider="orange")


with st.sidebar:
    st.title("Your conversation histories")
    conversations = getconversations(st.session_state.agentname)
    for conversation in conversations:
        with stylable_container(
            "go_to_agent",
            css_styles="""
                button {
                    color: #d68622;
                    height: 50px;
                    border: 2px solid #d68622;
                    background-color: #fff8e6;
                }""",
        ):
            if st.button(f"Go to {conversation}", use_container_width=True):
                st.session_state.nameconversation = conversation
                st.session_state.historique = gethistorique(st.session_state.agentname, st.session_state.nameconversation)
                st.rerun()
    with stylable_container(
        "add",
        css_styles="""
            button {
                color:  #84996a;
                border: 2px solid #9CB380;
                height: 60px;
                background-color: #fff8e6;
            }""",
    ):
        if st.button("Add a conversation", use_container_width=True):
            dialogtoaddconversation()

col1, col2 = st.columns(2)
with col1:
    st.write("")
    st.markdown("#### Api Base : "+st.session_state.apibase)
    st.markdown("#### Model : "+st.session_state.agentmodel)

if 'nameconversation' not in st.session_state:
        st.session_state.nameconversation = getfirstconversation(st.session_state.agentname)

with col2:
    st.session_state.context = get_context(st.session_state.agentname, st.session_state.nameconversation)
    st.session_state.newcontext = st.text_area(label = "Context Window (permit to give to LLM a context for the conversation) ", value = st.session_state.context)
    with stylable_container(
        "add_conv",
        css_styles="""
            button {
                color: #d68622;
                height: 30px;
                border: 2px solid #d68622;
            }""",
    ):
        if st.button("Update the context", use_container_width=True):
            set_context(st.session_state.agentname, st.session_state.nameconversation, st.session_state.newcontext)
            st.rerun()

with st.container(border=True, height=800):
    generate_chat_stream()


st.write("")
with stylable_container(
        "delete",
        css_styles="""
            button {
                color: #b0362e;
                border: 2px solid #b0362e;
                height: 30px;
            }""",
):
    if st.button(f"Delete this conversation : {conversation}", use_container_width=True):
        confirm_delete_conversation(st.session_state.agentname, st.session_state.nameconversation)







