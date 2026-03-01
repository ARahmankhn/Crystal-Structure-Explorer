"""UI components for displaying parsed structure information."""

from __future__ import annotations

import streamlit as st
from pymatgen.core import Structure


def display_results(structure: Structure) -> None:
    """Display basic structure information.

    Args:
        structure: Parsed pymatgen structure to summarize in the UI.
    """
    st.subheader("Structure Information")

    # Show core crystal statistics so users can confirm successful parsing.
    st.write(f"Formula: {structure.composition.reduced_formula}")
    st.write(f"Lattice parameters: {structure.lattice.parameters}")
    st.write(f"Volume: {structure.lattice.volume:.3f} Å³")
    st.write(f"Number of sites: {len(structure.sites)}")
