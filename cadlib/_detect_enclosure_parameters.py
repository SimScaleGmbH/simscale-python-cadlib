# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from ._schema_model import SchemaModel
from ._vector3 import Vector3


class DetectEnclosureParameters(SchemaModel):
    """
    Parameters for detect enclosure query
    """

    point: Vector3
    """
    Point to check for enclosure
    """
