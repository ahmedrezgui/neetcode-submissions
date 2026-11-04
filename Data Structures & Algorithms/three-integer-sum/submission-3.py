class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums= sorted(nums)
        for i, n in enumerate(nums):
            target = -n
            j, k= i+1, len(nums)-1 
            while (j<k):
                if (nums[j]+nums[k]<target):
                    j+=1
                elif (nums[j]+nums[k]>target):
                    k-=1
                else:
                    if [n,nums[j],nums[k]] not in res:                
                        res.append([n,nums[j],nums[k]])

                    j+=1
                    k-=1    
                
                           
                    
        return res            

