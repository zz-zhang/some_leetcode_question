# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def build_BST(self, num_list, index, depth):
        root = TreeNode(num_list[index])
        left_sub_list = num_list[:index]
        right_sub_list = num_list[index+1:]
        max_depth = depth

        if len(left_sub_list) > 0:
            root.left, temp_depth = self.build_BST(left_sub_list, int(len(left_sub_list) / 2), depth + 1)
            max_depth = max(max_depth, temp_depth)
        if len(right_sub_list) > 0:
            root.right, temp_depth = self.build_BST(right_sub_list, int(len(right_sub_list) / 2), depth + 1)
            max_depth = max(max_depth, temp_depth)
        return root, max_depth


    def normalize_BST(self, root, depth, max_depth):
        if depth == max_depth - 1:
            if root.left is None:
                root.left = TreeNode(None)
            if root.right is None:
                root.right = TreeNode(None)
        if root.left is not None:
            self.normalize_BST(root.left, depth + 1, max_depth)
        if root.right is not None:
            self.normalize_BST(root.right, depth + 1, max_depth)
        # if root.left is not None:
        #     self.normalize_BST(root.left)
        # if root.right is not None:
        #     self.normalize_BST(root.right)
        #
        #
        # if root.left is not None and root.right is None:
        #     root.right = TreeNode(None)
        # if root.left is None and root.right is not None:
        #     root.left = TreeNode(None)
        return root


    def visit_node_BFS(self, node):
        q = []
        q.append(node)
        res = []
        while True:
            head = q[0]
            if head.left is not None:
                q.append(head.left)
            if head.right is not None:
                q.append(head.right)
            res.append(head.val)
            q.pop(0)
            if len(q) == 0:
                break
        return res


    def sortedArrayToBST(self, nums) -> TreeNode:
        res = []
        if len(nums) > 0:
            root, depth = self.build_BST(nums, int(len(nums) / 2), 1)
            # print(depth)
            root = self.normalize_BST(root, 1, depth)
            res = self.visit_node_BFS(root)
            while res[-1] is None:
                res.pop(-1)
        return res

if __name__ == '__main__':
    s = Solution()
    input = [0,1,2,3,4,5,6,7,8]
    print(s.sortedArrayToBST(input))