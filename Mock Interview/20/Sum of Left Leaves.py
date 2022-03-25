from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, node, is_left=False):
        if node.left is None and node.right is None:
            if is_left:
                # print(node.val, node.val)
                return node.val
            else:
                # print(node.val, 0)
                return 0
        res = 0
        if node.left is not None:
            res = self.dfs(node.left, True)
        if node.right is not None:
            res += self.dfs(node.right)
        # print(node.val, res)
        return res

if __name__ == '__main__':
    sol = Solution()
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.left.left = TreeNode(4)
    head.right = TreeNode(3)
    head.right.right = TreeNode(5)
    res = sol.sumOfLeftLeaves(head)
    print(res)