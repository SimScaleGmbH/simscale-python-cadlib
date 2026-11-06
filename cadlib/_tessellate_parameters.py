# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._allowed_facet_faults_level import AllowedFacetFaultsLevel
from ._schema_model import SchemaModel
from ._tessellation_type import TessellationType


class TessellateParameters(SchemaModel):
    """
    Parameters for tessellate query
    """

    write_one_file_per_face: bool = Field(..., alias="writeOneFilePerFace")
    """
    If true, one STL file is written per face; if false, one per region
    """
    calculate_area: bool = Field(..., alias="calculateArea")
    """
    If true, computes the surface area of the tessellation and returns it as
    `tess_surface_area` in the response
    """
    tessellation_type: TessellationType | None = Field(None, alias="tessellationType")
    """
    Supported only for Parasolid models. Defines the tessellation strategy.
    Has no default: the query fails with `invalid-parameter` if it is not set
    """
    max_facet_width: float | None = Field(None, alias="maxFacetWidth")
    """
    Supported only for Parasolid models. Maximum facet width, used when `tessellation_type`
    is `maxFacetWidth`. If omitted, it is computed from the bounding box of the body
    """
    allowed_facet_faults_level: AllowedFacetFaultsLevel | None = Field(
        None, alias="allowedFacetFaultsLevel"
    )
    """
    Supported only for Parasolid models. Level of faults allowed in the tessellation.
    Used in quality checks. Defaults to `mild` when omitted
    """
    feature_size: float | None = Field(None, alias="featureSize")
    """
    Supported only for nTop models. Granularity at which the solid's field is sampled.
    Make this smaller to get more triangles and lower max edge length.
    Must be greater than zero. Defaults to 0.0015 when omitted
    """
    adaptivity: float | None = None
    """
    Supported only for nTop models. Controls how much the mesh is decimated.
    Make this higher to get less triangles and higher max edge length.
    Must be greater than zero. Defaults to 10 when omitted
    """
    max_edge_length: float | None = Field(None, alias="maxEdgeLength")
    """
    Supported only for nTop models. Specifies the maximum allowable length for any edge in the tessellated
    mesh. During refinement, edges longer than this value are subdivided to ensure the
    mesh respects this limit. Must be greater than zero. Defaults to 10 when omitted
    """
