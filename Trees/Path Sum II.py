#Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
#Each path should be returned as a list of the node values, not node references.
#A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        arr = []
        curr = root
        sub = []
        sums = 0
        def allpath(curr,sums,sub):
            if curr is None:
                return
            sums += curr.val
            if curr.left is None and curr.right is None:
                if sums == targetSum:
                    arr.append(sub + [curr.val])
                return
            else:
                if curr.left is not None:
                    allpath(curr.left,sums,sub + [curr.val])
                if curr.right is not None:
                    allpath(curr.right,sums,sub + [curr.val])
        allpath(curr,sums,sub)
        return arr
