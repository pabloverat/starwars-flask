import os
from flask import Flask
# import requests
# from flask import jsonify, request

from func_utils import *

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)

movie_url = "https://swapi.dev/api/films/"

@app.route("/", methods=['GET'])
def list_movies():
    return list_movies_foo(movie_url=movie_url)

@app.route("/characters", methods=['GET'])
def list_characters():
    return list_characters_foo(movie_url=movie_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
