import streamlit as st

st.title('Votre tableau de bord')

col1, col2 = st.columns(2)
with col1 :
    if st.button('Vos Agents') :
        st.switch_page('subpages/Agents.py')
with col2 :
    st.button('Votre emploi du temps')