from getpass import getpass
from mysql.connector import connect,Error

try:
    with connect(
        host = "localhost",
        username = input("Enter username: "),
        password = getpass("Enter password: "),
        database = "online_movie_rating"
    )as connection:
        print(connection)
        with connection.cursor() as cursor:
            show_table_query = "DESCRIBE movies"
            cursor.execute(show_table_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)
