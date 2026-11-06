# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._schema_model import SchemaModel


class VolumeMetric(SchemaModel):
    """
    Volume and surface area metrics for a single solid or sheet
    """

    entity_id: str = Field(..., alias="entityId")
    """
    Id of the solid or sheet
    """
    volume: float
    """
    Volume of the entity, when applicable
    """
    surface_area: float = Field(..., alias="surfaceArea")
    """
    Surface area of the entity
    """
