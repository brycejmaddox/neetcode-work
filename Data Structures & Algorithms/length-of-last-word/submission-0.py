class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string_list = s.split()
        last_word = string_list[-1]
        return len(last_word)
        