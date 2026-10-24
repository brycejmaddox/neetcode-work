import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [x*-1 for x in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) > 1:
            l1 = heapq.heappop(stones_heap)
            l2= heapq.heappop(stones_heap)
            l1 = l1 * -1
            l2 = l2 * -1
            if l1 == l2:
                continue
            elif l1 > l2:
                new = l1 - l2
                heapq.heappush(stones_heap, -new)

        if not stones_heap:
            return 0
        else: 
            return -heapq.heappop(stones_heap)

