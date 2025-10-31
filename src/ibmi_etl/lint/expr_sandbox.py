"""Expression sandbox interface for Db2 for i linting."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Protocol, Sequence


@dataclass(frozen=True)
class SandboxResult:
    """Schema-only preview returned from a dry-run of an expression."""

    columns: Sequence[str]
    types: Sequence[str]


class ExpressionSandbox(Protocol):
    """Performs schema-only dry-runs of expressions in a safe environment."""

    def describe(self, expression: str, parameters: Mapping[str, object] | None = None) -> SandboxResult:
        """Return the projected schema when evaluating *expression* with *parameters*."""
