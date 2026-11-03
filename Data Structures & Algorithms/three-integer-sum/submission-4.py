class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i, n in enumerate(nums):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            j, k= i+1, len(nums)-1
            while j<k:
                if nums[j]+nums[k]<-n:
                    j=j+1
                elif nums[j]+nums[k]>-n:
                    k=k-1
                else:
                    results.append([n,nums[j], nums[k]])
                    j=j+1
                    k=k-1
                    while j<k and nums[j]==nums[j-1]:
                        j=j+1
                    while j<k and nums[k]==nums[k+1]:
                        k=k-1
                
        return results    


