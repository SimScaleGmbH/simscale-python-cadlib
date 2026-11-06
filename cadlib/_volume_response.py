# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from ._schema_model import SchemaModel


class VolumeResponse(SchemaModel):
    """
    Response for volume query
    """

    total: float
    """
    Sum of the volumes in `volumes`
    """
    volumes: dict[str, float]
    """
    Volume of each measured entity, keyed by its entity id
    """
