#Given the head of a linked list, rotate the list to the right by k places.
#Input: head = [1,2,3,4,5], k = 2, Output: [4,5,1,2,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        curr_node = head
        count = 0
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next
        def rotation(node):
            actual_node = node
            prev = None
            store = None
            while actual_node is not None:
                if actual_node.next is None:
                    store = actual_node.val
                    prev.next = None
                    break
                else:
                    prev = actual_node
                    actual_node = actual_node.next
            new_node = ListNode(store)
            new_node.next = node
            node = new_node
            return node
        if k < count:
            while k != 0:
                head = rotation(head)
                k -= 1
            return head
        else:
            div = k % (count)
            while div != 0:
                head = rotation(head)
                div -= 1
            return head
