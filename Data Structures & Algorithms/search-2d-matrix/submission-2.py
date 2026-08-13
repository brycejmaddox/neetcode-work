class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatten_matrix = [item for sublist in matrix for item in sublist]

        l = 0
        r = len(flatten_matrix) - 1

        while l <= r:

            m = (l+r) // 2
            if flatten_matrix[m] > target:
                r = m - 1
            elif flatten_matrix[m] < target:
                l = m + 1
            elif flatten_matrix[m] == target:
                return True
        return False