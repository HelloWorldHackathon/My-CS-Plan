from typing import List, final

import re


def evaluate(first_track: List[List[any]], second_track: List[List[any]]) -> List[str]:
    """Evaluate the first and second track, and return a list of track names that is the smallest
    first and second are a list of list of class names where the first "class name" is the number required in the following classes
    The last list of classes is always electives
    """
    final_schedule = []

    # add all the single requirements to the final schedule
    final_schedule.extend(remove_singles(first_track, final_schedule))
    final_schedule.extend(remove_singles(second_track, final_schedule))

    # check overlap
    final_schedule.append(remove_non_overlapping(
        first_track, second_track, final_schedule))
    final_schedule.append(remove_non_overlapping(
        second_track, first_track, final_schedule))

    final_schedule = list(filter(lambda x: not re.match("\\d+", str(x)), final_schedule))
    final_schedule = list(map(lambda x: x.strip() if type(x) == str else x, final_schedule))
    return final_schedule


def remove_non_overlapping(first_track: List[List[any]], second_track: List[List[any]], final_schedule: List[any]) -> List[str]:
    non_overlapping = []
    for classes in first_track:
        # each class (ex. CS 180, MA 261)
        for cls in classes:
            # class list (ex. [1, MA 161, CS 193, CS 191])
            if cls in [classname for classlist in second_track for classname in classlist]:
                continue
            else:
                non_overlapping.append(cls)
                classes.remove(cls)
    non_overlapping = list(filter(lambda x: not re.match("\\d+", str(x)), non_overlapping))
    return non_overlapping


def remove_singles(track: List[List[any]], final_schedule: List[any]) -> List[str]:
    singles = []
    for class_list in track:
        if (is_minimum_requirement_amount(class_list)):
            # append the first class in the list
            # the first element is always the amount required of this class list
            if class_list[1] not in final_schedule:
                singles.append(class_list[1])
            track.remove(class_list)
    return singles


def is_minimum_requirement_amount(class_list: List[str]) -> bool:
    try:
        if int(class_list[0]) == 1:
            return True
        return False
    except:
        return False
