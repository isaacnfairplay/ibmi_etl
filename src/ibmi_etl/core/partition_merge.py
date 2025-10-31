"""Partition merge planning for deterministic Parquet consolidation."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass(frozen=True)
class PartitionMergePlan:
    """Describes how staged data should be merged into persistent partitions."""

    table_name: str
    staging_path: Path
    destination_path: Path
    reprocess_tail: bool


class PartitionMergePlanner(Protocol):
    """Creates merge plans combining staged data with existing Parquet partitions."""

    def plan(self, table_name: str) -> PartitionMergePlan:
        """Return a deterministic merge plan for *table_name*."""
