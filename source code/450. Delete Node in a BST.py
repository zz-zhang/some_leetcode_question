from utils import TreeNode
from typing import List, Optional

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        deleted, parent = self.get_deleted_node(root, key, None)
        if not deleted:
            return root
        new_root = self.rebuild(parent, deleted, root)
        return new_root

    def get_deleted_node(self, node, key, parent=None):
        if node.val == key:
            return (node, parent)
        if node.left and key <= node.val:
            return self.get_deleted_node(node.left, key, node)
        if node.right and key >= node.val:
            return self.get_deleted_node(node.right, key, node)
        return (None, None)

    def rebuild(self, parent, deleted, root):
        if not parent:
            if deleted.left and deleted.right:
                root = deleted.right
                min_leaf = self.get_min_leaf(root)
                min_leaf.left = deleted.left
                return root
            elif deleted.left:
                return deleted.left
            elif deleted.right:
                return deleted.right
            else:
                return None
        else:
            if deleted.left and deleted.right:
                if parent.left and parent.left.val == deleted.val:
                    parent.left = deleted.right
                elif parent.right and parent.right.val == deleted.val:
                    parent.right = deleted.right
                min_leaf = self.get_min_leaf(deleted.right)
                min_leaf.left = deleted.left
                return root

            elif deleted.left:
                if parent.left and parent.left.val == deleted.val:
                    parent.left = deleted.left
                elif parent.right and parent.right.val == deleted.val:
                    parent.right = deleted.left
                return root
            elif deleted.right:
                if parent.left and parent.left.val == deleted.val:
                    parent.left = deleted.right
                elif parent.right and parent.right.val == deleted.val:
                    parent.right = deleted.right
                return root
            else:
                if parent.left and parent.left.val == deleted.val:
                    parent.left = None
                elif parent.right and parent.right.val == deleted.val:
                    parent.right = None
                return root


    def get_min_leaf(self, node):
        if not node.left:
            return node
        else:
            return self.get_min_leaf(node.left)

            

if __name__ == '__main__':
    sol = Solution()
    root_str = '[]'
    root = TreeNode.build_by_str(root_str)
    key = 0
    res = sol.deleteNode(root, key)
    res.draw()