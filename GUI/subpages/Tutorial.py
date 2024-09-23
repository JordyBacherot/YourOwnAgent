import streamlit as st
import os
import sys

# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


st.title("🤖 Your Own Agent")
st.header("Tutorial", divider="orange")

st.subheader("Welcome to Your Own Agent (YOA)")

st.markdown(
    """
    This tutorial will show you **how to use our application**, and how add IA agents to help you work more efficiently and accurately.\n
    We'll take you through the basics of our application and how to get the most out of it.\n
    
    Firstly what is an agent ?\n
    An agent, in this application, is a AI system build on AI Large Language Models (LLM) that can help you in your daily tasks ans solving problems with textual response.\n
    """
)

st.divider()

st.subheader("How add an **Groq** Agent (Free) ?")
col1, col2 = st.columns(2)
with col1:
    st.write("")
    st.markdown(
        """
        What is **Groq** ?\n
        Groq is an entreprise that provide a free API to use their LPU (Language Processing Unit, calculator specialised in LLM models).\n

        To add an agent with Groq, you need to have an account on their website (here: : **https://groq.com/**).\n
        After that go to the API section and create a new API key (here : **https://console.groq.com/keys**).\n\n

        And **save the key** you just created.\n\n
        """
    )
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(
        """
        After you can **go to the "Agents"** section of the application and click on the **"Add a Groq Agent"** button.\n
        Follow your instruction and add your key to the agent.\n

        **Congrats** you can now use your agent to help you in your daily tasks.\n
        """
    )

with col2:
    st.image("Tutorial_Image/Groq_key.png")
    st.image("Tutorial_Image/Add_a_model.png")

st.divider()

st.subheader("How add an Ollama Agent (Free) ?")
col1, col2 = st.columns(2)
with col1 :
    st.markdown(
        """
        What is **Ollama** ?\n
        Ollama is a software that provide a local access to use different (open/free) LLM's.\n
        
        Firstly you need to **download** the software on their website (https://ollama.com/).\n
        
        After tou just have to start it and you can use it in the application.\n
        """
    )
with col2 :
    st.image("Tutorial_Image/See_Ollama.png")

st.divider()

st.subheader("How add an **OpenAI** Agent (Not Free) ?")

st.markdown(
    """
    The same way as Groq, OpenAI is an **entreprise that provide a paid API** to use their LLM models.\n
    To add an agent with OpenAI, you need to have a **premium** account on their website (**https://openai.com/**).\n
    After that go to the API section and create a new API key (here : **https://platform.openai.com/account/api-keys**).\n
    Save the key you just created.\n
    Finally just create your agent and add the key to it.\n
    """
)