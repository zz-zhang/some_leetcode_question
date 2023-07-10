from utils import TreeNode
from typing import List, Optional

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.dfs(root, targetSum)

    def dfs(self, node, left_sum):
        if not(node.left or node.right):
            if node.val == left_sum:
                # print(node.val)
                return True
            else:
                return False

        if node.left:
            if self.dfs(node.left, left_sum - node.val):
                return True

        if node.right:
            if self.dfs(node.right, left_sum - node.val):
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    root_str = '[1,2,3]'
    targetSum = 2
    root = TreeNode.build_by_str(root_str)
    print(sol.hasPathSum(root, targetSum))
