# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY


from pydantic import Field, RootModel

from ._entity import Entity


class EntitiesResponse(RootModel[list[Entity]]):
    """
    Response for entities query — a flat list of all entities.

    Each entity references its parents and children by their 0-based index in the list.
    Solids and sheets are the top-level entities.
    """

    root: list[Entity] = Field(..., title="EntitiesResponse")
    """
    Response for entities query — a flat list of all entities.

    Each entity references its parents and children by their 0-based index in the list.
    Solids and sheets are the top-level entities.
    """
