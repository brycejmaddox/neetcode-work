class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        check = []
        var = 0
        for i in s:
            position = t.find(i,var)
            check.append(position)
            var = position + 1

        copy = list(check.copy())
        check.sort()
        if -1 in check:
            return False
        else:
            return check == copy