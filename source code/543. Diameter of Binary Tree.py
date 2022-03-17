from utils import TreeNode, deserialize
from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)[1]

    def dfs(self, node, depth=0):
        if node.left is None and node.right is None:
            return depth, 0
        depth_left = depth
        depth_right = depth
        left_son_max_depth = 0
        right_son_max_depth = 0
        if node.left is not None:
            depth_left, left_son_max_depth = self.dfs(node.left, depth + 1)
        if node.right is not None:
            depth_right, right_son_max_depth = self.dfs(node.right, depth + 1)
        
        son_max_distance = max(left_son_max_depth, right_son_max_depth, depth_left + depth_right - 2 * depth)
        # print(node.val, depth, depth_left - depth, depth_right - depth, son_max_distance)
        return max(depth_left, depth_right), son_max_distance


if __name__ == '__main__':
    sol = Solution()
    root = deserialize('[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]')
    print(sol.diameterOfBinaryTree(root))