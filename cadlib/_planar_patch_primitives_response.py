# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY


from ._planar_patch import PlanarPatch
from ._schema_model import SchemaModel


class PlanarPatchPrimitivesResponse(SchemaModel):
    """
    Response for planar patch primitives query
    """

    patches: list[PlanarPatch]
    """
    The patches found among the requested faces
    """
