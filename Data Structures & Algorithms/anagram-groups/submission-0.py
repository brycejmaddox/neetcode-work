from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        for word in strs:
            sorted_word = sorted(word)
            signature = "".join(sorted_word)
            if signature in grouped_anagrams:
                grouped_anagrams[signature].append(word)
            else:
                grouped_anagrams[signature] = [word]
        return list(grouped_anagrams.values())
        