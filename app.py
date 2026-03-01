"""Main entry point for the Crystal Structure Explorer Streamlit app."""

import streamlit as st

from components.sidebar import render_sidebar


# Configure the Streamlit page.
st.set_page_config(page_title="Crystal Structure Explorer", layout="wide")

# App title.
st.title("Crystal Structure Explorer")

# Render sidebar content.
render_sidebar()

# File uploader for CIF files.
uploaded_file = st.file_uploader(
    "Upload a CIF file",
    type=["cif"],
    help="Choose a crystallographic information file (.cif) to explore.",
)

# Placeholder app content.
if uploaded_file is not None:
    st.info("CIF file uploaded. Structure parsing and analysis features are coming soon.")
else:
    st.write("Upload a CIF file to begin exploring crystal structure data.")
