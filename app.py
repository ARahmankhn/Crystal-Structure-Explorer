"""Main entry point for the Crystal Structure Explorer Streamlit app."""

import streamlit as st

from components.sidebar import render_sidebar


# Configure the Streamlit page.
st.set_page_config(page_title="Crystal Structure Explorer", layout="wide")

# App title.
st.title("Crystal Structure Explorer")

# Render sidebar content.
render_sidebar()

# Main uploader section.
st.subheader("Upload a CIF File")
uploaded_file = st.file_uploader(
    "Choose a CIF file to explore crystal structures", type=["cif"]
)

# Placeholder output in the main content area.
if uploaded_file is not None:
    st.info("CIF file uploaded successfully. Structure parsing will be added soon.")
else:
    st.write("Upload a CIF file from the sidebar area to begin exploring.")
