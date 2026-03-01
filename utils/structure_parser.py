"""Utilities for loading crystal structures from CIF files."""

from __future__ import annotations

from pathlib import Path
from typing import BinaryIO, Union

from pymatgen.core import Structure


FileLike = Union[str, Path, BinaryIO]


def load_structure(file: FileLike) -> Structure:
    """Load a crystal structure from a CIF file using pymatgen.

    Args:
        file: Path or file-like object for a CIF file.

    Returns:
        Parsed ``Structure`` object.

    Raises:
        ValueError: If parsing fails or the file is not a valid CIF.
    """
    try:
        # Delegate CIF parsing to pymatgen's robust file loader.
        structure = Structure.from_file(file)
        return structure
    except Exception as e:  # pragma: no cover - defensive wrapper for UI flow
        # Normalize parser errors for clean handling in Streamlit.
        raise ValueError(f"Invalid CIF file: {e}") from e
