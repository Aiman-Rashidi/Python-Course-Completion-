from typing import List

def info_print(students: List[str]) -> str:
    result = str()
    for index, name in enumerate(students, start=1):
        result += f"{index}. {name}\n"
    return result

students = ["Aiman", "Lyra", "Zara", "Ravi"]
print(info_print(students))