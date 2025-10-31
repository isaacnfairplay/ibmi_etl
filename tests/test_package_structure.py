"""Smoke tests ensuring the package skeleton exposes expected interfaces."""

from importlib import import_module

import pytest


@pytest.mark.parametrize(
    "module_name",
    [
        "ibmi_etl.core",
        "ibmi_etl.core.odbc_client",
        "ibmi_etl.core.keyring_adapter",
        "ibmi_etl.core.query_gen",
        "ibmi_etl.core.censor_cast",
        "ibmi_etl.core.partition_merge",
        "ibmi_etl.core.network_copy",
        "ibmi_etl.core.log",
        "ibmi_etl.lint",
        "ibmi_etl.lint.parser",
        "ibmi_etl.lint.expr_sandbox",
    ],
)
def test_module_imports(module_name: str) -> None:
    """Each top-level module should be importable without side effects."""

    module = import_module(module_name)
    assert module.__doc__, f"{module_name} should define a module docstring"
