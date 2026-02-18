# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy   # pointer to node before duplicates
        
        while head:
            
            # If duplicate detected
            if head.next and head.val == head.next.val:
                
                # Skip all nodes with same value
                while head.next and head.val == head.next.val:
                    head = head.next
                
                # Connect prev to node after duplicates
                prev.next = head.next
            
            else:
                prev = prev.next
            
            head = head.next
        
        return dummy.next


        
