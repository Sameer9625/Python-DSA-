# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Definition for singly-linked list.

        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        curr = slow
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Now 'prev' is the head of reversed second half
        
        # Step 3: Compare first half and reversed second half
        first = head
        second = prev
        
        while second:   # only need to check second half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
