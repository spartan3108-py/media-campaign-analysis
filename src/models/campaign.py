from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Campaign(BaseModel):
    name: str = Field(title="campaign name", example="Meta Summer Sale Campaign")
    platform: str = Field(title="platform", example="Meta")
    budget: float = Field(title="campaign budget", example=1000.0)
    status: str = Field(title="campaign status", example="active")
    metadata: Dict[str, Any] = Field(title="metadata", example=750)

