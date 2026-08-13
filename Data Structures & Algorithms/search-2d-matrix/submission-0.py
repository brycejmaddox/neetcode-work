class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatten_matrix = [item for sublist in matrix for item in sublist]

        l = 0
        r = len(flatten_matrix) - 1
        if len(flatten_matrix) == 1 and flatten_matrix[0] == target:
            return True
        while l < r:
            if flatten_matrix[l] == target or flatten_matrix[r] == target:
                return True
            m = (l+r) // 2
            if flatten_matrix[m] > target:
                r = m - 1
            elif flatten_matrix[m] < target:
                l = m + 1
            elif flatten_matrix[m] == target or flatten_matrix[l]:
                return True
        return False