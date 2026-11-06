# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from ._schema_model import SchemaModel
from ._vector3 import Vector3


class CenterOfGravityResponse(SchemaModel):
    """
    Response for compute center of gravity query
    """

    cog: Vector3
    """
    Center of gravity as a 3D vector
    """
