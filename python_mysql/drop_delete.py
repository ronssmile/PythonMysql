from getpass import getpass
from mysql.connector import connect,Error

try:
    with connect(
        host = "localhost",
        username = input("Enter Username: "),
        password = getpass("Enter password: "),
        database = "online_movie_rating"
    )as connection:
        print(connection)

        drop_table_query = '''DROP TABLE ratings'''

        with connection.cursor() as cursor:
            cursor.execute(drop_table_query)
            connection.commit()

except Error as e:
    print(e)