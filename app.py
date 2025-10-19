# app.py
import streamlit as st

st.set_page_config(
    page_title="Discordlit Tools",
    page_icon="🛠️"
)

st.title("Welcome to Discordlit Tools! 🛠️")

st.sidebar.success("Select a tool above.")

st.markdown(
    """
    This is a collection of tools designed to help with Empires & Puzzxes Discord formatting and utilities.
    
    **👈 Select a tool from the sidebar** to get started.
    
    ### Available Tools
    - Emoji List: Browse and filter a custom list of emojis used in SGG Discord servers.
    - **Table Formatter**: Convert table data copied from Google Sheets into a Discord-friendly monospaced format.
    
    ---
    
    *More tools will be added in the future! - BirksG*
    """
)