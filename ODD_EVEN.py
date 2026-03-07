# if head is None or head.next is None:
#     return head

# values = []

# temp = head
# while temp:
#     values.append(temp.val)
#     temp = temp.next.next

# temp = head.next
# while temp:
#     values.append(temp.val)
#     temp = temp.next.next

# temp = head
# index = 0

# while temp:
#     temp.val = values[index]
#     index += 1
#     temp = temp.next

# return head

# #OPtimal approach
# if head is None or head.next is None:
#     return head

# odd = head
# even = head.next
# even_head = even

# while even is not None and even.next is not None:
#     odd.next = odd.next.next
#     odd = odd.next

#     even.next = even.next.next
#     even = even.next

# odd.next = even_head
# return head