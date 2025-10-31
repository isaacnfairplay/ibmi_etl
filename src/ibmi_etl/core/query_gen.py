"""Query planning interfaces for incremental Db2 for i loads."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Protocol


@dataclass(frozen=True)
class QueryPlan:
    """Represents a SQL statement plus metadata required to execute it."""

    sql: str
    parameters: Mapping[str, object]
    identity_column: str


class QueryPlanner(Protocol):
    """Produces ordered query plans for incremental and revision-aware loads."""

    def initial_load(self) -> QueryPlan:
        """Plan the very first extract when no state is persisted."""

    def incremental_load(self, last_identity: object) -> QueryPlan:
        """Plan the next incremental extract given the last processed identity value."""

    def reprocess_partition(self, identity_floor: object) -> QueryPlan:
        """Plan a targeted reprocess of the trailing partition to capture revisions."""
