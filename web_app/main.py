"""WEBAPP"""

from asyncio import exceptions
from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello, World!"}


@app.post("/convert/{state}/{city}")
def convert_state(state: str, city: str):
    """Convert state and city to latitude and longitude using an external API."""
    print(f"Converting state {state}, city {city} to lat/lon")

    lat, lon = None, None

    api_key = "6a7f57138e04b429290986wxia11d90"
    # Invoke-WebRequest -Method POST http://localhost:8000/convert/Minnesota/minneapolis
    payload = {"api_key": api_key, "city": city, "state": state}
    response = requests.get("https://geocode.maps.co/search", params=payload)
    try:
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.HTTPError as e:
        return {"error": f"Could not connect to API: {e}"}

    try:  # Convert from API response to lat/lon
        best_result = response.json()[0]
        lat = best_result["lat"]
        lon = best_result["lon"]
    except Exception as e:
        raise exceptions.HTTPException(
            status_code=500, detail=f"Error parsing API response: {e}"
        )

    result = {"lat": lat, "lon": lon}
    return result
