# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        while len(lists)>1:
            k = 0
            mergedLists = []
            while k<len(lists) and k+1<len(lists):
                res = self.mergePair(lists[k], lists[k+1])
                mergedLists.append(res)
                k=k+2
            if k+1 == len(lists):
                mergedLists.append(lists[k])
            lists = mergedLists
        
        return lists[0]




    def mergePair(self,l1, l2):
        res = tmp = ListNode()
        while l1 and l2:
            if l1.val<l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if not l1:
            tmp.next = l2
        else:
            tmp.next = l1
        return res.next