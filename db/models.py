from dataclasses import dataclass


@dataclass
class Token:
    id: int
    uuid: str


@dataclass
class User:
    id: int
    name: str
    token: Token
