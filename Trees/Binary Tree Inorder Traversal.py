# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#**************** RECURSIVE ****************

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        curr = root
        def inord(curr):
            if curr:
                inord(curr.left)
                arr.append(curr.val)
                inord(curr.right)
        inord(curr)
        return arr
      
#**************** ITERATIVE *****************

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack = []
        arr = []
        
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
                
            elif len(stack) > 0:
                curr = stack.pop()
                arr.append(curr.val)
                curr = curr.right
            
            else:
                break
                
        return arr
