from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for value in operations:
            if value not in "+CD":
                record.append(int(value))
            elif value == "+":
                total_previous = sum(record[-2:])
                record.append(total_previous)
            elif value == "C":
                record.pop()
            elif value == "D":
                doubled = record[-1] * 2
                record.append(doubled)
        total_sum = sum(record)
        return total_sum