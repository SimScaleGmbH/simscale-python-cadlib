# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from typing import Any

from pydantic import Field

from ._schema_model import SchemaModel
from ._vector3 import Vector3


class MaterialPointsResponse(SchemaModel):
    """
    Response for material points query
    """

    model_material_point: Vector3 | None = Field(None, alias="modelMaterialPoint")
    """
    A point inside the model's material. Set when `queryType` is `entireModel`
    """
    material_point_per_body: dict[str, Any] | None = Field(
        None, alias="materialPointPerBody"
    )
    """
    A point inside each solid and sheet, keyed by its entity id. Set when
    `queryType` is `perBody`
    """
