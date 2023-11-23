# TODO решите задачу
import json

def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    result = 0
    for dict_ in data:
        result += dict_["score"] * dict_["weight"]
    return round(result, 3)


print(task())
