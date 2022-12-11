from __future__ import annotations

from pydantic import BaseModel
from pydantic import Field

from avito_tools.enums import City


class SearchInfo(BaseModel):
    q: str = Field(alias='phrase')
    p: int = Field(alias='page')
    region: City = Field(exclude=True)
