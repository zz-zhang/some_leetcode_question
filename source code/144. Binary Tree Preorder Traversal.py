from utils import TreeNode
from typing import List, Optional
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traversal(root)
        return self.res

    def traversal(self, node):
        if node is None:
            return
        self.res.append(node.val)
        self.traversal(node.left)
        self.traversal(node.right)

if __name__ == '__main__':
    sol = Solution()
    tree_str = '[1,2,3,4]'
    root = TreeNode.build_by_str(tree_str)
    print(sol.preorderTraversal(root))