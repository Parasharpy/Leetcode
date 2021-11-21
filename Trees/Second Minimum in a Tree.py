#Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node.
#If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
#More formally, the property root.val = min(root.left.val, root.right.val) always holds.
#Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
#If no such second minimum value exists, output -1 instead.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        mini = root.val
        self.ans = float('inf')
        
        def second(node):
            if node:
                if mini < node.val < self.ans:
                    self.ans = node.val
                elif node.val == mini:
                    second(node.left)
                    second(node.right)
        second(root)
        if self.ans == float('inf'):
            return -1
        else:
            return self.ans
