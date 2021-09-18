import re

import requests

classes_api = "http://api.purdue.io/odata/Courses?%24filter=Subject/Abbreviation%20eq%20%27<abbr>%27&%24orderby=Number%20asc"


def get_name(classnum: str) -> str:
    # handle CS 3XX
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


if __name__ == "__main__":
    print(get_name("CS 18000"))
    print(get_name("CS 489/490-DSO"))