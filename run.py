import sqlite3
from utils.search_by_name import search_by_name
from utils.search_by_release_year import search_by_release_year
from utils.search_by_rating import search_by_rating
from utils.search_by_genre import search_by_genre
from utils.search_by_actors import search_by_actors
from utils.search_by_many_parameters import search_by_many_parameters

from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index_page():
    return 'Hey'


@app.route('/movie/<title>')
def movie_by_name(title):
    result = search_by_name(title)
    return result


@app.route('/movie/<start_year>/to/<end_year>')
def movies_by_year(start_year, end_year):
    result = search_by_release_year(start_year, end_year)
    return result


@app.route('/rating/<rating>')
def movies_by_rating(rating):
    result = search_by_rating(rating)
    return result


@app.route('/genre/<genre>')
def movies_by_genre(genre):
    result = search_by_genre(genre)
    return result


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == '__main__':
    app.run()

