# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._allowed_facet_faults_level import AllowedFacetFaultsLevel
from ._schema_model import SchemaModel
from ._tessellation_type import TessellationType


class TessellateFacesParameters(SchemaModel):
    """
    Parameters for the tessellate faces query.

    Tessellates a chosen set of faces: each face becomes its own STL file, named
    after the face id. A face listed more than once is tessellated only once.

    Supported only for Parasolid models.
    """

    faces: list[str]
    """
    Ids of the faces to tessellate, as `entities` returns them. Each face is
    tessellated into its own STL file, named after the face id. A face
    requested more than once is tessellated only once. Must not be empty
    """
    tessellation_type: TessellationType | None = Field(None, alias="tessellationType")
    """
    Defines the tessellation strategy. Defaults to `chordTol` when omitted
    """
    max_facet_width: float | None = Field(None, alias="maxFacetWidth")
    """
    Maximum facet width for tessellationType=maxFacetWidth. If omitted, it is
    derived from the size of the face
    """
    allowed_facet_faults_level: AllowedFacetFaultsLevel | None = Field(
        None, alias="allowedFacetFaultsLevel"
    )
    """
    Level of faults allowed in the tessellation. Used in quality checks.
    Defaults to `mild` when omitted
    """
