import re
from typing import List

import pandas as pd
import requests
from requests.api import get

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
            if req != "NAXXX":
                if "Req" in req:
                    req = 1
                if "Electives" in str(req):
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
    classes = []
    to_remove = []
    # loops through all the requirements in the first track to see if any reqs only have one option
    for requirement1 in track1:
        if len(requirement1) == 2:
            if not requirement1[1] in classes:
                classes.append(requirement1[1])
                to_remove.append(requirement1)
                for req_number in range(len(track2) - 1):
                    req2 = track2[req_number]
                    for course in req2:
                        if course is requirement1[1]:
                            track2.pop(req_number)
    # removes requirements satisfied from previous loop from track 1
    for i in range(len(to_remove)):
        track1.remove(to_remove[i])

    to_remove.clear()
    for requirement2 in track2:
        if len(requirement2) == 2:
            if not requirement2[1] in classes:
                classes.append(requirement2[1])
                to_remove.append(requirement2)
                for req_number in range(len(track1) - 1):
                    req2 = track1[req_number]
                    for course in req2:
                        if course is requirement2[1]:
                            track1.pop(req_number)
    # removes requirements satisfied from previous loop from track 1
    for i in range(len(to_remove)):
        track2.remove(to_remove[i])
    to_remove.clear()

    for requirement1 in range(len(track2) - 1):
        for course1 in range(1, len(requirement1)):
            print()

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
            class_lists[abbr] = classes
        classes = list(filter(lambda x: x["Number"] == num, classes))
        return classes[0]["Title"]

    return "Error!"


def format_schedule(schedule_item):
    if type(schedule_item) == str:
        return get_name(schedule_item)
    else:
        return " OR ".join(list(map(lambda x: get_name(x), schedule_item)))