from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        
        less = less_dummy
        greater = greater_dummy
        
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            
            head = head.next
        
        # Important: end greater list
        greater.next = None
        
        # Connect both lists
        less.next = greater_dummy.next
        
        return less_dummy.next