# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field

from ._circle_primitive import CirclePrimitive
from ._patch_type import PatchType
from ._rectangle_primitive import RectanglePrimitive
from ._schema_model import SchemaModel


class PlanarPatch(SchemaModel):
    """
    One patch of adjacent, coplanar faces, together with the primitive approximating it.

    `patch_type` names which primitive describes the patch: exactly one of `rectangle` and
    `circle` is set, the one `patch_type` names.
    """

    faces: list[str]
    """
    The faces that make up this patch
    """
    patch_type: PatchType = Field(..., alias="patchType")
    """
    The kind of primitive that approximates this patch
    """
    rectangle: RectanglePrimitive | None = None
    """
    The rectangle approximating this patch, set when `patch_type` is `rectangle`
    """
    circle: CirclePrimitive | None = None
    """
    The circle approximating this patch, set when `patch_type` is `circle`
    """
