"""Linting primitives for Db2 for i SQL expressions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Protocol


@dataclass(frozen=True)
class SQLRule:
    """Represents a single lint rule enforced during validation."""

    identifier: str
    description: str


@dataclass(frozen=True)
class SQLRuleViolation:
    """Data structure describing a lint failure."""

    rule: SQLRule
    message: str
    line: int | None = None
    column: int | None = None


class SQLValidator(Protocol):
    """Validates SQL snippets against Db2 for i specific expectations."""

    def validate(self, sql: str) -> Iterable[SQLRuleViolation]:
        """Return an iterable of violations discovered in *sql*."""
