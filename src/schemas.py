from typing import List, Optional

from pydantic import BaseModel


class ValidResult(BaseModel):
    host: str
    valid: bool
    version: Optional[str] = None
    error: Optional[str] = None


class HostName(BaseModel):
    hostname: str


class HostNames(BaseModel):
    hostnames: List[str]


class CheckRedirectResponse(BaseModel):
    host: str
    request_url: str
    redirect_url: Optional[str] = None
