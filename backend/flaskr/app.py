import pandas as pd
from flask import Flask

from util import compare_tracks, load_csv, get_name, get_hours

app = Flask(__name__)
data = []


@app.route("/<classone>/<classtwo>")
def classes(classone: int, classtwo: int):
    # ["name", [1, electives], [2, electives]]
    data = {}

    compared = compare_tracks(classone, classtwo)
    courses = compared[0]
    courses = list(map(lambda x: [x, get_name(x), get_hours(x)], courses))
    data["courses"] = courses

    electives = compared[1]
    required = electives[0]
    electives.pop(0)
    electives_data = {
        "required": required,
        "courses": list(map(lambda x: [x, get_name(x), get_hours(x)], courses)) 
    }
    data["electives1"] = electives_data

    electives = compared[2]
    required = electives[0]
    electives.pop(0)
    electives_data = {
        "required": required,
        "courses": list(map(lambda x: [x, get_name(x), get_hours(x)], courses)) 
    }
    data["electives2"] = electives_data

    return data



if __name__ == "__main__":
    data = load_csv()

    app.run(host="0.0.0.0", port=8081)
