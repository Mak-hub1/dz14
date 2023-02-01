import sqlite3
import json


def search_by_actors(first_actor, second_actor):
    with sqlite3.connect('netflix.db') as connection:
        first_actor = f"%{ first_actor }%"
        second_actor = f"%{ second_actor }%"

        cursor = connection.cursor()
        sqlite_query = """
                        select \"cast\"
                        from netflix
                        where \"cast\" like ?
                        and \"cast\" like ?
                    """
        cursor.execute(sqlite_query, (first_actor, second_actor))
        executed_query = cursor.fetchall()
        all_actors = []
        for i in range(len(executed_query)):
            for item in executed_query[i][0].split(', '):
                all_actors.append(item)

        actors_count_dict = dict()

        for item in all_actors:
            if item in actors_count_dict.keys():
                actors_count_dict[item] += 1
            else:
                actors_count_dict[item] = 1

        res_actors_list = []

        for key, value in actors_count_dict.items():
            if value > 2 and key not in ('Rose McIver', 'Ben Lamb'):
                res_actors_list.append(key)

    return res_actors_list


