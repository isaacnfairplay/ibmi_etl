"""Structured logging helpers for the ETL toolkit."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class LogContext:
    """Correlation identifiers that should be attached to log records."""

    table_name: str
    run_id: str


class StructuredLogger(Protocol):
    """Emits structured log events scoped to table-level processing."""

    def info(self, message: str, context: LogContext) -> None:
        """Record an informational message enriched with *context*."""

    def warning(self, message: str, context: LogContext) -> None:
        """Record a warning message enriched with *context*."""

    def error(self, message: str, context: LogContext) -> None:
        """Record an error message enriched with *context*."""
