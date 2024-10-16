import altair as alt
import streamlit as st
import sys
import os
from streamlit_extras.stylable_container import stylable_container



# Ajouter le répertoire parent du projet au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Utils.Tojson import get_tasks, add_task, change_task_warning_level, change_task_status, delete_task, get_data_week_points

@st.dialog("Add a Task")
def dialog_add_task():
    st.session_state.newtasktitle = st.text_input("Please enter the title of the task")
    st.session_state.newtaskdescription = st.text_area("Please enter the description of the task")
    st.session_state.warning_level = st.selectbox("Warning Level", ["Low", "Medium", "High"])
    st.session_state.points = st.number_input("Points", min_value=1, max_value=8)
    if st.button("Add the task") and st.session_state.newtasktitle != "" and st.session_state.newtaskdescription != "":
        add_task(st.session_state.newtasktitle, st.session_state.newtaskdescription, st.session_state.warning_level, st.session_state.points)
        st.rerun()
    else :
        st.warning("Please fill the title and the description")

@st.dialog("Modif on the task")
def modif_task():
    st.session_state.warning_level = st.selectbox("Warning Level", ["Low", "Medium", "High"])
    with stylable_container(
            "button1",
            css_styles="""
                    button {
                        color: #d68622;
                        height: 50px;
                        border: 2px solid #d68622;
                    }""",
    ):
        if st.button(f"Change the warning level of {st.session_state.actualtask["name"]}"):
            change_task_warning_level(st.session_state.actualtask["name"], st.session_state.warning_level)
            st.rerun()
    st.session_state.statistask = st.selectbox("Status", ["To Do", "In Progress", "Done"])
    with stylable_container(
            "button1",
            css_styles="""
                        button {
                            color: #d68622;
                            height: 50px;
                            border: 2px solid #d68622;
                        }""",
    ):
        if st.button(f"Change the status of {st.session_state.actualtask["name"]}"):
            change_task_status(st.session_state.actualtask["name"], st.session_state.statistask)
            st.rerun()
    with stylable_container(
            "button2",
            css_styles="""
                    button {
                        color: #b0362e;
                        border: 2px solid #b0362e;
                        height: 30px;
                    }""",
    ):
        if st.button("Delete the task"):
            delete_task(st.session_state.actualtask["name"])
            st.rerun()


st.title("🤖 Your Own Agent")

st.header("Your Tasks", divider="orange")

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
            dialog_add_task()

st.session_state.taskToDo = []
st.session_state.taskInProgress = []
st.session_state.taskDone = []
st.session_state.lastTask = []

tasks = get_tasks()
for task in tasks:
    if task["status"] == "To Do":
        st.session_state.taskToDo.append(task)
    elif task["status"]  == "In Progress":
        st.session_state.taskInProgress.append(task)
    elif task["status"]  == "Done":
        st.session_state.taskDone.append(task)
    else :
        st.session_state.lastTask.append(task)

st.session_state.taskToDo.sort(key=lambda x: x["warning_level"])
st.session_state.taskInProgress.sort(key=lambda x: x["warning_level"])
st.session_state.taskDone.sort(key=lambda x: x["warning_level"])

col1, col2, col3, col4 = st.columns([2,2,2,4])

with st.container():
    with col1 :
        st.subheader("To Do")
        with st.container(border=True, height=500):
            for task in st.session_state.taskToDo:
                    with st.expander(r"$\textsf{\large "+task["name"]+"}$"):
                        st.write(f"Description : {task["description"]}")
                        st.write(f"Points : {task['points']}")
                        if st.button(f"Modification on {task["name"]}"):
                            st.session_state.actualtask = task
                            modif_task()
    with col2 :
        st.subheader("In Progress")
        with st.container(border=True, height=500):
            for task in st.session_state.taskInProgress:
                with st.expander(r"$\textsf{\large " + task["name"] + "}$"):
                    st.write(f"Description : {task["description"]}")
                    st.write(f"Points : {task['points']}")
                    if st.button(f"Modification on {task["name"]}"):
                        st.session_state.actualtask = task
                        modif_task()
    with col3 :
        st.subheader("Done")
        with st.container(border=True, height=500):
            for task in st.session_state.taskDone:
                with st.expander(r"$\textsf{\large " + task["name"] + "}$"):
                    st.write(f"Description : {task["description"]}")
                    st.write(f"Points : {task['points']}")
                    if st.button(f"Modification on {task["name"]}"):
                        st.session_state.actualtask = task
                        modif_task()

    with col4:
        data = get_data_week_points()
        print(data)
        st.subheader("Your Statistics")
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X('date', sort=None, title="Day of week"),
            y=alt.Y('points', title="Points"),
        ), use_container_width=True)




