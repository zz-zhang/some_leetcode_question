from utils import TreeNode
from typing import Optional
class Solution:
    '''
        node.val = 0 for not under monintored, 1 for under monintored, 2 for set a camera
    '''
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.root = root
        self.res = 0
        self.post_order(root)
        return self.res

    def post_order(self, node):
        if not node:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        if not node.left and not node.right:
            if node == self.root:
                node.val = 2
                self.res += 1
            return

        if node.left and node.right:
            if node.left.val == 0 or node.right.val == 0:
                node.val = 2
                node.left.val = 1
                node.right.val = 1
                self.res += 1
            if node.left.val == 2 or node.right.val == 2:
                node.val = 1
        elif node.left:
            if node.left.val == 0:
                node.val = 2
                node.left.val = 1
                self.res += 1
            if node.left.val == 2:
                node.val = 1
        else:
            if node.right.val == 0:
                node.val = 2
                node.right.val = 1
                self.res += 1
            if node.right.val == 2:
                node.val = 1
        if node == self.root and node.val == 0:
            node.val = 2
            self.res += 1
        




if __name__ == '__main__':
    sol = Solution()
    root_str = '[0,null,0,null,0,null,0]'
    root = TreeNode.build_by_str(root_str)
    print(sol.minCameraCover(root))
    root.draw()