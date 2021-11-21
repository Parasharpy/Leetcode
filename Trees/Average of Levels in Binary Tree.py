#Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
#Answers within 10-5 of the actual answer will be accepted.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        q = deque([])
        q.append(root)
        arr = []
        
        while q:
            count = len(q)
            sums = 0
            n = count
            while count > 0:
                node = q.popleft()
                sums += node.val
                
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                count -= 1
            arr.append((sums)/n)
        return arr
