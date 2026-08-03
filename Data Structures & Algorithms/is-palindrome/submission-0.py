class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lowered = s.lower()
        s_alnum = "".join([letter for letter in s_lowered if letter.isalnum() ])
        reversed_s = reversed(s_alnum)
        reversed_s_joined = "".join(reversed_s)
        if reversed_s_joined == s_alnum:
            return True
        else:
            return False