from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


<<<<<<< HEAD
app.run(port=8001)
=======
app.run(host='0.0.0.0', port=8001)
>>>>>>> c19934c5a5879568bf0cf8f8c3a9cf697768d5ff
