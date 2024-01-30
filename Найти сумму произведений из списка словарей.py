# TODO решите задачу
import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    return sum([dict_["score"] * dict_["weight"] for dict_ in data]).__round__(3)


print(task())
