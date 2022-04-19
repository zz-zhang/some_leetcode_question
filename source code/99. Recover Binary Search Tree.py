from typing import Optional
from utils import build_tree, TreeNode, drawtree


class Solution:

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        recoder = []
        self.in_order_read(root, recoder)
        # print(recoder)
        recoder = sorted(recoder)
        # print(recoder)
        self.in_order_write(root, recoder)

        # recoder = []
        # self.in_order_read(root, recoder)
        # print(recoder)

    def in_order_read(self, node, recoder=[]):
        if node.left is not None:
            self.in_order_read(node.left, recoder)
        recoder.append(node.val)
        if node.right is not None:
            self.in_order_read(node.right, recoder)

    def in_order_write(self, node, recoder):
        if node.left is not None:
            self.in_order_write(node.left, recoder)
        # print(node.val, recoder)
        node.val = recoder[0]
        recoder.pop(0)
        if node.right is not None:
            self.in_order_write(node.right, recoder)


if __name__ == '__main__':
    sol = Solution()
    root = build_tree('[3,1,4,null,null,2]')
    sol.recoverTree(root)
    drawtree(root)
