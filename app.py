from google_auth_oauthlib.flow import Flow
import os

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

@app.route("/connect-gmail")
def connect_gmail():

    flow = Flow.from_client_secrets_file(
        "credentials.json",
        scopes=[
            "https://www.googleapis.com/auth/gmail.readonly"
        ]
    )

    flow.redirect_uri = "http://127.0.0.1:5000/oauth2callback"

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true"
    )

    return redirect(authorization_url)



@app.route("/oauth2callback")
def oauth2callback():

    return "Gmail Connected Successfully!"



# Run database creation first
create_database()

app.run(host="0.0.0.0", port=5000)