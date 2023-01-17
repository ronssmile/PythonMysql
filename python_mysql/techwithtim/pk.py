from getpass import getpass
from mysql.connector import connect,Error

try:
    with connect(
        host = "localhost",
        user = "root",
        password="ron123",
        database = "testdatabase",
    ) as connection:
        # show_db_query= "SHOW DATABASES"
        users = [("tim","techwithtim"),("jose","joey123"),("sarah","sarah123")]

        user_scores = [(45,100),(30,200),(46,124)]

        Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"

        Q2 = "CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

        Q3 = "INSERT INTO Users (name, passwd) VALUES (%s, %s)"

        Q4 = "INSERT INTO Scores (userId, game1, game2) VALUES (%s,%s,%s)"

        with connection.cursor() as cursor:
            """ this part is creating the tables """
            # cursor.execute(Q1) 
            # cursor.execute(Q2)
            """ THIS PART IS TO SHOW ALL THE TABLES CREATED WHICH IS THE Users and Scores"""
            #cursor.execute("SHOW TABLES")
            # for x in cursor:
            #     print(x)
            for x,user in enumerate(users):
                cursor.execute(Q3, user)
                last_id = cursor.lastrowid
                cursor.execute(Q4, (last_id,)+ user_scores[x])
            #connection.commit()
            cursor.execute("SELECT * FROM Users")
            for x in cursor:
                print(x)

            cursor.execute("SELECT * FROM Scores")
            for x in cursor:
                print(x)


            













except Error as e:
    print(e)
