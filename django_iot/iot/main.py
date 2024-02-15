import threading
import sqlite3
import requests
import random
import datetime
import time

host, port = "127.0.0.1", 8000

db = "iot\db.db"
table = "vehicle"
columns = [
    "id",
    "serial_id",
    "x",
    "y",
    "is_working",
    "fuel",
    "speed",
    "date",
]
types = [
    "INTEGER PRIMARY KEY AUTOINCREMENT",
    "INTEGER",
    "INTEGER",
    "INTEGER",
    "BOOLEAN",
    "INTEGER",
    "INTEGER",
    "TEXT",
]


def query(db: str, sql: str, args: tuple, many: bool = True) -> list[tuple] | tuple:
    try:
        with sqlite3.connect(db) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, args)
            if many:
                return cursor.fetchall()
            return cursor.fetchone()
    except Exception as error:
        return error


def get():
    while True:
        try:
            serial_id = random.randint(1, 100)
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            is_working = random.choice([True, False])
            fuel = random.randint(0, 100)
            speed = random.randint(0, 100)
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            query(
                db=db,
                sql=f"INSERT INTO {table} ({', '.join(columns[1:])}) VALUES (?, ?, ?, ?, ?, ?, ?)",
                args=(serial_id, x, y, is_working, fuel, speed, date),
            )
        except Exception as error:
            print(get.__name__, error)
        time.sleep(5)


def post():
    while True:
        try:
            data = query(
                db=db,
                sql=f"SELECT {', '.join(columns)} FROM {table} ORDER BY {columns[0]} DESC LIMIT 5",
                args=(),
            )
            json_data = [dict(zip(columns, x)) for x in data]
            response = requests.post(f"http://{host}:{port}/api", json=json_data)
            if response.status_code == 200 or response.status_code == 201:
                query(
                    db=db,
                    sql=f"DELETE FROM {table} WHERE id IN ({', '.join('?' * len(json_data))})",
                    args=tuple(x["id"] for x in json_data),
                )
        except Exception as error:
            print(post.__name__, error)
        time.sleep(5)


if __name__ == "__main__":
    query(
        db=db,
        sql=f"CREATE TABLE IF NOT EXISTS {table} ({', '.join([f'{column} {type}' for column, type in list(zip(columns, types))])})",
        args=(),
    )
    threading.Thread(target=get).start()
    threading.Thread(target=post).start()
