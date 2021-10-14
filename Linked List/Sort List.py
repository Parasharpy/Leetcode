#This code uses merge sort to sort the linked list, time-complexity is O(nlogn) and space reqd. is O(logn), where n is total number of nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        actual_node = head
        def mergesort(actual_node):
            if actual_node is None or actual_node.next is None:
                return actual_node
            mid_node = getmid(actual_node)
            left_half = mergesort(actual_node)
            right_half = mergesort(mid_node)
            return conquer(left_half,right_half)
    
        def conquer(left_half,right_half): #merge phase
            dummy = ListNode(val = -(10**5), next = left_half)
            pointer = dummy
            while left_half is not None and right_half is not None:
                if left_half.val < right_half.val:
                    pointer.next = left_half
                    left_half = left_half.next
                else:
                    pointer.next = right_half
                    right_half = right_half.next
                pointer = pointer.next
            if left_half is not None:
                pointer.next = left_half
            else:
                pointer.next = right_half
            return dummy.next
        def getmid(node):
            fast_pointer = node
            slow_pointer = node
            while fast_pointer.next is not None and fast_pointer.next.next is not None:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next
            mid = slow_pointer.next
            slow_pointer.next = None #we are contracting the list for next call (most important step)
            return mid
        return mergesort(actual_node)
