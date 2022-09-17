from typing import Optional
from pydantic import BaseModel


class Account(BaseModel):
    id: Optional[str]
    aid: Optional[str]
    uid: Optional[str]
    title: Optional[str]
    description: Optional[str]
    category: Optional[str]
    email: Optional[str]
    password: Optional[str]
