class Solution:
    def isValid(self, s: str) -> bool:
        collection = {")":"(","]":"[","}":"{"}
        stack = []
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char in collection:
                top_element = stack.pop() if stack else '#'

                if collection[char] != top_element:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False
        