import re

import pandas as pd
import requests

classes_api = "http://api.purdue.io/odata/Courses?%24filter=Subject/Abbreviation%20eq%20%27<abbr>%27&%24orderby=Number%20asc"

# abbr -> json
class_lists = {}

tracks = ["(Algorithmic) Foundations Track",
          "Computational Science and Engineering Track",
          "Computer Graphics and Visualization Track",
          "Database and Information Systems Track",
          "Machine Intelligence Track",
          "Programming Language Track",
          "Security Track",
          "Software Engineering Track",
          "Systems Software Track"]


def get_class_list(track: pd.DataFrame):
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


def get_raw_classlist(data):
    """ given the data from load_csv(), just get a straight list of class names """
    cls = []
    for a in data:
        for b in a:
            for c in b:
                cls.append(c)
    return cls
    


def load_csv():
    csvs = []
    for file in tracks:
        path = "./data/" + file + ".csv"
        list = get_class_list(pd.read_csv(path))
        csvs.append(list)
    return csvs


def compare_tracks(track1, track2):
    print()


def get_name(classnum: str) -> str:
    # handle edge cases
    if classnum == "NAXXX":
        return classnum
    if re.match("CS \\dXX", classnum):
        return classnum
    if "-" in classnum:
        return classnum
    if "/" in classnum:
        return classnum
    if "CS 490" in classnum:
        return "Senior Project"
    if "EPICS" in classnum:
        return classnum

    if re.match("\\w+ \\d+", classnum):
        split = classnum.split(" ")
        abbr = split[0]
        num = split[1]

        # add the 00 at the end
        if len(str(num)) == 3:
            num = str(num) + "00"

        if abbr in class_lists.keys():
            classes = class_lists[abbr]
        else:
            r = requests.get(classes_api.replace("<abbr>", abbr))
            raw_data = r.json()
            classes = raw_data["value"]
            class_lists[abbr]=classes
        filter(lambda x: x["Number"] == num, classes)
        return classes[0]["Title"]

    return "Error!"
