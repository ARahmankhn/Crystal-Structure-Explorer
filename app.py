"""Main Streamlit application entry point."""

from __future__ import annotations

import streamlit as st

from components.results import display_results
from utils.structure_parser import load_structure


def main() -> None:
    """Run the Crystal Structure Explorer app."""
    st.set_page_config(page_title="Crystal Structure Explorer", layout="centered")
    st.title("Crystal Structure Explorer")
    st.write("Upload a CIF file to parse and inspect basic structure information.")

    # Let users provide a CIF file for parsing.
    uploaded_file = st.file_uploader("Upload CIF file", type=["cif"])

    if uploaded_file is not None:
        try:
            # Parse the uploaded file and render structure summary.
            structure = load_structure(uploaded_file)
            display_results(structure)
        except ValueError as exc:
            # Display parser-related issues in a user-friendly way.
            st.error(str(exc))
        except Exception as exc:  # pragma: no cover - unexpected runtime issues
            # Catch all unexpected errors to avoid app crashes.
            st.error(f"Unexpected error while processing file: {exc}")


if __name__ == "__main__":
    main()
