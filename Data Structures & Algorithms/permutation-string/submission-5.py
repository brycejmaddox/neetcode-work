from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0, len(s1)
        s1_counter = Counter(s1)
        while r <= len(s2):
            if s1_counter == Counter(s2[l:r]):
                print(l,r)
                return True
                
            else:
                l +=1
                r +=1
        print(l,r)
        return False
        
