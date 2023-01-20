from getpass import getpass
from mysql.connector import connect,Error
from convert_csv_json import data

reviewers_records = data
try:
    with connect(
        host = "localhost",
        username = input("Enter Username: "),
        password = getpass("Enter password: "),
        database = "online_movie_rating"
    ) as connection:
        pass
        insert_reviewers_query = """
            INSERT INTO example(first_name, last_name)
            VALUES ( %s, %s)
            """

        with connection.cursor() as cursor:
            cursor.executemany(insert_reviewers_query,reviewers_records)
            connection.commit()
            
except Error as e:
    print(e)