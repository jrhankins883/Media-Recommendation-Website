from flask import Flask
from dotenv import load_dotenv
import os
import tmdbsimple as tmdb
import requests
import random

# Loading environment variables from the .env file
load_dotenv()

# Accessing the TMDb API key
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Initializing the Flask app
app = Flask(__name__) # This creates an instance of the Flask class and assigns it to a variable. It's like creating a blueprint for the app

# Fetches a list of movie genres from TMDb API and should return a list of genre dictionaries
def fetch_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {"api_key": TMDB_API_KEY}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("genres", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching genres: {e}")
        return []

def fetch_movies_by_genre(genre_id, api_key):
    base_url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": api_key,
        "with_genres": genre_id,
        "page": random.randint(1, 10) # Randomly picks a page to vary results
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() # Raises an error for bad HTTP status codes
        data = response.json()
        movies = data.get("results", []) # Extract movies from the response
        return movies[:20]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies for genre {genre_id}: {e}")
        return []
    
# Define's a route for the home page
@app.route("/") # This is a route decorator. It tells Flask which URL to connect to this function
def home(): # This function runs when someone visits the specified route
    return "Hello, Flask!"

# Define's a route to display genres
@app.route("/genres")
def genres():
    genres = fetch_genres()
    return "<br>".join([f"{genre['id']}: {genre['name']}" for genre in genres])

# Defines a route for fetching movies by genre
@app.route("/movies/<int:genre_id>")
def movies(genre_id):
    movies = fetch_movies_by_genre(genre_id, TMDB_API_KEY)
    
    if not movies:
        return f"No movies found for genre ID: {genre_id}"
    
    # Creating a simple HTML response with movie titles
    movie_titles = "<br>".join([movie["title"] for movie in movies])
    return f"<h2>Movies in Genre ID {genre_id}:</h2><br>{movie_titles}"

# Main execution block
if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
    
    # Example usage of fetch_movies_ny_genre function
    genre_id = 28 # Action genre ID
    movies = fetch_movies_by_genre(genre_id)
    for movie in movies:
        print(movie["title"])