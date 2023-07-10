from utils import TreeNode
from typing import List, Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        self.res = []
        self.dfs(root, targetSum, [])
        return self.res

    def dfs(self, node, left_sum, path):
        if not(node.left or node.right):
            if node.val == left_sum:
                # print(node.val)
                self.res.append(path+[node.val])
                return
            else:
                return

        if node.left:
            self.dfs(node.left, left_sum - node.val, path+[node.val])

        if node.right:
            self.dfs(node.right, left_sum - node.val, path+[node.val])


if __name__ == '__main__':
    sol = Solution()
    root_str = '[5,4,8,11,null,13,4,7,2,null,null,5,1]'
    targetSum = 22
    root = TreeNode.build_by_str(root_str)
    print(sol.PathSum(root, targetSum))
