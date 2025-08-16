from typing import Dict, Union

def get_user_info(name : str, age : int) -> Dict[str, Union[int, str]]:
    return {"username": name, "age": age}

print(get_user_info("Aiman", 19))