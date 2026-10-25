import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x1 = 0
        y1 = 0
        def distance(x2,y2):
            length = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            return length
        output = []
        for val in points:
            length = distance(val[0],val[1])
            output.append((length, val))
        heapq.heapify(output)
        result = []
        while len(result) < k:
            popped = heapq.heappop(output)
            result.append(popped[1])
        return result



