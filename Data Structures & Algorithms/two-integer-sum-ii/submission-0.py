from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i,value in enumerate(numbers):
            needed = target - value
            if needed in seen:
                return [seen[needed], i + 1]
            seen[value] = i+1

        