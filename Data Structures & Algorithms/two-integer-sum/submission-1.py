from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            value = target - num
            if value in seen:
                j = seen[value]
                return [j,i]
            seen[num] = i