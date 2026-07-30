class MedianFinder:

    def __init__(self):
        self.d = []

    def addNum(self, num: int) -> None:
        self.d.append(num)

    def findMedian(self) -> float:
        self.d.sort()
        n = len(self.d)
        return (self.d[n//2] if (n & 1) else (self.d[n//2]+self.d[n//2-1]) /2)
        