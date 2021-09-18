import pandas as pd
from flask import Flask

import util

app = Flask(__name__)
data = []


@app.route("/hello")
def index():
    return "Hello"


@app.route("/<classone>/<classtwo>")
def classes(classone, classtwo):
    util.compare_tracks(classone, classtwo)
    return {
        "classone": classone,
        "classtwo": classtwo
    }


def load_csv():
    csvs = []
    for file in util.tracks:
        path = "./data/" + file + ".csv"
        print(path)
        list = util.get_class_list(pd.read_csv(path))
        csvs.append(list)


if __name__ == "__main__":
    data = load_csv()

    app.run(port=8081)
