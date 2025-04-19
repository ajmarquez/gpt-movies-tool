import requests

API_KEY = XXX
BASE_URL = "https://api.themoviedb.org/3"

def get_latest_movies(country="DE", provider_id="8"):  # Netflix = 8
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": API_KEY,
        "watch_region": country,
        "with_watch_providers": provider_id,
        "sort_by": "release_date.desc",
        "language": "en-US"
    }

    response = requests.get(url, params=params)
    data = response.json()

    print("\nLatest Movies:\n")
    for movie in data.get("results", []):
        title = movie.get("title", "Untitled")
        date = movie.get("release_date", "Unknown")
        print(f"- {title} ({date})")

# Call the function to test it
get_latest_movies()
