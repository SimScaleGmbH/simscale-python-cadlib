# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from ._schema_model import SchemaModel


class PlanarPatchPrimitivesParameters(SchemaModel):
    """
    Parameters for planar patch primitives query
    """

    faces: list[str]
    """
    Ids of the planar faces to group into patches, as `entities` returns them. The query fails if any of the given faces is not planar. Must not be empty
    """
