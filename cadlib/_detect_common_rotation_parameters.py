# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from ._schema_model import SchemaModel


class DetectCommonRotationParameters(SchemaModel):
    """
    Parameters for detect rotation query
    """

    faces: list[str]
    """
    Ids of the faces to check for common rotation, as `entities` returns them. The query will check if these faces are rotationally aligned and share the same rotation center and axis. Must not be empty
    """
