from utils import TreeNode
from typing import List, Optional
import sys

sys.setrecursionlimit(10000)

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        val = max(nums)
        root = TreeNode(val)
        root_idx = nums.index(val)
        left_nums = nums[:root_idx]
        right_nums = nums[root_idx+1:]

        if left_nums:
            root.left = self.constructMaximumBinaryTree(left_nums)
        if right_nums:
            root.right = self.constructMaximumBinaryTree(right_nums)
        return root

if __name__ == '__main__':
    sol = Solution()
    nums = [i for i in range(1001)]
    print(nums)
    root = sol.constructMaximumBinaryTree(nums)
    root.draw()
