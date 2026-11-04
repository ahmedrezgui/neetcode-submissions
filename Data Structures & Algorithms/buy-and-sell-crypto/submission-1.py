class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        res = 0
         
        while( l < r and r<len(prices)):
            if (prices[l]>prices[r]):
                if r == len(prices)-1:
                    return res
                else:
                    l+=1
                    r = l
            else:
                res = max(res, prices[r]-prices[l])
            r+=1    
        return res