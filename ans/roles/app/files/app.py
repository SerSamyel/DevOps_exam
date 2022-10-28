import os

import psycopg2
from flask import Flask

app = Flask(__name__)

def db_is_alive():
    host = os.getenv('DB_HOST')
    name = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    connect_string = f"host='{host}' dbname='{name}' user='{user}' password='{password}'"
    SQL = "SELECT NOW();"
    with psycopg2.connect(connect_string) as conn:
        with conn.cursor() as curs:
            curs.execute(SQL)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route("/ping_db")
def ping_db():
    try:
        db_is_alive()
        return "Живая)"
    except Exception:
        return "Не живая("

if __name__ == "__main__":
    app.run(host='0.0.0.0')
