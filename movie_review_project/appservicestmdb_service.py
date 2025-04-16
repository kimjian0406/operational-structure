import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

def fetch_popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page=1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("results", [])
    return []

