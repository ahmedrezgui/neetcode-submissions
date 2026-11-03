class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m= 0
        l,r = 0, len(heights)-1
        while l<r :
            a= (r-l)*min(heights[l],heights[r])
            m = max(m,a)
            if heights[l]>heights[r]:
                r = r-1
            else:
                l= l+1

        return m