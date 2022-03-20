from typing import *
from utils import *
from random import randint

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        q = [root]
        while len(q) > 0:
            node = q[0]
            if self.dfs(node, head):
                return True
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            q = q[1:]
        return False

    def dfs(self, tree_node, list_node):
        if tree_node.val != list_node.val:
            return False
        if list_node.next is None:
            return True

        left_res, right_res = False, False
        if tree_node.left is not None:
            left_res = self.dfs(tree_node.left, list_node.next)
        if tree_node.right is not None:
            right_res = self.dfs(tree_node.right, list_node.next)
        return left_res or right_res


if __name__ == '__main__':
    sol = Solution()
    head = build_list([1,1,1])
    root = deserialize("1,1,1")
    print(sol.isSubPath(head, root))