# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from enum import StrEnum


class TessellationType(StrEnum):
    """
        Tessellation strategy (Supported only for Parasolid models)
    `ChordTol` controls curve tolerance by specifying the maximum allowable distance between a true curved edge
    and the straight-line chords (facet edges) used to approximate it.
    The `MaxFacetWidth` strategy uses a maximum facet width to control the maximum size of the facets, which can be more intuitive in some cases.
    When using `MaxFacetWidth`, the `maxFacetWidth` parameter controls the maximum width of the facets.
    """

    CHORD_TOL = "chordTol"
    MAX_FACET_WIDTH = "maxFacetWidth"
