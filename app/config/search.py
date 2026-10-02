from pydantic import BaseModel, Field


class SearchConfig(BaseModel):
    keywords: list[str] = Field(default_factory=list)
    locations: list[str] = Field(default_factory=list)
    results_per_page: int = 20