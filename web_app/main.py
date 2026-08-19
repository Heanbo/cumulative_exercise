from fastapi import FastAPI
import requests

app = FastAPI()


# @app.get("/")
# async def index():
#     return {"message": "Hello, World!"}


@app.post("/convert{state}")
def convert_state(state: str, city: str):
    # Placeholder for state conversion logic
    return {"lat": city, "State": state}


api_key = "6a7f57138e04b429290986wxia11d90"

response = requests.get("https://geocode.maps.co/search", data=payload)

best_result = response.json()[0]

lat = best_result["lat"]
lon = best_result["lon"]

result = {"lat": lat, "lon": lon}
