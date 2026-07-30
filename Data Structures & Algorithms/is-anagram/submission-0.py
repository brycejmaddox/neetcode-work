class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for letter in s:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1
        count_t = {}
        for letter in t:
            if letter not in count_t:
                count_t[letter] = 1
            else:
                count_t[letter] += 1
        if count == count_t:
            return True
        else:
            return False
        