from utils import TreeNode
from typing import List, Optional

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
            if node.children is not None:
                q = q + [(child, depth + 1) for child in node.children]
            q.pop(0)

        ordered_res = []
        for depth in sorted(res.keys()):
            ordered_res.append(res[depth])
        return ordered_res
