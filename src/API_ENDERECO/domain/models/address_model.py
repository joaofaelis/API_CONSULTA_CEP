from typing import TypedDict


class AddressModel(TypedDict):
    code: str
    state: str
    city: str
    district: str
    address: str
    consultation_date: float
