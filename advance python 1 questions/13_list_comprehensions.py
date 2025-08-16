from typing import List

def process_numbers(nums: List[int]) -> List[int]:
    result = [number*number for number in nums if number % 2 == 0]
    return result

nums = [1, 2, 3, 4, 5, 6]
print(process_numbers(nums))