class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[]
        dict_nums = Counter(nums)
        for v,c in dict_nums.most_common(k):
            l.append(v)

        return l