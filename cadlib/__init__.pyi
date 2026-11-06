# AUTO-GENERATED type stubs - DO NOT EDIT MANUALLY
"""
Type stubs for CAD library Python bindings.

This .pyi file provides complete type information for type checkers and IDEs.
The Cad class is the main entry point for all CAD queries.
"""

from pathlib import Path
from typing import Any

# Import types from generated models
from ._bounding_box_parameters import BoundingBoxParameters
from ._bounding_box_response import BoundingBoxResponse
from ._center_of_gravity_parameters import CenterOfGravityParameters
from ._center_of_gravity_response import CenterOfGravityResponse
from ._colors_parameters import ColorsParameters
from ._colors_response import ColorsResponse
from ._detect_common_rotation_parameters import DetectCommonRotationParameters
from ._detect_common_rotation_response import DetectCommonRotationResponse
from ._detect_enclosure_parameters import DetectEnclosureParameters
from ._detect_enclosure_response import DetectEnclosureResponse
from ._entities_response import EntitiesResponse
from ._generate_comfort_map_disc_parameters import GenerateComfortMapDiscParameters
from ._generate_comfort_map_disc_response import GenerateComfortMapDiscResponse
from ._material_points_parameters import MaterialPointsParameters
from ._material_points_response import MaterialPointsResponse
from ._model_metrics_parameters import ModelMetricsParameters
from ._model_metrics_response import ModelMetricsResponse
from ._planar_patch_primitives_parameters import PlanarPatchPrimitivesParameters
from ._planar_patch_primitives_response import PlanarPatchPrimitivesResponse
from ._tessellate_faces_parameters import TessellateFacesParameters
from ._tessellate_faces_response import TessellateFacesResponse
from ._tessellate_parameters import TessellateParameters
from ._tessellate_response import TessellateResponse
from ._volume_parameters import VolumeParameters
from ._volume_response import VolumeResponse

class CadExpectedError(Exception):
    """Raised when a known, anticipated CAD error occurs.

    Attributes:
        error_code: Machine-readable error identifier (e.g. ``"detect-rotation-flat-faces-selected-with-entity"``).
        error_details: Structured details dict, or ``None`` if absent.

    Example::

        try:
            await cad.detect_common_rotation(params)
        except CadExpectedError as e:
            print(e.error_code)     # str
            print(e.error_details)  # dict | None
    """

    error_code: str
    error_details: dict | None

    def __init__(self, error_code: str, error_details: dict | None = None) -> None: ...

class CadUnexpectedError(Exception):
    """Raised when an unexpected internal error occurs in the CAD library."""

