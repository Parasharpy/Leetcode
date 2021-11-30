#Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both 
#p and q as descendants (where we allow a node to be a descendant of itself).”


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def path_f(root,path,node):
            if root is None:
                return False
            path.append(root)
            if root == node:
                return True
            if path_f(root.left,path,node) or path_f(root.right,path,node):
                return True
            path.pop()
            return False
        
        def lca(root,p,q):
            path1 = []
            path2 = []
            path_f(root,path1,p)
            path_f(root,path2,q)
            i = 0
            while i < len(path1) and i < len(path2):
                if path1[i] != path2[i]:
                    break
                i += 1
            return path1[i-1]
        return lca(root,p,q)
