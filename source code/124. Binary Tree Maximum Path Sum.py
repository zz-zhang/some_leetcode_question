# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = -0x7fffffff
    def find_sum(self, root):
        if root is None:
            return 0
        dp_l = self.find_sum(root.left)
        dp_r = self.find_sum(root.right)
        max_dir = max(dp_l, dp_r)
        max_one_son = max(root.val + max_dir, root.val)
        max_two_son = max(root.val + dp_l + dp_r, max_one_son)
        self.res = max(self.res, max_two_son)
        return max_one_son


    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -0x7fffffff
        self.find_sum(root)
        return self.res

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print(sol.maxPathSum(root))
