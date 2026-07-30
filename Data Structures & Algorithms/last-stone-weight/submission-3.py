import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. Heapify in-place. Do not assign the return value unless you are sure it returns the list.
        # In standard Python: heapify(stones) returns None.
        # In your environment, check if heapify_max returns the list or None.
        # Safest approach:
        if not stones:
            return 0
            
        # Assuming stones is a list of integers
        heapq.heapify_max(stones) # Modifies stones in place
        
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            
            if x != y:
                # If x and y are positive, x > y, so x - y is positive.
                # Push the result back.
                heapq.heappush_max(stones, x - y)
        
        # If the list is empty, return 0. Otherwise return the remaining stone.
        return stones[0] if stones else 0