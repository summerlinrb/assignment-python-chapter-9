import sqlite3

print("Getting data")
db_name = "db.sqlite3"
with sqlite3.connect(db_name) as conn:
    sql_command = "SELECT * FROM Movies"
    cursor = conn.execute(sql_command)
    for row in cursor:
        print(f"The Movie {row[1]} was released in {row[2]}")


print("Getting Data")
db_name = "db.sqlite3"
with sqlite3.connect(db_name) as conn:
    sql_command = "SELECT * FROM Movies WHERE Year > 1985"
    cursor = conn.execute(sql_command)
    for row in cursor:
        print(f"The movie {row[1]} was released in {row[2]}")


print("Getting Data")
db_name = "db.sqlite3"
with sqlite3.connect(db_name) as conn:
    sql_command = "SELECT * FROM Movies"
    cursor = conn.execute(sql_command)
    movies = cursor.fetchall()
    print(movies)
