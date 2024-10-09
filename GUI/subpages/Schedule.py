import streamlit as st
import sys
import os
from streamlit_calendar import calendar
from streamlit_extras.stylable_container import stylable_container



# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Utils.Tojson import get_calendar_data, add_event_calendar

@st.dialog("Add an event")
def dialog_add_event():
    st.session_state.neweventtitle = st.text_input("Please enter the title of the event")
    st.session_state.newdateeventstart = st.date_input("Please enter the start date of the event")
    st.session_state.newdateeventend = st.date_input("Please enter the end date of the event")
    print(st.session_state.newdateeventstart, st.session_state.newdateeventend)

    st.session_state.newtimeeventstart = st.time_input("Please enter the start time of the event")
    st.session_state.newtimeeventend = st.time_input("Please enter the end time of the event")
    print(st.session_state.newtimeeventstart, st.session_state.newtimeeventend)
    if st.button("Add the event") and st.session_state.neweventtitle != "" and st.session_state.newdateeventstart != "" and st.session_state.newdateeventend != "" and st.session_state.newtimeeventstart != "" and st.session_state.newtimeeventend != "":
        add_event_calendar(st.session_state.neweventtitle, str(st.session_state.newdateeventstart), str(st.session_state.newdateeventend), str(st.session_state.newtimeeventstart), str(st.session_state.newtimeeventend))
        st.rerun()
    else :
        st.warning("Please fill the title and the dates")



st.title("🤖 Your Own Agent")

st.header("Schedule", divider="orange")
with st.container():
    with stylable_container(
            "add",
            css_styles="""
                        button {
                            color: white;
                            height: 60px;
                            background-color: #c97712;
                        }""",
    ):
        if st.button("Add an event", use_container_width=True):
            dialog_add_event()
data = get_calendar_data()
calendar_events = data['calendar_events']
calendar_options = data['calendar_options']

custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""

calendar = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)

