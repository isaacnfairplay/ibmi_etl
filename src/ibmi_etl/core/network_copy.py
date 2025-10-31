"""Network copy orchestration for safely publishing Parquet outputs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass(frozen=True)
class NetworkCopyPlan:
    """Configuration describing where and how a dataset should be published."""

    source_path: Path
    destination_path: Path
    atomic_replace: bool


class NetworkCopyExecutor(Protocol):
    """Executes network copy plans with integrity and safety checks."""

    def run(self, plan: NetworkCopyPlan) -> None:
        """Perform the copy described by *plan* using temp files and atomic replace semantics."""
