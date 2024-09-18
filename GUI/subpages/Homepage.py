import streamlit as st
import sys
import os
from streamlit_extras.stylable_container import stylable_container


# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

st.title("🤖 Your Own Agent")
st.header("Homepage")

col1, col2, col3, col4, col5 = st.columns([1, 3, 1, 3, 1])
with col2 :
    with st.container(border=False):
        st.write("")
        st.write("")
        with stylable_container(
                "blue",
                css_styles="""
                    button {
                        color: #faa53c;
                        height: 80px;
                    }""",
        ):
            if st.button(r"$\textsf{\Large Access to your Agents}$", use_container_width=True):

                st.switch_page('subpages/Agents.py')
with col4:
    with st.container(border=False):
        st.write("")
        st.write("")
        with stylable_container(
                "blue",
                css_styles="""
                            button {
                                color: #faa53c;
                                height: 80px;
                            }""",
        ):
            if st.button(r"$\textsf{\Large Access to your schedule}$", use_container_width=True):
                st.switch_page('subpages/Agents.py')