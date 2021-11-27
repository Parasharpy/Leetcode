#Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque([])
        q.append(root)
        max_arr = []
        max_arr.append(root.val)
        while q:
            count = len(q)
            maxi = -(2**(31))
            while count > 0:
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                    maxi = max(maxi,node.left.val)
                if node.right is not None:
                    q.append(node.right)
                    maxi = max(maxi,node.right.val)
                count -= 1
            max_arr.append(maxi)
        max_arr.pop()
        return max_arr
