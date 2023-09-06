import streamlit as st
from projectPage import project_page
from sequencePage import sequences_page
from system_page import systems_page
from analyses_page import analyses_page
from report_page import report_page



pages = {
    "🧬 Project": project_page,
    "🧬 Sequences": sequences_page,
    "🧬 Analyses": analyses_page,
    "🧬 Report": report_page,
    "🧬 Systems": systems_page,
}

col1, col2 = st.columns(2)
with col1:
    st.header('Project Page', divider='rainbow')
with col2 :
    st.image('https://www.innodeep.net/wp-content/uploads/2022/03/logo2-removebg-preview.png', use_column_width=True)

selected_page = st.sidebar.selectbox("Navigate through the project", list(pages.keys()))

pages[selected_page]()