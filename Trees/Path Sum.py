#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path
#equals targetSum. A leaf is a node with no children.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        sums = 0
        curr = root
        def path(curr,sums):
            if curr is None:
                return False
            sums += curr.val
            
            if curr.left is None and curr.right is None:
                if sums == targetSum:
                    return True
            else:
                left = path(curr.left,sums)
                right = path(curr.right,sums)
                if left == True or right == True:
                    return True
                else:
                    return False
        return path(curr,sums)
