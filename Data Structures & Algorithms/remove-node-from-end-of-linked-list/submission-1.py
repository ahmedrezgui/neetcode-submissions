# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp =head
        l = 1
        while tmp.next:
            tmp = tmp.next
            l = l+1  
        r = l - n
        if r ==0:
            return head.next
        i=1
        tmp = head
        while i<r :
            tmp = tmp.next
            i = i + 1
        tmp.next = tmp.next.next

        return head