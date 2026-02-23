class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        start1 = end1 = None   # odd list
        start2 = end2 = None   # even list

        count = 1

        while head:
            temp = head
            head = head.next
            temp.next = None   # detach node

            if count % 2:  # odd index
                if start1 is None:
                    start1 = end1 = temp
                else:
                    end1.next = temp
                    end1 = temp
            else:  # even index
                if start2 is None:
                    start2 = end2 = temp
                else:
                    end2.next = temp
                    end2 = temp

            count += 1

        # join odd and even lists
        end1.next = start2

        return start1

        # if not head or not head.next:
        #     return head

        # odd = head
        # even = head.next
        # even_head = even

        # while even and even.next:
        #     # Connect odd nodes
        #     odd.next = even.next
        #     odd = odd.next

        #     # Connect even nodes
        #     even.next = odd.next
        #     even = even.next

        # # Attach even list after odd list
        # odd.next = even_head

        # return head


        # if not head or not head.next:
        #     return head

        # odd = head
        # even = head.next
        # even_head = even

        # while even and even.next:
        #     odd.next = even.next
        #     odd = odd.next

        #     even.next = odd.next
        #     even = even.next

        # odd.next = even_head

        # return head

    