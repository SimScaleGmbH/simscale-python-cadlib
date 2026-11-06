# AUTO-GENERATED Python interface - DO NOT EDIT MANUALLY

from enum import StrEnum


class AllowedFacetFaultsLevel(StrEnum):
    """
        Level of faults allowed in tessellation (Supported only for Parasolid models)
    Used in quality checks to classify the tessellation faults in three levels: mild, moderate and serious.
    The default is `Mild`, which allows only minor faults that do not significantly affect the quality of the tessellation.
    `Moderate` allows more significant faults that may affect the quality but are still acceptable for most applications.
    `Serious` allows all faults, including those that may result in a poor quality tessellation, and should be used with caution.
    """

    MILD = "mild"
    MODERATE = "moderate"
    SERIOUS = "serious"
