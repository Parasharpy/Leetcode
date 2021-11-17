#Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
#i.e., from left to right, then right to left for the next level and alternate between.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([])
        stack = []
        q.append(root)
        reverse = False
        ans = []
        while q:
            subans = []
            count = len(q)
            while count > 0:
                node = q.popleft()
                if reverse == False:
                    subans.append(node.val)
                else:
                    stack.append(node.val)
                
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                count -= 1
            if reverse == True:
                while stack:
                    subans.append(stack.pop())
                reverse = False
            else:
                 reverse = True
            ans.append(subans)
        return ans
