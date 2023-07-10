from utils import TreeNode
from typing import List, Optional

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        self.dfs(root, '')
        self.res = [s[2:] for s in self.res]
        return self.res

    def dfs(self, node, path):
        new_path = f'{path}->{node.val}'
        if not (node.left or node.right):
            self.res.append(new_path)
            return
        
        if node.left:
            self.dfs(node.left, new_path)
        if node.right:
            self.dfs(node.right, new_path)



if __name__ == '__main__':
    sol = Solution()
    root_str = '[1,2,2,3,3,null,null,4,4]'
    root = TreeNode.build_by_str(root_str)
    print(sol.binaryTreePaths(root))
