import json

from flask import Flask

from util import compare_tracks, format_schedule, get_hours, load_csv

app = Flask(__name__)
data = []


def classes(classone, classtwo):
    dd = {}

    # ["name", [1, electives], [2, electives]]
    compared = compare_tracks(data[int(classone)], data[int(classtwo)])

    electives1 = compared[-2]
    electives2 = compared[-1]

    compared.remove(electives1)
    compared.remove(electives2)

    courses = compared
    courses = list(map(lambda x: [" OR ".join(x) if type(
        x) != str else x, format_schedule(x), str(get_hours(x))], courses))
    dd["courses"] = courses

    required = electives1[0]
    electives1.pop(0)
    electives_data = {
        "required": required,
        "courses": list(map(lambda x: [" OR ".join(x) if type(x) != str else x, format_schedule(x), str(get_hours(x))], electives1))
    }
    dd["electives1"] = electives_data

    required = electives2[0]
    electives2.pop(0)
    electives_data = {
        "required": required,
        "courses": list(map(lambda x: [" OR ".join(x) if type(x) != str else x, format_schedule(x), str(get_hours(x))], electives2))
    }
    dd["electives2"] = electives_data

    return dd


if __name__ == "__main__":
    data = load_csv()

    # app.run(host="0.0.0.0", port=8081)

    for i in range(0, 9):
        for j in range(0, 9):
            if (i == j):
                continue
            with open(f"nums/{i}_{j}.json", 'w') as f:
                dd = classes(i, j)
                f.write(json.dumps(dd))
