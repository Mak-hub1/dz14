import sqlite3
import json


def search_by_genre(genre):
    with sqlite3.connect('netflix.db') as connection:
        genre = f'%{genre}%'
        cursor = connection.cursor()
        sqlite_query = """
                            select title, description
                            from netflix
                            where listed_in like ?
                            order by title
                            limit 10
                        """
        cursor.execute(sqlite_query, (genre,))
        executed_query = cursor.fetchall()
        answer_list = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in executed_query]
        res = json.dumps(answer_list)
    return res



