class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1] * len(nums)
        prefix = [1] * len(nums)
        pre, suff = 1, 1
        
        for i,n in enumerate(nums):
            prefix[i] = pre
            pre = pre*n
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = suff
            suff = suff * nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append( prefix[i]* suffix[i])
        return res
            
            