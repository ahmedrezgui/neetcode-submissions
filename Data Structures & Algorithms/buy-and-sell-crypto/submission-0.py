class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        res = 0
         
        while( l < r and l<len(prices)-1):
            res = max(res, prices[r]-prices[l])
            if (prices[l]>prices[r] or r==len(prices)-1):
                l+=1
                r = l
            r+=1    
        return res