# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._schema_model import SchemaModel


class EdgeMetric(SchemaModel):
    """
    Length metric for a single edge
    """

    entity_id: str = Field(..., alias="entityId")
    """
    Id of the edge
    """
    length: float
    """
    Length of the edge
    """
