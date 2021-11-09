#Given the root of a binary tree, return the sum of all left leaves.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        arr = [0]
        if root.left is None and root.right is None:
            return 0
        curr = root
        def left(curr,arr):
            if curr.left is None and curr.right is None:
                arr[0] += curr.val
            else:
                if curr.left is not None:
                    left(curr.left,arr)
                if curr.right is not None:
                    if curr.right.left is not None or curr.right.right is not None:
                        left(curr.right,arr)
        left(curr,arr)
        return arr[0]
