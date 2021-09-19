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

    remove_singles(track1, track2, classes)

    remove_singles(track2, track1,classes)
    remove_no_overlap(track1, track2, classes)
    remove_no_overlap(track2, track1, classes)

    track1[-1] = list_remaining_electives(track1, classes)

    track2[-1] = list_remaining_electives(track2, classes)

    classes.extend([track1[-1]])
    classes.extend([track2[-1]])
    print(classes)
    return classes




def remove_no_overlap(track1, track2, classes):

    to_remove = []
    for requirement1_index in range(len(track1) - 1):
        requirement1 = track1[requirement1_index]
        req1_in_Track2 = False
        course1_index = 1
        while course1_index < len(requirement1):
            course1 = requirement1[course1_index]
            requirement2_index = 0
            while requirement2_index < len(track2)-1:
                requirement2 = track2[requirement2_index]
                course2_index = 1
                while course2_index < len(requirement2):
                    course2 = requirement2[course2_index]
                    if course2 == course1:
                        if not course2 in classes:
                            classes.append(course2)
                        req1_in_Track2 = True
                        course2_index = 100
                        requirement2_index = 100
                        course1_index = 100
                    course2_index += 1
                requirement2_index += 1
            course1_index +=1
        if not req1_in_Track2:
            classes.append(requirement1[1:])
            to_remove.append(requirement1)
    # removes requirements satisfied from previous loop from track 1
    for i in range(len(to_remove)):
        track1.remove(to_remove[i])
    to_remove.clear()
    return classes


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


def get_hours(classnum: str) -> str:
    # handle edge cases
    if classnum == "NAXXX":
        return classnum
    if re.match("CS \\dXX", classnum):
        return "Unknown!"
    if "-" in classnum:
        return "Unknown!"
    if "/" in classnum:
        return "Unknown!"
    if "CS 490" in classnum:
        return "Unknown!"
    if "EPICS" in classnum:
        return "Unknown!"

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
        return classes[0]["CreditHours"]

    return "Error!"

def remove_singles(track1, track2, classes):
    # loops through all the requirements in the first track to see if any reqs only have one option

    to_remove = []
    for requirement1 in track1:
        if len(requirement1) == 2:
            if not requirement1[1] in classes:
                classes.append(requirement1[1])
                to_remove.append(requirement1)
                for req_number in range(len(track2) - 1):
                    req2 = track2[req_number]
                    for course in req2:
                        if course == requirement1[1]:
                            track2.pop(req_number)
    # removes requirements satisfied from previous loop from track 1
    for i in range(len(to_remove)):
        track1.remove(to_remove[i])
    to_remove.clear()
    return classes




def format_schedule(schedule_item):
    if type(schedule_item) == str:
        return get_name(schedule_item)
    else:
        return " OR ".join(list(map(lambda x: get_name(x), schedule_item)))

def list_remaining_electives(track, classes):
    electives_list = track[-1][1:]
    number_of_electives = track[-1][0]
    to_remove = []
    for elective in electives_list:

        for course_index in range(len(classes)):
            course = classes[course_index]
            if type(course) == str:
                if course == elective:
                    to_remove.append(elective)
                    number_of_electives -= 1
                    continue
            else:
                sub_course_index = 0
                while sub_course_index < len(course):
                    sub_course = course[sub_course_index]
                    if sub_course == elective:
                        to_remove.append(elective)
                        number_of_electives -= 1
                        classes[course_index] = sub_course
                        sub_course_index = 100
                    sub_course_index += 1
            course_index += 1
        if number_of_electives <= 0:
            break
    for course in to_remove:
        electives_list.remove(course)
    to_remove.clear()
    electives = [number_of_electives]
    electives.extend(electives_list)

    return electives
