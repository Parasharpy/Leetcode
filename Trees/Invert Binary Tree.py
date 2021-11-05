#Given the root of a binary tree, invert the tree, and return its root.



#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        if root.left is None and root.right is None:
            return root
        else:
            store = root.left
            root.left = root.right
            root.right = store
            if root.left is not None:
                self.invertTree(root.left)
            if root.right is not None:
                self.invertTree(root.right)
        return root
