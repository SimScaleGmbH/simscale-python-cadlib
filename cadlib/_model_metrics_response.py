# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._edge_metric import EdgeMetric
from ._face_metric import FaceMetric
from ._schema_model import SchemaModel
from ._volume_metric import VolumeMetric


class ModelMetricsResponse(SchemaModel):
    """
    Response for model metrics query
    """

    model_volume: float = Field(..., alias="modelVolume")
    """
    Sum of the volumes in `solids`
    """
    model_surface_area: float = Field(..., alias="modelSurfaceArea")
    """
    Aggregated surface area of all solids and sheets
    """
    solids: list[VolumeMetric]
    """
    Volume and surface area metrics per solid
    """
    sheets: list[VolumeMetric]
    """
    Volume and surface area metrics per sheet
    """
    faces: list[FaceMetric]
    """
    Surface area metrics per face
    """
    edges: list[EdgeMetric]
    """
    Length metrics per edge
    """
