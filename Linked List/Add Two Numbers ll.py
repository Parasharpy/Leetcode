#Given two non-empty linked lists representing two non-negative integers. Most significant digit comes first and each of their nodes contains a single digit.
#Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.



#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseL(node):
            current_ = node
            prev_node = None
            next_node = None
            while current_ is not None:
                next_node = current_.next
                current_.next = prev_node
                prev_node = current_
                current_ = next_node
            return prev_node
        l1 = reverseL(l1)
        l2 = reverseL(l2)
        current = ListNode(0)
        current_node = current
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                if (l2.val + carry) < 10:
                    current_node.next = ListNode(l2.val + carry)
                    carry = 0
                else:
                    current_node.next = ListNode((l2.val + carry)%10)
                    carry = 0
                    carry = carry + 1
                l2 = l2.next
            elif l2 is None:
                if (l1.val + carry) < 10:
                    current_node.next = ListNode(l1.val + carry)
                    carry = 0
                else:
                    current_node.next = ListNode((l1.val + carry)%10)
                    carry = 0
                    carry = carry + 1
                l1 = l1.next
            else:
                if (l1.val + l2.val + carry) < 10:
                    current_node.next = ListNode(l1.val + l2.val + carry)
                    carry = 0
                else:
                    current_node.next = ListNode((l1.val + l2.val + carry)%10)
                    carry = 0
                    carry = carry + 1
                l1 = l1.next
                l2 = l2.next
            current_node = current_node.next
        if carry == 1:
            current_node.next = ListNode(carry)
        return reverseL(current.next)
