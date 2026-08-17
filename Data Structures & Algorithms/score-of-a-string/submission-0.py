class Solution:
    def scoreOfString(self, s: str) -> int:
        scores = []
        for i,char in enumerate(s):
            if i == len(s) - 1:
                pass
            if not i == len(s) - 1:
                indiv_score = abs(ord(s[i+1]) - ord(char))
                scores.append(indiv_score)
        return sum(scores)