from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

app = FastAPI()

@app.get("/movies")
def get_movies(country: str = "DE", provider_id: str = "8"):
    if not API_KEY:
        return {"error": "TMDB_API_KEY is missing. Check your .env file."}

    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": API_KEY,
        "watch_region": country,
        "with_watch_providers": provider_id,
        "sort_by": "release_date.desc",
        "language": "en-US"
    }

    response = requests.get(url, params=params)
    
    print("Final request URL:", response.url)
    data = response.json()
    print("TMDb raw response:", data)

    if "status_message" in data:
        return {"error": data["status_message"]}

    results = []
    for movie in data.get("results", []):
        results.append({
            "title": movie.get("title", "Untitled"),
            "release_date": movie.get("release_date", "Unknown")
        })

    return {"movies": results}
