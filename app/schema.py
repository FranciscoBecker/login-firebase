from typing import Optional
from pydantic import BaseModel


class UserData(BaseModel):
    email: str
    password: str
    display_name: Optional[str] = None
    phone_number: Optional[str] = None
    photo_url: Optional[str] = None
