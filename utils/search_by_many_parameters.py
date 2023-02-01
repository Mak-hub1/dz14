import sqlite3
import json


def search_by_many_parameters(movie_type, release_year, genre):
    """
    :param movie_type:
    :param release_year:
    :param genre:
    :return:
    """
    with sqlite3.connect('netflix.db') as connection:
        genre = f'%{genre}%'
        cursor = connection.cursor()
        sqlite_query = """
                        select title, description
                        from netflix
                        where type = ?
                        and release_year = ?
                        and listed_in like ?
                        order by title asc
                    """
        cursor.execute(sqlite_query, (movie_type, release_year, genre))
        executed_query = cursor.fetchall()
        answer_list = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in executed_query]
        res = json.dumps(answer_list)
    return res


