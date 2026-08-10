from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_dict = {}
        for i,value in enumerate(nums):
            if value == target:
                return i
        return -1