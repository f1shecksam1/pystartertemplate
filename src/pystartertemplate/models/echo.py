from pydantic import BaseModel


class EchoIn(BaseModel):
    text: str


class EchoOut(BaseModel):
    echoed: str
