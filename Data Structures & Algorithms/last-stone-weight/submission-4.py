

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            
            if x != y:
                # If x and y are positive, x > y, so x - y is positive.
                # Push the result back.
                heapq.heappush_max(stones, x - y)
        
        # If the list is empty, return 0. Otherwise return the remaining stone.
        return stones[0] if stones else 0