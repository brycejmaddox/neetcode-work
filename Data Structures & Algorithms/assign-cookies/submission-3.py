class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        g_pointer, s_pointer = 0,0
        while g_pointer <= len(g) - 1 and s_pointer <= len(s) - 1:
            if g[g_pointer] > s[s_pointer]:
                s_pointer += 1
            else:
                res += 1
                g_pointer += 1
                s_pointer += 1

        return res



        