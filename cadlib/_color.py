# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from ._schema_model import SchemaModel


class Color(SchemaModel):
    """
    Color information for an entity
    """

    entity_id: str
    """
    Id of the solid or sheet the color is defined on
    """
    color: str
    """
    Color in hex format (e.g., "#ff0000")
    """
