
from utils import TreeNode
from typing import List, Optional

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = 100001
        self.lst = []
        self.in_order(root)
        print(self.lst)
        for n1, n2 in zip(self.lst[:-1], self.lst[1:]):
            res = min(res, n2-n1)
        return res

    def in_order(self, node):
        if not node:
            return
        
        self.in_order(node.left)
        self.lst.append(node.val)
        self.in_order(node.right)


if __name__ == '__main__':
    sol = Solution()
    root_str = '[1,0,48,null,null,12,49]'
    root = TreeNode.build_by_str(root_str)
    res = sol.getMinimumDifference(root)
    print(res)