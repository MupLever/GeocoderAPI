from typing import Optional

from pydantic import BaseModel


class LegalAddress(BaseModel):
    city: Optional[str] = None
    district: Optional[str] = None
    street: Optional[str] = None
    house_number: Optional[str] = None
