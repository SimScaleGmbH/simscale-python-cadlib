# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._schema_model import SchemaModel


class VolumeParameters(SchemaModel):
    """
    Parameters for compute volume query
    """

    entity_ids: list[str] = Field(..., alias="entityIds")
    """
    Ids of the solids and sheets to measure, as `entities` returns them.
    Must not be empty
    """
