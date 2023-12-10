from flask import Flask, render_template
import json

app = Flask(
    __name__,
    static_url_path="/static",
    static_folder="static",
    template_folder="templates",
)


@staticmethod
@app.route("/")
def home():
    return render_template("home.html", page="home")


@staticmethod
@app.route("/products")
def products():
    with open("flask-app\data.json", "r") as file:
        data = json.load(file)
    return render_template("products.html", page="products", products=data["products"])


@staticmethod
@app.route("/login")
def login():
    return render_template("login.html")


@staticmethod
@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
