import jwt
from pydantic import BaseModel, Field
from typing import Optional


class BearerToken(BaseModel):
    email: Optional[str]
    user_id: Optional[str] = Field(alias="sub")
    name: Optional[str]
    aud: Optional[str]
    picture : Optional[str]
async def decode_token(token: str):
    token = jwt.decode(token, options={"verify_signature": False})
    token = BearerToken(**token)
    return token
