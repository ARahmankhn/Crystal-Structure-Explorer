"""Sidebar UI components for the Crystal Structure Explorer app."""

import streamlit as st


def render_sidebar():
    """Render a simple app sidebar with title and description."""
    st.sidebar.title("Crystal Structure Explorer")
    st.sidebar.write(
        "Use this panel to upload CIF files and configure analysis options "
        "in future versions."
    )
