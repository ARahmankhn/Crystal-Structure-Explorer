"""Main entry point for the Crystal Structure Explorer Streamlit app."""

import streamlit as st

from components.results import display_results
from components.sidebar import render_sidebar


def main() -> None:
    """Initialize and render the Streamlit user interface."""
    # Basic page metadata.
    st.set_page_config(page_title="Crystal Structure Explorer", layout="wide")

    # Main page title.
    st.title("Crystal Structure Explorer")

    # Sidebar placeholder controls.
    render_sidebar()

    # Upload control for CIF files.
    uploaded_file = st.file_uploader("Upload a CIF file", type=["cif"])

    # Placeholder feedback area.
    if uploaded_file is None:
        st.info("Upload a CIF file to start exploring crystal structure properties.")
    else:
        st.success("CIF file uploaded successfully. Analysis placeholders are shown below.")

    # Placeholder results panel.
    display_results()


if __name__ == "__main__":
    main()
