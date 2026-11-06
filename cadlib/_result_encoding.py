# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from enum import StrEnum


class ResultEncoding(StrEnum):
    """
    Encoding format for STL result data, used in some queries to control how the result is encoded (e.g. for comfort map disc)
    """

    ASCII = "ascii"
    BINARY = "binary"
    ZIPPED_ASCII = "zipped-ascii"
    ZIPPED_BINARY = "zipped-binary"
