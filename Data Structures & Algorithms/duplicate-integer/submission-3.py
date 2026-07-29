from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i,num in enumerate(nums):
            if num in seen:
                return bool(1)
            seen[num] = i 
        return bool()