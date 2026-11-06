# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._schema_model import SchemaModel


class TessellateResponse(SchemaModel):
    """
    Response for tessellation query
    """

    num_bodies: int = Field(..., alias="numBodies")
    """
    Number of bodies in the tessellated geometry
    """
    tess_surface_area: float | None = Field(None, alias="tessSurfaceArea")
    """
    Surface area of the tessellated geometry. Set only when `calculate_area`
    was requested
    """
