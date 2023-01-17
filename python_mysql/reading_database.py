from getpass import getpass
from mysql.connector import connect,Error

#

try:
    with connect(
        host = "localhost",
        username = input("Enter Username: "),
        password = getpass("Enter Password: "),
        database = "online_movie_rating"
    )as connection:
        pass

        select_movies_query = "SELECT * FROM movies LIMIT 5"

        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    pass
