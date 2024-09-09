import streamlit as st

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

pg = st.navigation(pages)
pg.run()
