class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for words in strs:
            sorted_word = "".join(sorted(words))
            if sorted_word in groups:
                groups[sorted_word].append(words)
            else:
                groups[sorted_word] = [words]
        return list(groups.values())

        