# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._material_points_query_type import MaterialPointsQueryType
from ._schema_model import SchemaModel


class MaterialPointsParameters(SchemaModel):
    """
    Parameters for material points query
    """

    query_type: MaterialPointsQueryType = Field(..., alias="queryType")
    """
    Defines whether one point is computed for the whole model or one per solid
    and sheet. The response sets the matching field and leaves the other unset
    """
