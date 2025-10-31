"""ODBC connectivity abstraction for IBM i (Db2 for i) data sources."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Protocol, Sequence


@dataclass(frozen=True)
class QueryResult:
    """Container for tabular results returned by the ODBC client."""

    columns: Sequence[str]
    rows: Iterable[Sequence[object]]


class ODBCClient(Protocol):
    """Interface responsible for executing SQL against Db2 for i via ODBC."""

    def fetch_rows(self, sql: str, parameters: Mapping[str, object] | None = None) -> QueryResult:
        """Execute *sql* and return an iterable row set."""

    def close(self) -> None:
        """Release any open handles and sockets associated with the client."""
