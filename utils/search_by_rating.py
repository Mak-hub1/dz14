import sqlite3
import json


def search_by_rating(rating):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        if rating == 'children':
            sqlite_query = """
                            select title, rating, description
                            from netflix
                            where rating = 'G'
                        """
        elif rating == 'family':
            sqlite_query = """
                            select title, rating, description
                            from netflix
                            where rating in ('G', 'PG', 'PG-13')
                        """
        elif rating == 'adult':
            sqlite_query = """
                            select title, rating, description
                            from netflix
                            where rating in ('R', 'NC-17')
                        """
        else:
            return "Подходящих под запрос фильмов не найдено"
        cursor.execute(sqlite_query)
        executed_query = cursor.fetchall()
        answer_list = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in executed_query]
        res = json.dumps(answer_list)
    return res


