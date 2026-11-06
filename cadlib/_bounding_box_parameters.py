# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from ._schema_model import SchemaModel


class BoundingBoxParameters(SchemaModel):
    """
    Parameters for bounding box info query
    """

    faces: list[str] | None = None
    """
    Ids of faces to measure in addition to the model and its bodies. When
    given, the response also holds the box enclosing all of them and one box
    per face
    """
