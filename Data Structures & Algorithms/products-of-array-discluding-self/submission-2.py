class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        count = Counter(nums)
        zeros = count.get(0,0)
        if zeros > 1:
            return res
        mult = 1
        for num in nums:
            if num != 0:
                mult *= num    
        if zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = mult
            return res        
        if zeros == 0 :
            res = [mult//num for num in nums]
            return res               
