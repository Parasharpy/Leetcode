#Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same
#tree, construct and return the binary tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(inorder)-1
        self.postindex = len(postorder)-1
        dictt = {}
        for i in range(len(inorder)):
            dictt[inorder[i]] = i
        def construct(inorder,postorder,start,end):
            if start > end:
                return None
            root = TreeNode(postorder[self.postindex])
            self.postindex -= 1
            
            inindex = dictt[root.val]
            
            root.right = construct(inorder,postorder,inindex+1,end)
            root.left = construct(inorder,postorder,start,inindex-1)
            
            return root
        return construct(inorder,postorder,start,end)
