class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        currmin = prices[0]  # Start with the first day's price, not 0
        currmax = 0          # This tracks the maximum profit found so far
        i = 0
    
        while i < len(prices):
            if prices[i] < currmin:
                currmin = prices[i]  # Found a new lowest buy price
            elif prices[i] - currmin > currmax:
                currmax = prices[i] - currmin  # Found a better profit
            i += 1
            
        return currmax