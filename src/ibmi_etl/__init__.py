"""Public package for the i-Series Data Warehouse toolkit."""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("ibmi-etl")
except PackageNotFoundError:  # pragma: no cover - package metadata absent in editable installs.
    __version__ = "0.0.0"

__all__ = ["__version__"]
