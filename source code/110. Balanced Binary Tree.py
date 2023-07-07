from utils import TreeNode
from typing import List, Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            True
        return self.max_depth(root, 1)[-1]

    def max_depth(self, node, depth):
        if not node:
            return depth - 1, False, True
        depth_l, return_flag, res = self.max_depth(node.left, depth + 1)
        # print('l', node.val, depth_l)
        if return_flag:
            return max(depth_l, depth), return_flag, res
        depth_r, return_flag, res = self.max_depth(node.right, depth + 1)
        # print('r', node.val, depth_r)
        if return_flag:
            return max(depth, depth_r), return_flag, res

        if abs(depth_l - depth_r) > 1:
            return max(depth_l, depth_r), True, False
        else:
            return max(depth_l, depth_r), False, True


if __name__ == '__main__':
    sol = Solution()
    root_str = '[1,2,2,3,3,null,null,4,4]'
    root = TreeNode.build_by_str(root_str)
    print(sol.isBalanced(root))
