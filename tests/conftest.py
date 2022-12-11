from __future__ import annotations

import pytest

from avito_tools.enums import City
from avito_tools.models import SearchInfo


@pytest.fixture
def search_info_fixture() -> SearchInfo:
    return SearchInfo(phrase='tortik', page=1, region=City.MOSCOW)
