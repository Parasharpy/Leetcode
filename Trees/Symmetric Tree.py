#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([])
        q.append(root)
        
        while len(q) > 0:
            count = len(q)
            arr = []
            while count > 0:
                node = q.popleft()
                if node is None:
                    arr.append("None")
                else:
                    arr.append(node.val)
                if node is not None:
                    if node.left is not None and node.right is not None:
                        q.append(node.left)
                        q.append(node.right)
                    elif node.left is None and node.right is not None:
                        q.append(None)
                        q.append(node.right)
                    elif node.left is not None and node.right is None:
                        q.append(node.left)
                        q.append(None)
                    else:
                        q.append(None)
                        q.append(None)
                count -= 1
            start = 0
            end = len(arr) - 1
            while start < end:
                if arr[start] != arr[end]:
                    return False
                start += 1
                end -= 1
        return True