class Cad:
    """
    Main entry point for CAD queries.

    Example:
        cad = Cad.load(request.data_map.cad)
        result = await cad.tessellate(Path("/path/to/output/folder"), params)
        entities = await cad.entities()
    """

    @staticmethod
    def load(entry: Any) -> Cad:
        """Load a CAD model from the CAD data map entry of a workflow method's run request.

        Accepts the method's generated ``FileSystemDataMapEntry``, any other Pydantic model or
        dict serializing to the same shape, or already-serialized JSON text.
        """
        ...

    # Query Methods
    async def bounding_box(
        self, parameters: BoundingBoxParameters | None = None
    ) -> BoundingBoxResponse:
        """Computes the bounding box of the model, of each body, and of any faces given.

        The box of the whole model and one box per solid and sheet are always
        returned. Naming faces additionally returns one box per face, keyed by
        face id, and a single box enclosing all of them.

        Supported for Parasolid and nTop models. Other formats fail with
        ``query-type-unsupported-for-cad-format``.

        Raises:
            CadExpectedError: if the query fails (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md).
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def center_of_gravity(
        self, parameters: CenterOfGravityParameters | None = None
    ) -> CenterOfGravityResponse:
        """Computes the center of gravity of the given faces and edges.

        The selection accepts faces and edges only; any other entity type fails
        the query. One center of gravity is computed for the selection as a
        whole, not one per selected entity.

        Supported only for Parasolid models. Other formats fail with
        ``query-type-unsupported-for-cad-format``.

        Raises:
            CadExpectedError: with one of these error codes (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md):
                * ``compute-cog-entity-not-supported`` - A selected entity has unsupported type, it is neither a face nor an edge.
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def colors(
        self, parameters: ColorsParameters | None = None
    ) -> ColorsResponse:
        """Returns the colors defined on the model's solids and sheets.

        The query takes no parameters and covers the whole model. Each entry names
        the entity the color is defined on and the color itself, as a hex string
        such as ``#ff0000``.

        Supported for Parasolid and nTop models. Other formats fail with
        ``query-type-unsupported-for-cad-format``.

        Raises:
            CadExpectedError: if the query fails (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md).
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def detect_common_rotation(
        self, parameters: DetectCommonRotationParameters | None = None
    ) -> DetectCommonRotationResponse:
        """Detects the rotation axis and center shared by the given faces.

        All the given faces must be rotationally aligned about a single axis; the
        query fails if they are not, or if no axis can be determined. The response
        gives the direction of that axis and a point on it.

        Supported only for Parasolid models. Other formats fail with
        ``query-type-unsupported-for-cad-format``.

        Raises:
            CadExpectedError: with one of these error codes (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md):
                * ``detect-rotation-axis-not-consistent-for-all-faces`` - The selected faces do not share the same rotation axis.
                * ``detect-rotation-could-not-detect-axis`` - No rotation axis could be detected for the selected faces.
                * ``detect-rotation-flat-faces-selected[-with-entity]`` - The selection contains flat faces, which have no rotation axis.
                * ``detect-rotation-multiple-possible-directions`` - More than one rotation direction fits the selected faces.
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def detect_enclosure(
        self, parameters: DetectEnclosureParameters | None = None
    ) -> DetectEnclosureResponse:
        """Finds the solids that enclose a given point.

        The response holds the id of every solid that contains it.

        Supported only for Parasolid models. Other model formats fail with
        ``query-type-unsupported-for-cad-format``.

        Raises:
            CadExpectedError: if the query fails (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md).
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def entities(self) -> EntitiesResponse:
        """Returns the model's entities: solids, sheets, faces, edges and vertices.

        The list is flat: each entity references its parents and children by their
        0-based index in it. Solids and sheets are the top-level entities.

        Each entity carries the entity id that the other queries take as input.

        Supported for Parasolid, STL and nTop models.

        Raises:
            CadExpectedError: if the query fails (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md).
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def generate_comfort_map_disc(
        self, path: Path, parameters: GenerateComfortMapDiscParameters | None = None
    ) -> GenerateComfortMapDiscResponse:
        """Generates the comfort-map disc and writes the STL result into a directory.

        The disc is a tessellated surface covering a region of interest: a circle of
        radius ``floor_radius`` around ``center``, placed ``height`` above the ground.
        ``fineness`` controls how finely it is tessellated.

        By default the disc is written as a single file. Asking for one of the zipped
        encodings in ``result_encoding`` unpacks the result into the directory instead.
        The directory is created if it does not exist, and files in it with
        the same names are overwritten.

        A disc with no geometry is reported as ``empty-comfort-map-disc``.

        Supported for Parasolid and STL models. Other formats fail with
        ``query-type-unsupported-for-cad-format``.

        Raises:
            CadExpectedError: with one of these error codes (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md):
                * ``empty-comfort-map-disc`` - The query returned no geometry.
                * ``lawson-cylinder-exceeds-size-box`` - ``floor_radius`` is too large for the model's size box.
                * ``lawson-negative-height-above-ground`` - ``height`` is negative.
                * ``lawson-roi-radius-must-be-positive`` - ``floor_radius`` is zero or negative.
                * ``lawson-tessellation-max-width-must-be-positive`` - ``fineness`` is zero or negative.
                * ``lawson-tessellation-too-fine`` - ``fineness`` produces more than 100 million triangles, which the query does not allow.
                * ``tessellation-has-error[-with-entity]`` - The kernel could not tessellate one or more entities.
                * ``tessellation-too-large`` - The result could not be written; the kernel ran out of disk space.
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def material_points(
        self, parameters: MaterialPointsParameters | None = None
    ) -> MaterialPointsResponse:
        """Computes a point inside the material, for the whole model or for each solid.

        ``query_type`` chooses between the two. The response sets the field that
        matches it and leaves the other unset; the per-body field is keyed by
        entity id.

        A material point is only guaranteed to lie inside the material. Which
        interior point is returned is unspecified, and can differ between runs.

        Supported only for Parasolid models. Other formats fail with
        ``query-type-unsupported-for-cad-format``.

        Raises:
            CadExpectedError: if the query fails (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md).
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def model_metrics(
        self, parameters: ModelMetricsParameters | None = None
    ) -> ModelMetricsResponse:
        """Computes volume and surface-area metrics for the model and its entities.

        Computes aggregated volume and surface area for the model, along with
        per-solid, per-sheet, per-face and per-edge metrics.

        The query takes no parameters: the metrics always cover the whole model.

        Supported for Parasolid and nTop models. Other formats fail with
        ``query-type-unsupported-for-cad-format``.

        Raises:
            CadExpectedError: if the query fails (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md).
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def planar_patch_primitives(
        self, parameters: PlanarPatchPrimitivesParameters | None = None
    ) -> PlanarPatchPrimitivesResponse:
        """Approximates groups of coplanar faces with a circle or rectangle primitive.

        Groups the requested faces into patches of adjacent, coplanar faces and
        approximates each patch with the primitive — a circle or a rectangle — whose
        area is closest to the area of the patch. All faces of a patch belong to the
        same occurrence. The query fails if any of the requested faces is not planar.

        Supported only for Parasolid models. Other formats fail with
        ``query-type-unsupported-for-cad-format``.

        Raises:
            CadExpectedError: with one of these error codes (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md):
                * ``planar-patch-primitives-degenerate-patch[-with-entity]`` - A face has no interior point, or a patch is not two-dimensional, so no primitive fits it.
                * ``planar-patch-primitives-non-coplanar-faces[-with-entity]`` - Faces that are adjacent, and so belong to the same patch, lie on different planes.
                * ``planar-patch-primitives-non-planar-faces[-with-entity]`` - One or more of the requested faces is not planar.
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def tessellate(
        self, path: Path, parameters: TessellateParameters | None = None
    ) -> TessellateResponse:
        """Tessellates the model and writes the STL files into a directory.

        One STL file is written per region by default, or one per face when
        ``write_one_file_per_face`` is set. The directory is created if it does not
        exist, and files in it with the same names are overwritten.

        ``tessellation_type``, ``max_facet_width`` and ``allowed_facet_faults_level``
        apply to Parasolid models, and ``tessellation_type`` has to be set explicitly;
        ``feature_size``, ``adaptivity`` and ``max_edge_length`` apply to nTop models
        and all default when omitted. ``tess_surface_area`` is set in the response
        only when ``calculate_area`` is requested.

        Supported for Parasolid, STL and nTop models.

        Raises:
            CadExpectedError: with one of these error codes (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md):
                * ``tessellation-has-error[-with-entity]`` - The kernel could not tessellate one or more entities.
                * ``tessellation-ntop-negative-adaptivity`` - ``adaptivity`` is negative.
                * ``tessellation-ntop-zero-edge-length`` - ``max_edge_length`` is zero.
                * ``tessellation-ntop-zero-feature-size`` - ``feature_size`` is zero.
                * ``tessellation-too-large`` - The result could not be written; the kernel ran out of disk space.
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def tessellate_faces(
        self, path: Path, parameters: TessellateFacesParameters | None = None
    ) -> TessellateFacesResponse:
        """Tessellates the requested faces, writing one STL file per face into a directory.

        Each requested face is tessellated into its own STL file, named after the
        face id; a face requested more than once is tessellated only once. The
        response additionally carries the normal of each face, evaluated at the
        mid point of the face.

        The faces to tessellate are required, so a query without parameters is
        rejected. The directory is created if it does not exist, and files in it with
        the same names are overwritten.

        Supported only for Parasolid models. Other formats fail with
        ``query-type-unsupported-for-cad-format``.

        Raises:
            CadExpectedError: with one of these error codes (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md):
                * ``tessellation-has-error`` - The kernel could not tessellate one of the faces.
            CadUnexpectedError: if the library fails internally.
        """
        ...

    async def volume(
        self, parameters: VolumeParameters | None = None
    ) -> VolumeResponse:
        """Computes the volume of each selected solid, and their total.

        The solids and sheets to measure are given by their entity ids, as
        ``entities`` returns them.

        ``volumes`` holds one entry per measured entity, keyed by its entity id,
        and ``total`` is their sum.

        Supported for Parasolid and nTop models. Other formats fail with
        ``query-type-unsupported-for-cad-format``.

        Raises:
            CadExpectedError: if the query fails (see https://github.com/SimScaleGmbH/simscale-python-cadlib/blob/main/ERRORS.md).
            CadUnexpectedError: if the library fails internally.
        """
        ...

__all__: list[str]
