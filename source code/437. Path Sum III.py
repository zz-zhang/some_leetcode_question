from utils import TreeNode
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # self.recoder = []
        res = self.dfs(root, targetSum)
        # print(self.recoder)
        return res

    def dfs(self, node, target, path=[]):
        if not node:
            return 0

        res = 0
        path = path + [node.val]
        for start in range(len(path)):
            # start = len(path) - start
            if sum(path[start:]) == target:
                res += 1
                # self.recoder.append(path[start:])

        res += self.dfs(node.left, target, path)
        res += self.dfs(node.right, target, path)
        return res


if __name__ == '__main__':
    sol = Solution()
    root_str = '[10,5,-3,3,2,null,11,3,-2,null,1,null,null,-3]'
    targetSum = 8
    root = TreeNode.build_by_str(root_str)
    print(sol.pathSum(root, targetSum))
    root.draw()
