from utils import TreeNode
from typing import List, Optional

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = [(root, 1)]
        cache = []
        max_depth = 1

        while len(q) > 0:
            node, depth = q[0]
            if depth == max_depth:
                cache.append(node)
            else:
                max_depth = depth
                cache = [node]

            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
            q = q[1:]
        return cache[0].val

if __name__ == '__main__':
    sol = Solution()
    root_str = '[1]'
    root = TreeNode.build_by_str(root_str)
    print(sol.findBottomLeftValue(root))
