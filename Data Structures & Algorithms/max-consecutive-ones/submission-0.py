class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        max_count = 0
        for i in nums:
            if i == 0:
                count = 0
            elif i == 1:
                count += 1
            if count > max_count:
                max_count = count
        return max_count