import pandas as pd
from flask import Flask

from util import load_csv, compare_tracks

app = Flask(__name__)
data = []


@app.route("/hello")
def index():
    return "Hello"


@app.route("/<classone>/<classtwo>")
def classes(classone, classtwo):
    compare_tracks(classone, classtwo)
    return {
        "classone": classone,
        "classtwo": classtwo
    }


if __name__ == "__main__":
    data = load_csv()

    app.run(port=8081)
