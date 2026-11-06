# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from typing import Any

from pydantic import Field

from ._box import Box
from ._schema_model import SchemaModel


class BoundingBoxResponse(SchemaModel):
    """
    Response for bounding box query
    """

    model_bounding_box: Box = Field(..., alias="modelBoundingBox")
    """
    Bounding box of the entire model
    """
    bounding_box_per_body: dict[str, Box] = Field(..., alias="boundingBoxPerBody")
    """
    Bounding box of each solid and sheet in the model, keyed by its entity id
    """
    faces_bounding_box: Box | None = Field(None, alias="facesBoundingBox")
    """
    Single box enclosing all the requested faces. Set only when faces were
    requested
    """
    bounding_box_per_face: dict[str, Any] | None = Field(
        None, alias="boundingBoxPerFace"
    )
    """
    Bounding box of each requested face, keyed by its face id. Set only when
    faces were requested
    """
