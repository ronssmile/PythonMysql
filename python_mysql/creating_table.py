from getpass import getpass
from mysql.connector import connect,Error

try:
    with connect(
        host = "localhost",
        username = input("Enter Username: "),
        password = getpass("Enter Password: "),
        database = "online_movie_rating",
    )as connection:
        create_movies_table_query = """
CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
"""
        create_example_table_query="""
CREATE TABLE example (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)

)           
"""
        create_ratings_table_query = """
CREATE TABLE ratings (
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id)
)
"""     
        alter_table_query = """
        ALTER TABLE movies MODIFY COLUMN collection_in_mil DECIMAL (4,1)
        """
        #print(connection)
        with connection.cursor() as cursor:
            #cursor.execute(create_movies_table_query)
            cursor.execute(create_example_table_query)
            #cursor.execute(create_ratings_table_query)
            connection.commit()
            #cursor.execute(alter_table_query)
            #cursor.execute("DESCRIBE movies")
            #result = cursor.fetchall()
            #print("Movies Table Schema after alteration:")
            #for row in result:
                #print(row)
except Error as e:
    print(e)

