num: int = 7
name: str = "Aiman"

def sum(num1: int, num2: int) -> int:
    return num1 + num2
print(sum(3, 4))



from typing import List, Tuple, Dict, Union

number_list: List[int] = [1, 2, 3, 4, 5]
person_age: Tuple[str, int] = ("Aiman", 19)
scores: Dict[str, int] = {"Aiman": 90, "Harry": 89}
identifier: Union[int, str] = "Aiman"