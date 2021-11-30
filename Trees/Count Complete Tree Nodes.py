#Given the root of a complete binary tree, return the number of the nodes in the tree.
#According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left 
#as possible. It can have between 1 and 2h nodes inclusive at the last level h. Design an algorithm that runs in less than O(n) time complexity.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def count(root):
            left = right = 0
            curr = root
            while curr is not None:
                left += 1
                curr = curr.left
            curr = root
            while curr is not None:
                right += 1
                curr = curr.right
            if left == right:
                return (2**(left)) - 1
            else:
                return 1 + count(root.left) + count(root.right)
        return count(root)
      
 #this solution is O(logn * logn)
