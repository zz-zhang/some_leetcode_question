from utils import TreeNode
from typing import List, Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = {}
        q = [(root, 0)]
        while len(q) > 0:
            node, depth = q[0]
            if depth not in res:
                res[depth] = node.val
            else:
                res[depth] = node.val
            if node.left is not None:
                q.append((node.left, depth + 1))
            if node.right is not None:
                q.append((node.right, depth + 1))
            q.pop(0)
        
        ordered_res = []
        for depth in sorted(res.keys()):
            ordered_res.append(res[depth])
        return ordered_res

if __name__ == '__main__':
    sol = Solution()
    tree_str = '[1,null,3]'
    root = TreeNode.build_by_str(tree_str)
    print(sol.rightSideView(root))