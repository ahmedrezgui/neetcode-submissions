class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for n in nums:
            prev = n-1
            if prev not in hashset:
                length = 1
                while (n+length) in hashset:
                    length+=1
                longest = max(longest, length)
        return longest
            
