from utils import TreeNode
from typing import List, Optional

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        self.insert(root, val)
        return root

    def insert(self, node, val):
        if not node.left and val <= node.val:
            node.left = TreeNode(val)
            return
        if not node.right and val >= node.val:
            node.right = TreeNode(val)
            return

        if val <= node.val:
            self.insert(node.left, val)
            return
        if val >= node.val:
            self.insert(node.right, val)
            return

            

if __name__ == '__main__':
    sol = Solution()
    root_str = '[4,2,7,1,3,null,null,null,null,null,null]'
    root = TreeNode.build_by_str(root_str)
    val = 5
    res = sol.insertIntoBST(root, val)
    res.draw()