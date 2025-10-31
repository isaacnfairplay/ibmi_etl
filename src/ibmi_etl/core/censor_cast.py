"""Censoring and casting planner interfaces."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Protocol


@dataclass(frozen=True)
class CastExpression:
    """Mapping describing how to project a transformed column."""

    alias: str
    expression: str


@dataclass(frozen=True)
class CensorCastPlan:
    """Specification of the censoring and casting pipeline."""

    censored_columns: Iterable[str]
    cast_expressions: Iterable[CastExpression]
    validation_rules: Mapping[str, str]


class CensorCastPlanner(Protocol):
    """Defines how staged tables should be censored, cast, and validated."""

    def plan(self, table_name: str) -> CensorCastPlan:
        """Return the plan for *table_name* covering censorship, casts, and validation."""
