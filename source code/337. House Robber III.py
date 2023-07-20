from typing import List, Optional
import random
from utils import TreeNode

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.post_order(root)
        # print(dp)
        return max(dp)

    def post_order(self, node):
        if node.left or node.right:
            dp = [0, node.val]
            dp_left, dp_right = [0, 0], [0, 0]
            if node.left:
                dp_left = self.post_order(node.left)
            if node.right:
                dp_right = self.post_order(node.right)
            dp[0] = max(dp_left) + max(dp_right)
            dp[1] += dp_left[0] + dp_right[0]
        else:
            dp = [0, node.val]
        # print(node.val, dp)
        return dp

if __name__ == '__main__':
    sol = Solution()
    root_str = '[4,1,null,2,null,3]'
    root = TreeNode.build_by_str(root_str)
    print(sol.rob(root))
    root.draw()
