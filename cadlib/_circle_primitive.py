# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from ._schema_model import SchemaModel
from ._vector3 import Vector3


class CirclePrimitive(SchemaModel):
    """
    Circle approximating a planar patch
    """

    center: Vector3
    """
    Center of the circle
    """
    radius: float
    """
    Radius of the circle
    """
    normal: Vector3
    """
    Outward normal of the patch
    """
