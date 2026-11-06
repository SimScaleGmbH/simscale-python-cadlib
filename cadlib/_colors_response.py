# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from pydantic import Field, RootModel

from ._color import Color


class ColorsResponse(RootModel[list[Color]]):
    """
    Response for get model colors query
    List of colors defined on solids and sheets
    """

    root: list[Color] = Field(..., title="ColorsResponse")
    """
    Response for get model colors query
    List of colors defined on solids and sheets
    """
