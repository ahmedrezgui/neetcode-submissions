# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node = None
        t_node= head
        while t_node.next:
            new = t_node.next
            t_node.next = node
            node = t_node
            t_node = new
        t_node.next = node
        return t_node