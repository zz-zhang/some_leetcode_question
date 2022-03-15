from random import randint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def list_to_tree(self, numbers):
        if len(numbers) == 0:
            return None
        root = TreeNode()
        currect = root
        treelist = []
        for idx, val in enumerate(numbers):
            if val is not None:
                treelist.append(TreeNode(val))
            else:
                treelist.append(None)

        # breakpoint()
        for idx, curr in enumerate(treelist):
            if curr is not None:
                if idx * 2 + 1 < len(treelist) and treelist[idx * 2 + 1] is not None:
                    curr.left = treelist[idx * 2 + 1]
                if idx * 2 + 2 < len(treelist) and treelist[idx * 2 + 2] is not None:
                    curr.right = treelist[idx * 2 + 2]
        # breakpoint()
        return treelist[0]

    def travel(self):
        print(self.val, end=' ')
        if self.left is not None:
            self.left.travel()
        else:
            print('None', end=' ')
        if self.right is not None:
            self.right.travel()
        else:
            print('None', end=' ')

class Solution:
    def largestValues(self, root):
        if root is None:
            return []
        res = []
        q = [(root, 0)]
        temp_max = - 2 ** 31 - 1
        current_depth = 0
        while len(q) > 0:
            node, depth = q[0]
            if depth == current_depth:
                temp_max = max(temp_max, node.val)
            else:
                res.append(temp_max)
                current_depth = depth
                temp_max = node.val
            
            if node.left is not None:
                q.append((node.left, depth + 1))
            if node.right is not None:
                q.append((node.right, depth + 1))
            q = q[1:]
        res.append(temp_max)
        return res

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode().list_to_tree([randint(-2 ** 31, 2 ** 31 - 1) for _ in range(10000)])
    print(sol.largestValues(root))