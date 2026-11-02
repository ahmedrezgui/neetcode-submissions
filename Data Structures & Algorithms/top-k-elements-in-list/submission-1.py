class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n]=1+count.get(n, 0)
        for n, cnt in count.items():
            freq[cnt].append(n)
        
        results= []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                results.append(j)
                if len(results)==k:
                    return results
                
