"""Credential storage abstraction aware of expiry slugs."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Protocol


@dataclass(frozen=True)
class CredentialRecord:
    """Structured credentials retrieved from a secure keyring."""

    service_name: str
    secret: str
    expires_on: date | None


class KeyringAdapter(Protocol):
    """Interface for retrieving and rotating credentials used by the ODBC client."""

    def get(self, service_name: str) -> CredentialRecord | None:
        """Return credentials for *service_name* if present and not expired."""

    def set(self, record: CredentialRecord) -> None:
        """Persist *record* into the underlying secret store."""

    def delete(self, service_name: str) -> None:
        """Remove credentials for *service_name* from the secret store."""
