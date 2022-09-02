from typing import Optional
from pydantic import BaseModel


class Account(BaseModel):
    id: Optional[str]
    aid: Optional[str]
    category: Optional[str]
    email: Optional[str]
    password: Optional[str]
