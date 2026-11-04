class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = sorted(set(nums))    
        if len(k)==1:
            return 1    
  
        l = [num + 1 for num in k]
        seqs= []
        seq=1
        for i in range(len(k)-1):
            if l[i] == k[i+1]:
                seq += 1
            else:
                seqs.append(seq)
                seq = 1
        if i == len(k)-2:
            seqs.append(seq)        
        return max(seqs)        