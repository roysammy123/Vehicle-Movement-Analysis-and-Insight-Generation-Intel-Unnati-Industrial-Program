import streamlit as st
import pages
from menu import menu

st.set_page_config(
    page_title="Vehicle Registration and Monitoring App",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state = "collapsed"
)

from pages import home
home.main()
