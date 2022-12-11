from __future__ import annotations
EXPECTED_RESULT = '{"q": "tortik", "p": 1}'


def test_search_info_serialization(search_info_fixture):
    info = search_info_fixture
    json_str = info.json()
    assert json_str == EXPECTED_RESULT
