from typing import Optional
from utils import TreeNode, build_tree, drawtree


class Solution:

    def trimBST(self, root: Optional[TreeNode], low: int,
                high: int) -> Optional[TreeNode]:
        prev_node = TreeNode(-1, right=root)
        self.travel(root, prev_node, 'r', low, high)
        return prev_node.right

    def travel(self, node, prev_node, parent_dir, low, high):
        if low <= node.val <= high:
            if node.left is not None:
                self.travel(node.left, node, 'l', low, high)
            if node.right is not None:
                self.travel(node.right, node, 'r', low, high)
        elif node.val < low:
            if parent_dir == 'l':
                prev_node.left = node.right
                if prev_node.left is not None:
                    self.travel(prev_node.left, prev_node, 'l', low, high)
            else:
                prev_node.right = node.right
                if prev_node.right is not None:
                    self.travel(prev_node.right, prev_node, 'r', low, high)

        else:
            if parent_dir == 'l':
                prev_node.left = node.left
                if prev_node.left is not None:
                    self.travel(prev_node.left, prev_node, 'l', low, high)

            else:
                prev_node.right = node.left
                if prev_node.right is not None:
                    self.travel(prev_node.right, prev_node, 'r', low, high)


if __name__ == '__main__':
    sol = Solution()
    root = build_tree('[3,0,4,null,2,null,null,1]')
    low = 1
    high = 3
    root = sol.trimBST(root, low, high)
    drawtree(root)
