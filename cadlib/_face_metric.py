# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._schema_model import SchemaModel


class FaceMetric(SchemaModel):
    """
    Surface area metric for a single face
    """

    entity_id: str = Field(..., alias="entityId")
    """
    Id of the face
    """
    area: float
    """
    Surface area of the face
    """
