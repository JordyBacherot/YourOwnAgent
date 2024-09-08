import streamlit as st

pages = {
    "Welcome": [
        st.Page("pages/Homepage.py", title="Homepage"),
        st.Page("pages/Tutorial.py", title="Tutorial"),
    ],
    "Agents": [
        st.Page("pages/Agents.py", title="Agents"),
        st.Page("pages/YourAgent.py", title="Your Agent"),
    ],
}

pg = st.navigation(pages)
pg.run()
