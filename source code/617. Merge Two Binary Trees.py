'''
in-place solution
'''
from utils import TreeNode
from typing import List, Optional

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            root1.val += root2.val
        elif root2:
            root1 = root2
            return root1
        else:
            return root1

        if root1.left or root2.left:
            if root1.left:
                self.mergeTrees(root1.left, root2.left)
            else:
                root1.left = root2.left
        if root1.right or root2.right:
            if root1.right:
                self.mergeTrees(root1.right, root2.right)
            else:
                root1.right = root2.right

        return root1



if __name__ == '__main__':
    sol = Solution()
    root1_str = '[1]'
    root1 = TreeNode.build_by_str(root1_str)
    root2_str = '[1,2]'
    root2 = TreeNode.build_by_str(root2_str)
    res = sol.mergeTrees(root1, root2)
    res.draw()
