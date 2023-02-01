import sqlite3
import json


def search_by_name(title):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        sqlite_query = """
                        select title, country, release_year, listed_in, description
                        from netflix
                        where title = ?
                        order by release_year desc
                        limit 1
                    """
        cursor.execute(sqlite_query, (title,))
        executed_query = cursor.fetchone()
        answer_dict = dict()
        keys_for_dict = ["title", "country", "release_year", "listed_in", "description"]

        for i in range(len(executed_query)):
            answer_dict[keys_for_dict[i]] = executed_query[i]
        res = json.dumps(answer_dict)
    return res


