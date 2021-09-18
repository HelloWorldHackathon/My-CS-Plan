from flask import Flask
import pandas as pd
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
    csvs=[]
    for file in util.tracks:
        path = "./data/" + file + ".csv"
        print(path)
        csvs.append(pd.read_csv(path))

if __name__ == "__main__":
    data = load_csv();

    app.run(port=8081)

