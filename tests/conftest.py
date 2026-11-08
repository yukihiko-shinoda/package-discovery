"""Configuration of pytest."""

from __future__ import annotations

__author__ = "Yukihiko Shinoda"
__copyright__ = "Copyright (c) 2025 Yukihiko Shinoda"
__license__ = "MIT"

from typing import Any

import pytest

collect_ignore = ["setup.py"]


@pytest.fixture
def response() -> dict[Any, Any] | None:
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests  # noqa: ERA001
    # return requests.get("https://github.com/audreyr/cookiecutter-pypackage")  # noqa: ERA001
    return None
