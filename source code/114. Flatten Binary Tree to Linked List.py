from typing import *
from utils import TreeNode, build_tree, drawtree
import random

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.func(root)

    def _the_most_right(self, node):
        while node.right is not None:
            node = node.right
        return node

    def func(self, root):
        if root is not None:
            self.func(root.left)
            self.func(root.right)

            if root.left is not None and root.right is not None:
                left_leaf = self._the_most_right(root.left)
                left_leaf.right = root.right
                root.right = root.left
                root.left = None
            
            elif root.left is not None:
                root.right = root.left
                root.left = None





if __name__ == '__main__':
    sol = Solution()
    inp_lst = [str(random.randint(-100, 100)) for _ in range(2000)]
    inp = '[' + ','.join(inp_lst) + ']'
    inp = '[1,2,5,3,4,null,6]'
    root = TreeNode.build_by_str(inp)
    # root.draw()
    sol.flatten(root)
    root.draw()
