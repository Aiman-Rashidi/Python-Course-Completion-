from typing import List, Tuple

def process_data(data_base: List[Tuple[str, List[int]]]) -> List[str]:
    result = []
    for name, scores in data_base:
        total_score = sum(scores)
        result.append(f"Name: {name}, Total Score: {total_score}")
    return result

print(process_data([("Aiman", [80, 90]), ("Lyra", [70, 80])]))