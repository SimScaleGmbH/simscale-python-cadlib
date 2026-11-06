# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._schema_model import SchemaModel
from ._vector3 import Vector3


class TessellateFacesResponse(SchemaModel):
    """
    Response for the tessellate faces query
    """

    face_normals: dict[str, Vector3] = Field(..., alias="faceNormals")
    """
    Unit normal of each requested face, evaluated at the mid point of the
    face, keyed by face id
    """
