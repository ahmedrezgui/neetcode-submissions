class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_set = set(nums)
        nums_list = list(list_set)
        if len(nums_list) != len(nums):
            return True
        else:
            return False        