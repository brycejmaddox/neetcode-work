from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for value in operations:
            if value not in "+CD":
                record.append(int(value))
            elif value == "+":
                record.append(sum(record[-2:]))
            elif value == "C":
                record.pop()
            elif value == "D":
                record.append(record[-1] * 2)
        return sum(record)