class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        prev = []
        for i, n in enumerate(nums):
            for j in range(i+1, len(nums)):
                add =n + nums[j]
                for k in range(j+1, len(nums)):
                    if add + nums[k]==0:
                        if sorted([n,nums[j],nums[k]]) not in res:
                            res.append(sorted([n,nums[j],nums[k]])) 
                    
        return res            

