from utils import TreeNode
from typing import List, Optional

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = {}
        q = [(root, 0)]
        while len(q) > 0:
            node, depth = q[0]
            if depth not in res:
                res[depth] = [node.val]
            else:
                res[depth].append(node.val)
            if node.left is not None:
                q.append((node.left, depth + 1))
            if node.right is not None:
                q.append((node.right, depth + 1))
            q.pop(0)
        
        ordered_res = []
        for depth in sorted(res.keys(), reverse=True):
            ordered_res.append(res[depth])
        return ordered_res


if __name__ == '__main__':
    sol = Solution()
    tree_str = '[1]'
    root = TreeNode.build_by_str(tree_str)
    print(sol.levelOrderBottom(root))