#Given the head of a singly linked list, return true if it is a palindrome.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow_pointer = head
        fast_pointer = head
        while fast_pointer.next is not None and fast_pointer.next.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        current_node = slow_pointer.next
        prev_node = None
        next_node = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        while prev_node is not None:
            if prev_node.val != head.val:
                return False
            prev_node = prev_node.next
            head = head.next
            
        return True
