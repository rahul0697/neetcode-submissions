# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        result = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:

            node, level = queue.popleft()
            result[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        res = []
        for key in result:
            values = result[key]
            res.append(values[len(values)-1])
        return res
            