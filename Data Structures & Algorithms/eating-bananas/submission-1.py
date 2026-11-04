class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        u = max(piles)
        l, r = 1, u
        k= 0
        while l<=r:
            m = (l + r) // 2
            th= 0
            for j in piles:
                th= th + math.ceil(j / m)
            if th<=h:
                k = m
                r = m - 1
            else:
                l= m+1

        return k
            