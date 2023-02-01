import sqlite3
import json


def search_by_release_year(start_year, end_year):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = """
                        select title, release_year
                        from netflix
                        where release_year between ? and ?
                        order by release_year asc
                        limit 100
                    """
        cursor.execute(sqlite_query, (start_year, end_year))
        executed_query = cursor.fetchall()
        answer_list = [dict((cursor.description[i][0], value) for i, value in enumerate(row)) for row in executed_query]
        res = json.dumps(answer_list)
    return res



