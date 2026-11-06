# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY


from ._result_encoding import ResultEncoding
from ._schema_model import SchemaModel
from ._vector2 import Vector2


class GenerateComfortMapDiscParameters(SchemaModel):
    """
    Parameters for comfort maps query
    """

    center: Vector2
    """
    Center point of the region of interest on the ground plane. The disc will be generated in a circular region around this center point.
    """
    height: float
    """
    Height above ground of the region of interest (distance between the center point and the plane where the disc will be generated). Must not be negative
    """
    floor_radius: float
    """
    Radius of the region of interest on the ground plane (disc will be generated in a circular region with this radius around the center point). Must be greater than zero
    """
    fineness: float
    """
    Tessellation fineness parameter to control the size of the disc's tessellation,. Must be greater than zero, and large enough that the disc stays under the limit of 100 million triangles
    """
    faces: list[str] | None = None
    """
    Ids of the faces that make up the ground (optional)
    """
    ground_level: float | None = None
    """
    Height of the ground plane. Defaults to 0 when omitted
    """
    result_encoding: ResultEncoding | None = None
    """
    Defines the encoding of the file which contains the disc (optional). With `ascii` or `binary`, or when omitted, the disc is written as a single file; with `zipped-ascii` or `zipped-binary` the result is unpacked into the directory
    """
