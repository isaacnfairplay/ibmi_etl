"""Tests for keyring adapter expiry helpers."""

from __future__ import annotations

from datetime import date, timedelta

import pytest

from ibmi_etl.core.keyring_adapter import (
    CredentialRecord,
    InMemoryKeyringAdapter,
    parse_expiry_from_service_name,
)


def test_parse_expiry_from_service_name_returns_date() -> None:
    service_name = "system21:dsn=System21;user=etl;exp=2025-11-30"
    assert parse_expiry_from_service_name(service_name) == date(2025, 11, 30)


def test_parse_expiry_is_case_insensitive_and_ignores_whitespace() -> None:
    service_name = "system21;EXP=2024-01-15 ;user=etl"
    assert parse_expiry_from_service_name(service_name) == date(2024, 1, 15)


def test_parse_expiry_raises_for_invalid_dates() -> None:
    with pytest.raises(ValueError):
        parse_expiry_from_service_name("system21;exp=2025-13-01")


def test_credential_record_requires_rotation_on_or_after_expiry() -> None:
    record = CredentialRecord(
        service_name="system21;exp=2025-10-31",
        secret="secret",
        expires_on=date(2025, 10, 31),
    )
    assert record.requires_rotation(on_date=date(2025, 10, 31)) is True
    assert record.requires_rotation(on_date=date(2025, 10, 30)) is False


def test_credential_record_from_service_name_parses_slug() -> None:
    record = CredentialRecord.from_service_name(
        "system21;exp=2025-12-01",
        "secret",
    )
    assert record.expires_on == date(2025, 12, 1)


def test_credential_record_from_service_name_uses_default_ttl_when_missing_slug() -> None:
    record = CredentialRecord.from_service_name(
        "system21",
        "secret",
        default_ttl=timedelta(days=10),
        issued_on=date(2025, 10, 1),
    )
    assert record.expires_on == date(2025, 10, 11)


def test_in_memory_keyring_adapter_returns_active_credentials() -> None:
    adapter = InMemoryKeyringAdapter(today=lambda: date(2025, 10, 1))
    record = CredentialRecord(
        service_name="system21;exp=2025-10-05",
        secret="secret",
        expires_on=date(2025, 10, 5),
    )
    adapter.set(record)

    retrieved = adapter.get("system21;exp=2025-10-05")
    assert retrieved is record


def test_in_memory_keyring_adapter_evicts_expired_credentials() -> None:
    clock = iter([date(2025, 10, 6), date(2025, 10, 6)])
    adapter = InMemoryKeyringAdapter(today=lambda: next(clock))
    adapter.set(
        CredentialRecord(
            service_name="system21;exp=2025-10-05",
            secret="secret",
            expires_on=date(2025, 10, 5),
        )
    )

    assert adapter.get("system21;exp=2025-10-05") is None
    assert adapter.get("system21;exp=2025-10-05") is None
