from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        collection = {}
        for number in nums:
            if number in collection:
                collection[number] += 1
            else:
                collection[number] = 1
        result = sorted(collection.items(), key= lambda pair: pair[1], reverse = True)
        values = []
        for number in result:
            values.append(number[0])
        return values[:k]
                    

        