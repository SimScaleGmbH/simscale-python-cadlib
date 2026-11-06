# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from ._schema_model import SchemaModel
from ._vector3 import Vector3


class DetectCommonRotationResponse(SchemaModel):
    """
    Response for detect common rotation query
    """

    center: Vector3
    """
    Center of common rotation
    """
    axis: Vector3
    """
    Axis of common rotation
    """
