'''
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        q = [root]
        while len(q) > 0:
            node = q[0]
            q.pop(0)



if __name__ == '__main__':
    sol = Solution()
    head = TreeNode(3)
    head.left = TreeNode(0)
    head.right = TreeNode(0)
    print(sol.distributeCoins(head))
