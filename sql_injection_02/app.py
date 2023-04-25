import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('query')
    conn = sqlite3.connect('example.db')

    cursor = conn.cursor()

    sql = "SELECT * FROM users WHERE name LIKE ?"
    query = cursor.execute(sql, ('%' + search_query + '%',))
    results = query.fetchall()

    conn.close()

    return render_template('search_results.html', results=results)


if __name__ == '__main__':
    app.run(debug=True, port=7777)
