class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        mh= [-i for i in c.values()]
        heapq.heapify(mh)

        t= 0
        q = deque()
        while mh or q:
            t += 1
            if not mh:
                t = q[0][1]
            else:
                c = 1 + heapq.heappop(mh)
                if c:
                    q.append([c,t + n])
            if q and q[0][1] == t:
                heapq.heappush(mh, q.popleft()[0])
        return t
    