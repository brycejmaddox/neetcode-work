class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Set res equal to the first index in rotated array
        res = nums[0]
        # Establish pointers
        l,r = 0, len(nums) - 1
        # Needs to be equal or less than because l and r could be the min if they both reach that point
        while l <= r:
            # Initial check to see if value for l is less than that of r, if so we compare to res
            if nums[l] < nums[r]:
                res = min(res, nums[l])
            # Next we move on to checking is m, the middle value of current list, is less than what is currently res
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res