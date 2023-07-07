from utils import TreeNode
from typing import List, Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not (p and q):
            return False
        return self.compare(p, q)
        
    def compare(self, node1, node2):
        if not node1 and not node2:
            return True
        if not (node1 and node2):
            return False

        if node1.val != node2.val:
            return False
        if not self.compare(node1.left, node2.left):
            return False
        if not self.compare(node1.right, node2.right):
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    p_str = '[1,2, 1]'
    q_str = '[1,1,2]'
    p = TreeNode.build_by_str(p_str)
    q = TreeNode.build_by_str(q_str)
    print(sol.isSameTree(p, q))
