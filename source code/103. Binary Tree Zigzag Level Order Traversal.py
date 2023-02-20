# The same to Q102, but reverse sub_res every 2 appending
from typing import *
from utils import TreeNode, build_tree, drawtree
import random

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = [(root, 0)]
        sub_res = []
        reverse = False
        last_depth = 0
        while len(q) > 0:
            node, depth = q[0]
            if depth != last_depth:
                last_depth = depth
                res.append(sub_res if not reverse else sub_res[::-1])
                sub_res = []
                reverse = not reverse
            sub_res.append(node.val)
            if node.left is not None:
                q.append((node.left, depth + 1))
            if node.right is not None:
                q.append((node.right, depth + 1))
            q = q[1:]
        if len(sub_res) > 0:
            res.append(sub_res if not reverse else sub_res[::-1])
        return res

if __name__ == '__main__':
    sol = Solution()
    # inp_lst = [str(random.randint(-1000, 1000)) for _ in range(2000)]
    # inp = '[' + ','.join(inp_lst) + ']'
    inp = '[3,9,20,null,null,15,7]'
    root = TreeNode.build_by_str(inp)
    # root.draw()
    print(sol.zigzagLevelOrder(root))