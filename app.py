import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pYd)?Zx@Vo!0izI'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# when a requests comes to the root director from the home page
@app.route('/')
def index():
    # refer to db connection, which connects to the database and makes a table
    conn = get_db_connection()
    # grabs all the entries from the table and calls them posts 
    # SELECT * FROM posts --> each row is a post (because in init_db.py we made two posts which make two rows in the table)
    posts = conn.execute('SELECT * FROM posts').fetchall()
    # prints posts to the console
    print(posts)
    # just closes the connection (stops for continuously running)
    conn.close()
    # renders the posts and puts them on the html in the front end
    return render_template('index.html', posts=posts)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('create.html')

# updates the font end each time you edit in vscode
app.run(debug=True, port=5500)
