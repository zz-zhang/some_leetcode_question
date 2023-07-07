from utils import TreeNode
from typing import List, Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val:
            if self.is_match(root, subRoot):
                return True
        
        res_l = self.isSubtree(root.left, subRoot)
        res_r = self.isSubtree(root.right, subRoot)
        return res_l or res_r

    def is_match(self, root, subRoot):
        pre_r, in_r = self.traversal(root, [], [])
        pre_s, in_s = self.traversal(subRoot, [], [])

        # print(pre_r, pre_s)
        # print(in_r, in_s)
        
        if len(pre_r) != len(pre_s):
            return False
        for v1, v2 in zip(pre_r, pre_s):
            if v1 != v2:
                return False

        if len(in_r) != len(in_s):
            return False
        for v1, v2 in zip(in_r, in_s):
            if v1 != v2:
                return False
        return True

    def traversal(self, node, pre_order=[], in_order=[]):
        if node is None:
            return pre_order, in_order
        pre_order.append(node.val)
        self.traversal(node.left, pre_order, in_order)
        in_order.append(node.val)
        self.traversal(node.right, pre_order, in_order)
        return pre_order, in_order


if __name__ == '__main__':
    sol = Solution()
    root_str = '[3,4,5,1,2,null,null,null,null,0]'
    subRoot_str = '[4,1,2]'
    root = TreeNode.build_by_str(root_str)
    subRoot = TreeNode.build_by_str(subRoot_str)
    print(sol.isSubtree(root, subRoot))
