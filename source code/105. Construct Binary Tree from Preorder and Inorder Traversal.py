import enum
from typing import *
from utils import TreeNode, build_tree, drawtree
import random

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        # print(preorder, inorder)
        # print()
        root_val = preorder[0]
        root = TreeNode(root_val)

        root_idx_inorder = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:root_idx_inorder + 1], inorder[:root_idx_inorder])
        root.right = self.buildTree(preorder[root_idx_inorder + 1:], inorder[root_idx_inorder + 1:])
        return root


if __name__ == '__main__':
    sol = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    root = sol.buildTree(preorder, inorder)
    root.draw()