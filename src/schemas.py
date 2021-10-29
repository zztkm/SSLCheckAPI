from pydantic import BaseModel


class ValidResult(BaseModel):
    host: str
    valid: bool
