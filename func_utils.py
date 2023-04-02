import requests
from flask import jsonify, request

def list_movies_foo(movie_url: str):
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    sorted_movies = sorted(movies, key=lambda movie: movie['id'])
    return jsonify(sorted_movies)

def list_characters_foo(movie_url: str):
    data = requests.get(movie_url).json()
    wanted_id = request.args.get('episode_id', default=-1, type=int)
    characters = [movie["characters"] for movie in data["results"] if movie["episode_id"] == wanted_id] if wanted_id != -1 else [item for sublist in [movie["characters"] for movie in data["results"]] for item in sublist]
    names = [requests.get(character).json()['name'] for character in characters[0]]
    return jsonify(names)