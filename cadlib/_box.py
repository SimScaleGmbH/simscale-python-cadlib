# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._schema_model import SchemaModel


class Box(SchemaModel):
    """
    3D bounding box representation
    """

    min_x: float = Field(..., alias="minX")
    """
    Minimum X coordinate
    """
    min_y: float = Field(..., alias="minY")
    """
    Minimum Y coordinate
    """
    min_z: float = Field(..., alias="minZ")
    """
    Minimum Z coordinate
    """
    max_x: float = Field(..., alias="maxX")
    """
    Maximum X coordinate
    """
    max_y: float = Field(..., alias="maxY")
    """
    Maximum Y coordinate
    """
    max_z: float = Field(..., alias="maxZ")
    """
    Maximum Z coordinate
    """
