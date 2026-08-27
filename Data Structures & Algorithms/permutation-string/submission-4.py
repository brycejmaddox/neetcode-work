class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0, len(s1)
        s1_sorted = sorted(s1)
        while r <= len(s2):
            if s1_sorted == sorted(s2[l:r]):
                print(l,r)
                return True
                
            else:
                l +=1
                r +=1
        print(l,r)
        return False
        
