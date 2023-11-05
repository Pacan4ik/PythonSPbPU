import json


def task() -> float:
    total_product = 0.000

    with open("input.json", "r") as json_file:
        data = json.load(json_file)

    for item in data:
        score = item.get("score")
        weight = item.get("weight")
        product = score * weight
        total_product += product

    return round(total_product, 3)


print(task())
