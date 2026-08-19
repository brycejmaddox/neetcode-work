class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Sort solution. Not Binary Search
        nums.sort()
        return nums[0]
        