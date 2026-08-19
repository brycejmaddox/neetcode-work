class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best_area = 0
        # Establish l and r pointers
        l,r = 0,len(heights) - 1
        # While loop to use pointers
        while l < r:
            # Area formula, select whichever height is less since that'd be the height of the container
            area = min(heights[l],heights[r]) * (r-l)
            # Comparing current area to best area, whichever one is greater becomes the new best area
            best_area  = max(best_area,area)
            # Need to compare heights of l and r pointers to determine which pointer to move 
            # If the height of l pointer is less, we move l to the right, attempting to find a greater height that could increase the area
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return best_area