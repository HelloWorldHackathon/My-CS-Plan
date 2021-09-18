import re

import pandas as pd
import requests

classes_api = "http://api.purdue.io/odata/Courses?%24filter=Subject/Abbreviation%20eq%20%27<abbr>%27&%24orderby=Number%20asc"

tracks = ["(Algorithmic) Foundations Track",
          "Computational Science and Engineering Track",
          "Computer Graphics and Visualization Track",
          "Database and Information Systems Track",
          "Machine Intelligence Track",
          "Programming Language Track",
          "Security Track",
          "Software Engineering Track",
          "Systems Software Track"]


def get_class_list(track:pd.DataFrame):
    classes = []
    shape = track.shape
    for i in range(shape[0]):
        req1 = []
        for j in range(shape[1]):
            req = track.iat[i, j]
            if req != "NAXXX" and not "Req" in req:
                if "Electives" in req:
                    req = int(req[0])
                req1.append(req)
        classes.append(req1)

    return classes


def compare_tracks(track1, track2):
    print(track1['1'][0])


def get_name(classnum: str) -> str:
    # handle edge cases
    if classnum == "NAXXX":
        return classnum
    if re.match("CS \\dXX", classnum):
        return classnum
    if classnum.__contains__("-"):
        return classnum
    if classnum.__contains__("/"):
        return classnum
    if classnum.__contains__("CS 490"):
        return "Senior Project"

    if re.match("\\w+ \\d+", classnum):
        split = classnum.split(" ")
        abbr = split[0]
        num = split[1]

        r = requests.get(classes_api.replace("<abbr>", abbr))
        raw_data = r.json()
        classes = raw_data["value"]
        for cls in classes:
            if cls["Number"] == num:
                return cls["Title"]

    return "Error!"
