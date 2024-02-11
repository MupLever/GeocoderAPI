from random import randint

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class LegalAddress(BaseModel):
    city: str
    street: str
    house_number: int
    apartment_number: int
    entrance_number: int
    floor: int


@app.post("/api/v1/geocoder/")
async def get_geocoordinates(address: LegalAddress):
    return {
        "address": address,
        "coordinates": {"lat": randint(-90, 90), "lng": randint(-180, 180)}
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8001)