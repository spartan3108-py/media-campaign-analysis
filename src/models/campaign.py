from pydantic import BaseModel, Field
from typing import Optional


class Campaign(BaseModel):
    name: str = Field(title="campaign name", example="Meta Summer Sale Campaign")
    platform: str = Field(title="platform", example="Meta")
    budget: float = Field(title="campaign budget", example=1000.0)
    status: str = Field(title="campaign status", example="active")
    impressions: Optional[int] = Field(title="clicks", example=750)
    clicks: Optional[int] = Field(title="clicks", example=75)

