import streamlit as st

st.title('Votre tableau de bord')

col1, col2 = st.columns(2)
with col1 :
    if st.button('Vos Agents') :
        a=2
with col2 :
    st.button('Votre emploi du temps')

