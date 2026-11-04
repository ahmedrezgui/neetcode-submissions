class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l,r = 0,k
        while l<=len(nums)-1:
            if r>len(nums)-1:
                r=len(nums)-1
            while r>l:
                if nums[l] != nums[r]:
                    r= r-1
                else:
                    return True
            l= l+1
            r= l+k
        return False
            

            
