# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.res=True
        def iterate(p, q):
            
            if p is None and q is None:
                return True
            if p is None or q is None:   # one is None, other isn't
                return False
            if p.val != q.val:
                return False

            return iterate(p.left, q.left) and iterate(p.right, q.right)

        return iterate(p,q)
