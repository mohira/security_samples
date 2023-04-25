import sqlite3
from pathlib import Path


def main():
    db_path = Path('example.db')

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")

    sample_users = [('Alice',), ('Bob',), ('Charlie',), ('David',)]

    cursor.executemany("INSERT INTO users (name) VALUES (?)", sample_users)
    conn.commit()

    conn.close()


if __name__ == '__main__':
    main()
