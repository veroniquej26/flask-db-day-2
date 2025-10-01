import sqlite3

# Opens a connection to the database in file database.db
# Similar to running sqlite3 database.db in the terminal
connection = sqlite3.connect('database.db')

# Opens the schema file and runs the SQL code inside it
with open('schema.sql') as f:
    connection.executescript(f.read())

# Creates a cursor object that lets us interact with db
cur = connection.cursor()

# "Seeds" our database by adding 2 blog posts
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

# Commit saves the changes we've made to the DB file
connection.commit()
# Closes the connection to the db
connection.close()