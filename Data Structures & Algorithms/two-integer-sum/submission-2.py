class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,val in enumerate(nums):
            other = target - val
            if other in seen:
                return [seen[other],i]
            else:
                seen[val] = i
                
        