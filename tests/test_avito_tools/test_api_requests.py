from __future__ import annotations

from avito_tools.api_requests import get_page_url

EXPECTED_URL = 'https://www.avito.ru/moskva/predlozheniya_uslug/obuchenie_kursy-ASgBAgICAUSYC7afAQ?q=tortik&p=1'


def test_get_page_url(search_info_fixture):
    url = get_page_url(params=search_info_fixture)
    assert url == EXPECTED_URL
