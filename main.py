from random import random
from json import JSONDecodeError

import requests
from urllib.parse import quote
import uvicorn
from fastapi import FastAPI

from schemas import LegalAddress
from configs.logger import logger
from configs.params import params
from configs.headers import headers


app = FastAPI()


@app.post("/api/v1/geocoder/")
async def get_geocoordinates(address: LegalAddress):
    url = "https://suggest-maps.yandex.ru/suggest-geo?"
    params["part"] = quote(', '.join(address.model_dump(exclude_none=True).values()))

    url += "&".join([f"{param}={value}" for param, value in params.items()])

    try:
        response = requests.get(url, headers=headers).json()
        coords = response.get("results")[0].get("pos")
        lng, lat = coords.split(",")
        logger.info(f"Received from the Yandex API {lng=} {lat=}")
    except JSONDecodeError:
        lat, lng = round(random() * 55, 6), round(random() * 37, 6)
    except AttributeError:
        lat, lng = round(random() * 55, 6), round(random() * 37, 6)
    except IndexError:
        lat, lng = round(random() * 55, 6), round(random() * 37, 6)

    return {
        "address": address.model_dump(),
        "coordinates": {"lat": str(lat), "lng": str(lng)}
    }


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8001)
