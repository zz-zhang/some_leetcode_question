# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    result = []
    def inorder_travel(self, root):
        if root.left is not None:
            self.inorder_travel(root.left)
        self.result.append(root.val)
        if root.right is not None:
            self.inorder_travel(root.right)


    def inorderTraversal(self, root):
        self.result = []
        if root is not None:
            self.inorder_travel(root)
        return self.result

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(sol.inorderTraversal(root))