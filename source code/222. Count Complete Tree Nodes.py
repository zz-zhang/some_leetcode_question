from utils import TreeNode
from typing import List, Optional

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        route = self.find_last_leaf(root, [])
        # print(route)

        res = (2 ** (len(route))) - 1
        # print(res)
        last_num = 1
        for depth, r in enumerate(route[::-1]):
            last_num += r * (2 ** depth)
        res = res + last_num
        return res

    def find_last_leaf(self, node, route):
        if not(node.left or node.right):
            return route
        
        found_route_r = None
        if node.right:
            found_route_r = self.find_last_leaf(node.right, route + [1])
        
        found_route_l = self.find_last_leaf(node.left, route + [0])
        
        if not found_route_r:
            return found_route_l
        elif len(found_route_l) > len(found_route_r):
            return found_route_l
        else:
            return found_route_r



if __name__ == '__main__':
    sol = Solution()
    root_str = '[1,2,3,4,5,6,7,8,9,120]'
    root = TreeNode.build_by_str(root_str)
    print(sol.countNodes(root))
