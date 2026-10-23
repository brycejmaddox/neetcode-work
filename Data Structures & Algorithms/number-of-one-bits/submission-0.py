class Solution:
    def hammingWeight(self, n: int) -> int:
        new = bin(n)
        new2 = new.replace("0","").replace("b", "")
        return len(new2)
        