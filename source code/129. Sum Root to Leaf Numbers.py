from utils import TreeNode
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        self.dfs(root, 0, nums)
        return sum(nums)

    def dfs(self, node, temp, nums=[]):

        temp = temp * 10 + node.val
        if node.left or node.right:
            if node.left:
                self.dfs(node.left, temp, nums)
            if node.right:
                self.dfs(node.right, temp, nums)
        else:
            nums.append(temp)


if __name__ == '__main__':
    sol = Solution()
    root = '[1]'
    root = TreeNode.build_by_str(root)
    print(sol.sumNumbers(root))
