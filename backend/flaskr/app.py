import json

from flask import Flask, request
from flaskr import util
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/calculatecourses", methods=["POST"])
def calculatecourses():
    return classes(request.json[0], request.json[1])

@app.route("/<int:classone>/<int:classtwo>")
def classes(classone, classtwo):
    dd = {}

    # ["name", [1, electives], [2, electives]]
    csv_data = util.load_csv(classone, classtwo)

    compared = util.compare_tracks(csv_data[max(int(classone), int(classtwo))], csv_data[min(int(classtwo), int(classone))])

    electives1 = compared[-2]
    electives2 = compared[-1]

    compared.remove(electives1)
    compared.remove(electives2)

    courses = compared
    courses = list(map(lambda x: [" OR ".join(x) if type(
        x) != str else x, util.format_schedule(x), str(util.get_hours(x))], courses))
    dd["courses"] = courses

    required = electives1[0]
    electives1.pop(0)
    electives_data = {
        "required": required,
        "courses": list(map(lambda x: [" OR ".join(x) if type(x) != str else x, util.format_schedule(x), str(util.get_hours(x))], electives1))
    }
    dd["electives1"] = electives_data

    required = electives2[0]
    electives2.pop(0)
    electives_data = {
        "required": required,
        "courses": list(map(lambda x: [" OR ".join(x) if type(x) != str else x, util.format_schedule(x), str(util.get_hours(x))], electives2))
    }
    dd["electives2"] = electives_data

    return dd


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081)

    #for i in range(0, 9):
    #    for j in range(0, 9):
    #        if (i == j):
    #             continue
    #         with open(f"nums/{i}_{j}.json", 'w') as f:
    #             dd = classes(i, j)
    #             f.write(json.dumps(dd))
