import streamlit as st

import os
import sys

# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from Utils.Tojson import get_first_access, set_first_access

if get_first_access():
    set_first_access()
    pages = {
        "Welcome": [
            st.Page("subpages/Tutorial.py", title="Tutorial"),
            st.Page("subpages/Homepage.py", title="Homepage"),
        ],
        "Agents": [
            st.Page("subpages/Agents.py", title="Agents"),
            st.Page("subpages/YourAgent.py", title="Your Agent"),
        ],
    }
else :
    pages = {
        "Welcome": [
            st.Page("subpages/Homepage.py", title="Homepage"),
            st.Page("subpages/Tutorial.py", title="Tutorial"),
        ],
        "Agents": [
            st.Page("subpages/Agents.py", title="Agents"),
            st.Page("subpages/YourAgent.py", title="Your Agent"),
        ],
    }

st.set_page_config(
    page_title="Your Own Agent",
    page_icon="🤖",
    layout="wide",
)

pg = st.navigation(pages)
pg.run()
