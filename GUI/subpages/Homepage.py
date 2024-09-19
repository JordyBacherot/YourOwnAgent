import streamlit as st
import sys
import os
from streamlit_extras.stylable_container import stylable_container


# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

st.title("🤖 Your Own Agent")
st.header("Homepage", divider="orange")

col1, col2, col3, col4, col5 = st.columns([1, 3, 1, 3, 1])
with col2 :
    with st.container(border=False):
        st.write("")
        st.write("")
        st.write("")
        with stylable_container(
                "access_agent",
                css_styles="""
                    button {
                        color: #d68622;
                        height: 80px;
                        border: 2px solid #d68622;
                    }""",
        ):
            if st.button(r"$\textsf{\Large Access to your Agents}$", use_container_width=True):

                st.switch_page('subpages/Agents.py')
with col4:
    with st.container(border=False):
        st.write("")
        st.write("")
        st.write("")
        with stylable_container(
                "access_shcedule",
                css_styles="""
                            button {
                                color: #d68622;
                                height: 80px;
                                border: 2px solid #d68622;
                            }""",
        ):
            if st.button(r"$\textsf{\Large Access to your schedule}$", use_container_width=True):
                st.switch_page('subpages/Agents.py')