# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field, RootModel


class DetectEnclosureResponse(RootModel[list[str]]):
    """
    Response for detect enclosure query
    List of solids enclosing the input point
    """

    root: list[str] = Field(..., title="DetectEnclosureResponse")
    """
    Response for detect enclosure query
    List of solids enclosing the input point
    """
