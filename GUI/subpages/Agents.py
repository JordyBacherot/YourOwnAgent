import streamlit as st
import sys
import os

from streamlit_extras.customize_running import center_css
from streamlit_extras.stylable_container import stylable_container

# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Importer la fonction depuis ToJson.py
from Utils.Tojson import get_key, add_key, create_an_agent, get_all_agents, delete_agent, get_keys, delete_key, getfirstconversation, gethistorique


# Functions
#-------------------------------------------------#

@st.dialog("Add a key")
def dialog_create_key():
    model_ids = [
        "groq",
        "openai",
    ]
    st.session_state.newapibase = st.selectbox("Please enter the api base of your key", model_ids)
    st.session_state.newkeyname = st.text_input("Please enter your name key")
    st.session_state.newkey = st.text_input("Please enter your key")
    with stylable_container(
            "add_key",
            css_styles="""
                        button {
                            color:  #84996a;
                            border: 2px solid #9CB380;
                            height: 60px;
                        }""",
    ):
        if st.button("Add the key", use_container_width=True):
            verify = add_key(st.session_state.newapibase, st.session_state.newkeyname, st.session_state.newkey)
            if not verify:
                st.write("This key name already exist")
            else:
                st.write("The key has been added")
    with stylable_container(
            "info",
            css_styles="""
                            button {
                                color:  #6483cc;
                                border: 2px solid #6483cc;
                                height: 60px;
                            }""",
    ):
        if st.button("Where can I find my key ?", use_container_width=True):
            st.info("You have to create an account on the website Groq or OpenAI (not free) and go to the API section to get your key")

@st.dialog("Create an agent with Groq")
def dialog_create_groq_agent():
    keynames = get_key("groqkey")
    if keynames is not None:
        st.session_state.keyname = st.selectbox("Choose a key name", keynames)
        st.session_state.key = keynames[st.session_state.keyname]
    else :
        st.info("You have to add a key")
    cola, colb = st.columns([1, 1])
    with cola :
        with stylable_container(
                "refresh",
                css_styles="""
                                button {
                                    color: #d68622;
                                    height: 40px;
                                    border: 2px solid #d68622;
                                }""",
        ):
            st.button("Refresh the keys", use_container_width=True)
    with colb :
        with stylable_container(
                "addakey",
                css_styles="""
                                button {
                                    color:  #84996a;
                                    border: 2px solid #9CB380;
                                    height: 40px;
                                }""",
        ):
            if st.button("Add a key", use_container_width=True):
                st.session_state.start_dialogue_key = True
                st.rerun()
    model_ids = [
        "gemma2-9b-it",
        "llama3-70b-8192",
        "llama3-8b-8192",
        "mixtral-8x7b-32768",
    ]
    st.session_state.model = st.selectbox("Please enter the model you want to use", model_ids)
    st.session_state.agentname = st.text_input("Please enter the name of your agent")
    with stylable_container(
            "addakey",
            css_styles="""
                button {
                    color:  #84996a;
                    border: 2px solid #9CB380;
                    height: 40px;
                }""",
    ):
        if st.button("Create the agent", use_container_width=True):
            if st.session_state.keyname != "" and st.session_state.key != "" and st.session_state.agentname != "":
                verify = create_an_agent("groq", st.session_state.agentname, st.session_state.model, st.session_state.key)
                if verify:
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
        st.session_state.keyname = st.selectbox("Choose a key name", keynames)
        st.session_state.key = keynames[st.session_state.keyname]
    else:
        st.info("You have to add a key")
    cola, colb = st.columns([1, 1])
    with cola:
        with stylable_container(
                "refresh",
                css_styles="""
                                        button {
                                            color: #d68622;
                                            height: 40px;
                                            border: 2px solid #d68622;
                                        }""",
        ):
            st.button("Refresh the keys", use_container_width=True)
    with colb:
        with stylable_container(
                "addakey",
                css_styles="""
                                        button {
                                            color:  #84996a;
                                            border: 2px solid #9CB380;
                                            height: 40px;
                                        }""",
        ):
            if st.button("Add a key", use_container_width=True):
                st.session_state.start_dialogue_key = True
                st.rerun()
    model_ids = [
        "gpt-4o",
        "gpt-4o-turbo",
        "gpt-4o-mini",
        "gpt-4",
        "gpt-3.5-turbo"
    ]
    st.session_state.model = st.selectbox("Please enter the model you want to use", model_ids)
    st.session_state.agentname = st.text_input("Please enter the name of your agent")
    with stylable_container(
            "addakey",
            css_styles="""
                    button {
                        color:  #84996a;
                        border: 2px solid #9CB380;
                        height: 40px;
                    }""",
    ):
        if st.button("Create the agent", use_container_width=True):
            if st.session_state.keyname != "" and st.session_state.key != "" and st.session_state.agentname != "":
                verify = create_an_agent("openai", st.session_state.agentname, st.session_state.model, st.session_state.key)
                if verify:
                    st.rerun()
                else:
                    st.warning("An agent with this name already exist")
            else:
                st.write("Key name : ", st.session_state.keyname)
                st.write("Key : ", st.session_state.key)
                st.write("Agent name : ", st.session_state.agentname)
                st.write("Model : ", st.session_state.model)
                st.warning("Please fill all the fields : Key Name, Key, Model and Agent name")

