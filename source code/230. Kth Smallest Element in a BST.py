from typing import Optional
from utils import TreeNode, build_tree

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        _, res, _ = self.travsal(root, k)
        return res

    def travsal(self, node, k, num=-1):
        if node.left is not None:
            finish, res, num = self.travsal(node.left, k, num)
            if finish:
                return finish, res, num
        if num == -1:
            num = 0
        num += 1
        print(num, node.val)
        if num == k:
            return True, node.val, num
        
        if node.right is not None:
            finish, res, num = self.travsal(node.right, k, num)
            if finish:
                return finish, res, num
        return False, None, num

if __name__ == '__main__':
    sol = Solution()
    root = build_tree('[5,3,6,2,4,null,null,1]')
    k = 6
    print(sol.kthSmallest(root, k))