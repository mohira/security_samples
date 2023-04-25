from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/')
def xss_example():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DOM-based XSS Example</title>
    </head>
    <body>
        <h1>DOM-based XSS Example</h1>
        <p>Search: <input size=100 type="text" id="search" value="Type your search..."></p>
        <button onclick="displaySearch()">Search</button>
        <p id="result"></p>

        <script>
            function displaySearch() {
                const search = document.getElementById("search").value;
                document.getElementById("result").innerHTML = "You searched for: " + search;
            }
        </script>
    </body>
    </html>
    """)


if __name__ == '__main__':
    app.run(debug=True)
