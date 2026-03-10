from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Mini CTF Platform</h1>
    <a href='/login'>Challenge 1: SQL Injection</a><br>
    <a href='/xss'>Challenge 2: XSS</a>
    """

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        user = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username='{user}' AND password='{password}'"

        result = cursor.execute(query).fetchone()

        if result:
            return "FLAG{SQLI_SUCCESS}"
        else:
            return "Login failed"

    return """
    <form method="post">
    username:<input name="username">
    password:<input name="password">
    <button>login</button>
    </form>
    """

@app.route("/xss")
def xss():

    name = request.args.get("name","guest")

    return f"Hello {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)