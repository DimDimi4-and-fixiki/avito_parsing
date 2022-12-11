from __future__ import annotations

import urllib.parse

import config
from avito_tools.models import SearchInfo


def get_page_url(params: SearchInfo) -> str:
    endpoint = config.AVITO_URL.replace('city', params.region.value)
    url = endpoint + urllib.parse.urlencode(params.dict())
    return url
