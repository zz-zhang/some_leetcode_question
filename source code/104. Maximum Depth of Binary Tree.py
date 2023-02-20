from typing import *
from utils import TreeNode, build_tree, drawtree
import random

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.dfs(root, 1)

    def dfs(self, node, depth):
        depth_left, depth_right = depth, depth
        if node.left is not None:
            depth_left = self.dfs(node.left, depth+1)
        if node.right is not None:
            depth_right = self.dfs(node.right, depth+1)
        # print(node.val, depth_left, depth_right)
        return max(depth_left, depth_right)

if __name__ == '__main__':
    sol = Solution()
    inp_lst = [str(random.randint(-100, 100)) for _ in range(2000)]
    inp = '[' + ','.join(inp_lst) + ']'
    # inp = '[3,9,20,null,null,15,7]'
    root = TreeNode.build_by_str(inp)
    # root.draw()
    print(sol.maxDepth(root))
