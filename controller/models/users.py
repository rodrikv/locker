from pydantic import BaseModel


class Token(BaseModel):
    id: int
    uuid: str


class User(BaseModel):
    id: int
    name: str
    token: Token
