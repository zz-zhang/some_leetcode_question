# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree_to_list(self, root: TreeNode):
        queue = [root]
        l = []
        while len(queue) > 0:
            head = queue[0]
            queue.pop(0)

            if head is None:
                l.append(-0x7fffffff)
            else:
                l.append(head.val)
                queue.append(head.left)
                queue.append(head.right)
        return l

    def maxPathSum(self, root: TreeNode) -> int:
        node_list = self.tree_to_list(root)
        dp = [item for item in node_list]

        def left(index):
            return index * 2 + 1
        def right(index):
            return index * 2 + 2
        for index in range(len(dp) - 1, -1, -1):
            l = left(index)
            r = right(index)
            temp = dp[index]
            if l < len(dp):
                temp = max(temp, dp[index] + dp[l], dp[l])
            if r < len(dp):
                temp = max(temp, dp[index] + dp[r], dp[r])
            if l < len(dp) and r < len(dp):
                temp = max(temp, dp[index] + dp[r] + dp[l])
            dp[index] = temp
            # print(index, dp)
        return dp[0]

def list_to_tree(l, index):
    if index >= len(l):
        return None
    if l[index] is not None:
        root = TreeNode(l[index])
        root.left = list_to_tree(l, index * 2 + 1)
        root.right = list_to_tree(l, index * 2 + 2)
        return root
    else:
        return None

if __name__ == '__main__':
    sol = Solution()
    l = [1,None,2,None,3,None,4,None,5]
    # print(l)
    root = list_to_tree(l, 0)
    print(sol.maxPathSum(root))
