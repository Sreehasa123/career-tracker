from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


# Create database and table
def create_database():

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        role TEXT,
        applied_date TEXT,
        application_link TEXT,
        status TEXT

    )
    """)


    connection.commit()
    connection.close()



# Home page
@app.route("/")
def home():

    return render_template("index.html")



# Run database creation first
create_database()

app.run(host="0.0.0.0", port=5000)