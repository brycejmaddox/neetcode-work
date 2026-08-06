from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        consec = {}
        streak = 0
        longest_streak = 0
        for i,num in enumerate(nums_sorted):
            if consec == {}:
                consec[num] = i
                streak += 1
            elif num in consec:
                continue
            elif num - 1 in consec:
                consec[num] = i
                streak += 1
            else:
                streak = 0
                consec[num] = i
                streak += 1
            if streak > longest_streak:
                longest_streak = streak
        return longest_streak

        