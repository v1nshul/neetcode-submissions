class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m = []
        for x,y in points:
            m.append([(x**2+y**2),x,y])

        heapq.heapify(m)

        res = []
        while k > 0:
            dist,x,y= heapq.heappop(m)
            res.append([x,y])
            k -= 1
        return res