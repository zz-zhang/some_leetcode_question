from utils import TreeNode
from typing import List, Optional

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = [(root, 1)]
        res = -1
        while len(q) > 0:
            node, depth = q[0]
            res = max(res, depth)
            if not (node.left or node.right):
                return res
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
            q.pop(0)
        

if __name__ == '__main__':
    sol = Solution()
    tree_str = '[2,null,3,null,4,null,5,null,6]'
    root = TreeNode.build_by_str(tree_str)
    print(sol.minDepth(root))