class Solution:
    def isValid(self, s: str) -> bool:
        collection = {")":"(","]":"[","}":"{"}
        stack = []
        for char in s:
            if char in collection:
                top_element = stack.pop() if stack else '#'
                if collection[char] != top_element:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        