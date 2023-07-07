from utils import TreeNode, drawtree
from typing import List, Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root

    def invert(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        if node.left:
            self.invert(node.left)
        if node.right:
            self.invert(node.right)

if __name__ == '__main__':
    sol = Solution()
    tree_str = '[]'
    root = TreeNode.build_by_str(tree_str)
    new_root = sol.invertTree(root)
    new_root.draw()