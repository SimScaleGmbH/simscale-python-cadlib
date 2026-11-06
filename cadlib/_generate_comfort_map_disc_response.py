# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY


from ._box import Box
from ._schema_model import SchemaModel


class GenerateComfortMapDiscResponse(SchemaModel):
    """
    Response for comfort maps query
    """

    number_of_triangles: int
    """
    Number of triangles in the tessellated disc. Always greater than zero: a
    disc with no geometry fails the query instead
    """
    bounding_box: Box | None = None
    """
    Bounding box of the tessellated disc (optional)
    """
