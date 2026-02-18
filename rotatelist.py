# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Find length
        count = 1
        temp = head
        while temp.next:
            temp = temp.next
            count += 1
        
        # Step 2: Make circular
        temp.next = head
        
        # Step 3: Reduce k
        k = k % count
        if k == 0:
            temp.next = None
            return head
        
        # Step 4: Find new tail
        steps = count - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
        
        # Step 5: Break circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
