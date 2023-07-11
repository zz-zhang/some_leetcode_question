from utils import TreeNode
from typing import List, Optional

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        return self.travseral(root, p.val, q.val)

        

    def travseral(self, node, p, q):
        # breakpoint()
        if p <= node.val <= q:
            return node
        if node.left and node.val == q and node.left.val == p:
            return node
        if node.right and node.val == p and node.right.val == q:
            return node

        if q <= node.val:
            return self.travseral(node.left, p, q)
        if p >= node.val:
            return self.travseral(node.right, p, q)
        
            

if __name__ == '__main__':
    sol = Solution()
    root_str = '[6,2,8,0,4,7,9,null,null,3,5]'
    root = TreeNode.build_by_str(root_str)
    p = TreeNode(3)
    q = TreeNode(4)
    res = sol.lowestCommonAncestor(root, p, q)
    res.draw()