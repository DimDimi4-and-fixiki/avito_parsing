from __future__ import annotations

import typing as t

import requests
from frozendict import frozendict

default_headers = frozendict({
    'authority': 'm.avito.ru',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'ru-RU,ru;q=0.9', })


def get_session(headers: t.Optional[t.Mapping[str, t.Any]] = None) -> requests.Session:
    headers = headers or default_headers
    session = requests.Session()
    session.headers.update(headers)
    return session
