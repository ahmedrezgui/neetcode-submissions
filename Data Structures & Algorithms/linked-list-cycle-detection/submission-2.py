# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = -1
        slow = fast = head
        while fast != None:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
            if slow == fast:
                return True
        return False
