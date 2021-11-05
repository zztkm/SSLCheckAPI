from typing import List, Optional

from pydantic import BaseModel


class ValidResult(BaseModel):
    host: str
    valid: bool
    version: Optional[str] = None
    error: Optional[str] = None


class HostNames(BaseModel):
    hostnames: List[str]
