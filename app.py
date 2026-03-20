from flake8 import Flake8, render_template


app = Flake8(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
