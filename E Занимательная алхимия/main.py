import sys

sys.setrecursionlimit(1000000)

potions = [
    {0: 0},
    {1: 1},
    {2: 1},
]

n = int(input())
for _ in range(n - 2):
    _, *ingredients = map(int,(input().split(" ")))
    potion = {}
    for i in ingredients:
        if i in potion:
            potion[i] += 1
        else:
            potion[i] = 1
    potions.append(potion)


def basic_ingredients(n: int, prev_elem: int = None):
    
    a_b_count = {
        "A": 0,
        "B": 0
    }

    pot = potions[n]
    for key, value in pot.items():
        if key == prev_elem:
            return
        
        if key == 1:
            a_b_count["A"] += value
        elif key == 2:
            a_b_count["B"] += value
        else:
            data = basic_ingredients(key, prev_elem = n)
            if not data:
                return
            a_b_count["A"] += data["A"] * value
            a_b_count["B"] += data["B"] * value

    return a_b_count

data_for_return = []
q = int(input())
for _ in range(q):
    x, y, s = map(int, input().split(" "))
    base_elem_data = basic_ingredients(s)
    if base_elem_data and base_elem_data["A"] <= x and base_elem_data["B"] <= y:
        data_for_return.append("1")
    else:
        data_for_return.append("0")

for i in data_for_return:
    print(i, end="")