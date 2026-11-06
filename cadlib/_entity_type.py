# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from enum import StrEnum


class EntityType(StrEnum):
    """
        Type of entity. A body is never part of the topology, since it is
    represented by its top-level solids or sheets.
    """

    SOLID = "SOLID"
    SHEET = "SHEET"
    FACE = "FACE"
    EDGE = "EDGE"
    VERTEX = "VERTEX"
