# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from ._schema_model import SchemaModel


class CenterOfGravityParameters(SchemaModel):
    """
    Parameters for compute center of gravity query
    """

    entities: list[str]
    """
    Ids of the faces and edges to combine into a single center of gravity, as
    `entities` returns them. Any other entity type fails the query.
    Must not be empty
    """
