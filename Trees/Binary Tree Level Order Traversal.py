#Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([])
        q.append(root)
        result = []
        if root is None:
            return result
        while q:
            arr = []
            count = len(q)
            while count > 0:
                node = q.popleft()
                arr.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)  
                count -= 1
                
            result.append(arr)
            
        return result
