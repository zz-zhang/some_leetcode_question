from utils import TreeNode
from typing import List, Optional
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traversal(root)
        return self.res

    def traversal(self, node):
        if node is None:
            return
        self.traversal(node.left)
        self.traversal(node.right)
        self.res.append(node.val)

if __name__ == '__main__':
    sol = Solution()
    tree_str = '[1,null,2,3]'
    root = TreeNode.build_by_str(tree_str)
    print(sol.postorderTraversal(root))