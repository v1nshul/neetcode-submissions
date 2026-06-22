class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0

        l= 0
        r = l+1

        while l < len(prices) and r < len(prices):
            curp = 0
            if prices[l] < prices[r]:
                curp = prices[r] - prices[l]
                maxp = max(curp,maxp)
            r+= 1
            if r > len(prices) -1:
                l += 1
                r = l + 1

        return maxp