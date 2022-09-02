from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str]
    uid: Optional[str]
    fullname: Optional[str]
    email: Optional[str]
    password: Optional[str]
    keyConfirm: Optional[str]
    isConfirmed: Optional[bool]
