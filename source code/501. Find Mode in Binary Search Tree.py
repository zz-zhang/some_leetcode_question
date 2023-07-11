from utils import TreeNode
from typing import List, Optional

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.max_num = -1
        self.last = None
        self.res = []
        self.traversal(root, 0)
        return self.res

    def traversal(self, node, counter):
        if node.left:
            counter = self.traversal(node.left, counter)
        # breakpoint()
        if not self.last:
            counter = 1
        elif node.val != self.last.val:
            counter = 1
        else:
            counter += 1
        if counter == self.max_num:
            self.res.append(node.val)
        elif counter > self.max_num:
            self.res = [node.val]
            self.max_num = counter
        # print(self.res)
        # breakpoint()
        self.last = node
        if node.right:
            counter = self.traversal(node.right, counter)

        return counter
            

if __name__ == '__main__':
    sol = Solution()
    root_str = '[1,null,2,2,2,null,null,null,3,3,3]'
    root = TreeNode.build_by_str(root_str)
    res = sol.findMode(root)
    print(res)