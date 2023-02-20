# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *
from utils import TreeNode, build_tree, drawtree
import random

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = [(root, 0)]
        sub_res = []
        last_depth = 0
        while len(q) > 0:
            node, depth = q[0]
            if depth != last_depth:
                last_depth = depth
                res.append(sub_res)
                sub_res = []
            sub_res.append(node.val)
            if node.left is not None:
                q.append((node.left, depth + 1))
            if node.right is not None:
                q.append((node.right, depth + 1))
            q = q[1:]
        if len(sub_res) > 0:
            res.append(sub_res)
        return res

if __name__ == '__main__':
    sol = Solution()
    inp_lst = [str(random.randint(-1000, 1000)) for _ in range(2000)]
    inp = '[' + ','.join(inp_lst) + ']'
    # inp = '[1, 2, null, 3, null, 4, null, 5]'
    root = TreeNode.build_by_str(inp)
    # root.draw()
    print(sol.levelOrder(root))