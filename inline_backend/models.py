from typing import List, Optional

from pydantic import BaseModel


class SearchResponseItem(BaseModel):
    name: str
    owner: str
    language: Optional[str]
    followers: Optional[int]
    url: Optional[str]
    description: Optional[str]


class SearchResponse(BaseModel):
    repositories: List[SearchResponseItem]
