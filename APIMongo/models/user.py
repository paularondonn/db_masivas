from pydantic import BaseModel
from typing import Any


class CreateUser(BaseModel):
    name: str
    lastname: str
    email: str


class Response(BaseModel):
    data: Any
    flag: bool
    message: str
