import streamlit as st
import time

if 'agentname' not in st.session_state:
    st.header("You do not have an agent in charge")
    with st.spinner('Redirection in progress'):
        time.sleep(3)
    st.switch_page("pages/Agents.py")

with st.sidebar:
    st.header("Your conversation histories")

st.title(f"Your agent : {st.session_state.agentname}")
st.header(f"Your Api Base : {st.session_state.apibase}")
st.header(f"Model : {st.session_state.agentmodel}")


