class Solution:
    def isPalindrome(self, s: str) -> bool:
        onlyalnum = "".join(char for char in s if char.isalnum()).lower()
        reversed_lowered = "".join(reversed(onlyalnum.lower()))
        if reversed_lowered == onlyalnum:
            return True
        else:
            return False

        