@st.dialog("Create an agent with Ollama")
def dialog_create_ollama_agent():
    st.warning("Be sure to have follow the tutorial, and have installed Ollama on your computer")
    st.divider()
    st.write("You don't need a key to use Ollama, because it's locally installed")
    st.divider()
    st.write("Be careful, models of 8b are heavy (4go), be sure to have a good computer")
    st.write("Be careful, models of 70b are really heavy (50go), be sure to have a strong computer")
    model_ids = [
        "llama3.1:8b",
        "gemma2:2b",
        "gemma2:9b",
        "mistral-nemo:12b",
        "qwen2:7b",
        "qwen2:1.5b",
        "llama3.1:70b",
    ]
    st.session_state.model = st.selectbox("Please enter the model you want to use", model_ids)
    st.session_state.agentname = st.text_input("Please enter the name of your agent")
    if st.button("Create the agent") :
        if  st.session_state.agentname != "":
            verify = create_an_agent("ollama", st.session_state.agentname, st.session_state.model)
            if verify:
                st.rerun()
            else :
                st.warning("An agent with this name already exist")
        else :
            st.write("Key name : ", st.session_state.keyname)
            st.write("Agent name : ", st.session_state.agentname)
            st.write("Model : ", st.session_state.model)
            st.warning("Please fill all the fields : Key Name, Key, Model and Agent name")

@st.dialog("Delete an agent")
def confirm_delete_agent(agentname):
    st.write("Are you sure you want to delete this agent ?")
    if st.button("Yes"):
        delete_agent(agentname)
        st.rerun()
    if st.button("No"):
        st.rerun()

def create_button_agent(agent):
    with st.container(border=True, height=270):
        st.write(r"$\textsf{\Large "+agent['agentname']+"}$")
        st.write(r"$\textsf{Api Base : "+ agent['apibase']+"}$")
        st.write(r"$\textsf{Model : "+ agent['agentmodel']+"}$")
        with stylable_container(
                "go_to_agent",
                css_styles="""
                    button {
                        color: #d68622;
                        height: 50px;
                        border: 2px solid #d68622;
                    }""",
        ):
            if st.button(f"Go to Agent : {agent['agentname']}", use_container_width=True):
                st.session_state.agentname = agent['agentname']
                st.session_state.apibase = agent['apibase']
                st.session_state.agentmodel = agent['agentmodel']
                if agent['apibase'] != "ollama":
                    st.session_state.agentkey = agent['agentkey']
                st.session_state.nameconversation = getfirstconversation(st.session_state.agentname)
                st.session_state.historique = gethistorique(st.session_state.agentname, st.session_state.nameconversation)
                st.switch_page("subpages/Youragent.py")
        with stylable_container(
                "delete_agent",
                css_styles="""
                            button {
                                color: #b0362e;
                                border: 2px solid #b0362e;
                                height: 30px;
                            }""",
        ):
            if st.button(f"Delete {agent['agentname']}", use_container_width=True):
                confirm_delete_agent(agent['agentname'])

@st.dialog("Delete a key")
def dialogue_delete_key():
    keys = get_keys()
    if keys is not None:
        st.session_state.deletekeyname = st.selectbox("Choose a key name", keys)
    else:
        st.write("You don't have any key")
        st.rerun()
    with stylable_container(
            "delete_agent",
            css_styles="""
                                button {
                                    color: #b0362e;
                                    border: 2px solid #b0362e;
                                    height: 30px;
                                }""",
    ):
        if st.button("Delete the key", use_container_width=True):
            delete_key(st.session_state.deletekeyname)
            st.rerun()



# End of functions
#-------------------------------------------------#

st.title("🤖 Your Own Agent")
st.header("Your Own Agents", divider="orange")

if "start_dialogue_key" not in st.session_state:
    st.session_state.start_dialogue_key = False

if st.session_state.start_dialogue_key == True:
    st.session_state.start_dialogue_key = False
    dialog_create_key()


c1, c2, c3 = st.columns([10, 1, 4])

with c3 :
    st.write("")
    st.subheader("Manage")
    with st.container(border=True):
        with stylable_container(
                "add",
                css_styles="""
                    button {
                        color:  #84996a;
                        border: 2px solid #9CB380;
                        height: 60px;
                    }""",
        ):
            if st.button("Add a Groq agent", use_container_width=True):
                dialog_create_groq_agent()

            if st.button("Add an OpenAI Agent", use_container_width=True):
                dialog_create_openai_agent()

            if st.button("Add an Ollama Agent", use_container_width=True):
                dialog_create_ollama_agent()
        with stylable_container(
                "delete",
                css_styles="""
                    button {
                        color: #b0362e;
                        border: 2px solid #b0362e;
                        height: 60px;
                    }""",
        ):
            if st.button("Delete a key", use_container_width=True):
                dialogue_delete_key()

with c1:
    st.write("")
    st.subheader("Agents")
    # View of all the agents
    dataAgents = get_all_agents()
    i=0
    col1 , col2, col3= st.columns(3)
    for agent in dataAgents:
        i +=1
        # modulo len
        match i % 3:
            case 1:
                with col1:
                    create_button_agent(agent)
            case 2:
                with col2:
                    create_button_agent(agent)
            case 0:
                with col3:
                    create_button_agent(agent)








