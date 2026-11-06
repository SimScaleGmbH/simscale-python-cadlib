# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from ._schema_model import SchemaModel
from ._vector3 import Vector3


class RectanglePrimitive(SchemaModel):
    """
    Rectangle approximating a planar patch
    """

    corners: list[Vector3]
    """
    The four corners of the rectangle, counterclockwise around `normal`
    """
    normal: Vector3
    """
    Outward normal of the patch
    """
