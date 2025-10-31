"""Credential storage abstraction aware of expiry slugs."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Protocol

_EXPIRY_SLUG_PATTERN = re.compile(
    r"(?:^|;)\s*exp=(\d{4}-\d{2}-\d{2})\s*(?:;|$)", re.IGNORECASE
)


def parse_expiry_from_service_name(service_name: str) -> date | None:
    """Extract an ``exp=YYYY-MM-DD`` slug from ``service_name`` if present.

    The expiry marker is parsed case-insensitively and must represent a valid
    calendar date. When no slug exists ``None`` is returned; invalid dates raise
    :class:`ValueError` so callers can surface actionable rotation guidance.
    """

    match = _EXPIRY_SLUG_PATTERN.search(service_name)
    if not match:
        return None

    slug = match.group(1)
    try:
        year, month, day = map(int, slug.split("-"))
        return date(year, month, day)
    except ValueError as exc:
        raise ValueError(
            f"Invalid exp= slug in service name: {service_name!r}"
        ) from exc


@dataclass(frozen=True)
class CredentialRecord:
    """Structured credentials retrieved from a secure keyring."""

    service_name: str
    secret: str
    expires_on: date | None

    @classmethod
    def from_service_name(
        cls,
        service_name: str,
        secret: str,
        *,
        default_ttl: timedelta | None = None,
        issued_on: date | None = None,
    ) -> "CredentialRecord":
        """Construct a record inferring expiry from ``service_name``.

        When ``service_name`` includes an ``exp=YYYY-MM-DD`` slug that value is
        used verbatim. Otherwise ``default_ttl`` can supply a fallback window
        which is added to ``issued_on`` (or ``date.today()`` when ``issued_on``
        is omitted).
        """

        expires_on = parse_expiry_from_service_name(service_name)
        if expires_on is None and default_ttl is not None:
            reference_date = issued_on or date.today()
            expires_on = reference_date + default_ttl
        return cls(service_name=service_name, secret=secret, expires_on=expires_on)

    def requires_rotation(self, *, on_date: date | None = None) -> bool:
        """Return ``True`` when the credential should be rotated."""

        if self.expires_on is None:
            return False
        reference_date = on_date or date.today()
        return reference_date >= self.expires_on


class KeyringAdapter(Protocol):
    """Interface for retrieving and rotating credentials used by the ODBC client."""

    def get(self, service_name: str) -> CredentialRecord | None:
        """Return credentials for *service_name* if present and not expired."""

    def set(self, record: CredentialRecord) -> None:
        """Persist *record* into the underlying secret store."""

    def delete(self, service_name: str) -> None:
        """Remove credentials for *service_name* from the secret store."""
