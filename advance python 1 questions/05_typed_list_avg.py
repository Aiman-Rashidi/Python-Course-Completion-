from typing import List

def average(num_list : List[float]) -> float:
    return sum(num_list) / len(num_list)

print(average([1, 2, 3, 5.5]))