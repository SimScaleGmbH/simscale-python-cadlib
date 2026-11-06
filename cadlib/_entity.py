# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY


from pydantic import Field

from ._entity_type import EntityType
from ._schema_model import SchemaModel


class Entity(SchemaModel):
    """
    An entity in the CAD model topology (solids, sheets, faces, edges, vertices).
    """

    entity_id: str = Field(..., alias="entityId")
    """
    Unique entity id, e.g. `A1_I2_B3_TE4` or `B1_TE2`
    """
    name: str
    """
    Human-readable entity name, e.g. `face_name@body_name`
    """
    type: EntityType
    """
    Type of the entity
    """
    children: list[int]
    """
    Indices of the children of this entity in this list
    """
    parents: list[int]
    """
    Indices in this list of all entities this entity is a child of.
    Empty for top-level entities, i.e. solids and sheets.
    An entity can have several parents: an edge is usually shared by two faces,
    a vertex by several edges.
    """
