# from linked_list import LinkedList
# from linked_list_reverse import reverse_linked_list
#
#
# def palindrome(head):
#     #移动fast到链表末尾。此时slow在链表中间
#     fast = head
#     slow = head
#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next
#     #reverse链表后半部分
#     reverse_linked_list(slow)
#     #比较链表前半部分和reverse后的后半部分
#     #情况1，偶数个node
#     if fast is None:
#         if linkedList_equality(slow, head):
#             return True
#         else:
#             return False
#     # 情况2，奇数个node
#     else:
#         if linkedList_equality(slow.next, head):
#             return True
#             palindrome     else:
#
#
#         return False
#
# def linkedList_equality(head1, head2):
#     while head1 and head2:
#         if head1.data != head2.data:
#             return False
#         head1 = head1.next
#         head2 = head2.next
#     if head1 is None and head2 is None:
#         return True
#     else:
#         return False
#
#
# # Driver code
# def main():
#
#     input_linked_list = LinkedList()
#     input_linked_list.create_linked_list([1, 2, 3, 2, 1])
#     palindrome(input_linked_list.head)
#
#
#
# if __name__ == "__main__":
#     main()