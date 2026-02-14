class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        next_node = None  # renamed 'next' to avoid conflict with keyword

        while curr != None:
            next_node = curr.next   # store the next node
            curr.next = prev        # reverse the pointer
            prev = curr             # move prev forward
            curr = next_node        # move curr forward

        return prev  # prev is the new head