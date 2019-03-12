# import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        pass


    def DLR(self, root):
        if root.val is None:
            return []
        result = []
        result.extend([root.val])
        if root.left is not None:
            result.extend(self.DLR(root.left))
        if root.right is not None:
            result.extend(self.DLR(root.right))
        return result


    def LRD(self, root):
        if root.val is None:
            return []
        result = []
        if root.left is not None:
            result.extend(self.DLR(root.left))
        if root.right is not None:
            result.extend(self.DLR(root.right))
        result.extend([root.val])
        return result


    def isSymmetric(self, root: TreeNode) -> bool:
        # print(self.DLR(root))
        # print(self.LRD(root))
        res_DLR = self.DLR(root)
        res_LRD = self.LRD(root)
        # res_DLR = res_DLR.replace('None', 'N')
        # res_LRD = res_LRD.replace('None', 'N')
        print(res_DLR)
        print(res_LRD[::-1])
        if res_DLR == res_LRD[::-1]:
            return True
        else:
            return False


def build_tree(input_list, index):
    # print(input_list)
    if index >= len(input_list):
        return None
    if input_list[index] is not None:
        root = TreeNode(input_list[index])
        root.left = build_tree(input_list, (index + 1) * 2 - 1)
        root.right = build_tree(input_list, (index + 1) * 2)
        return root
    else:
        return None


# def visit_node_bfs(root):
#     bfs_queue = queue.Queue()
#     head = root
#     tail = head
#     bfs_queue.put(root)
#     while True:
#         head = bfs_queue.get()
#         print(head.val)
#         if head.left is not None:
#             bfs_queue.put(head.left)
#         if head.right is not None:
#             bfs_queue.put(head.right)
#         if bfs_queue.empty():
#             break


if __name__ == '__main__':
    s = Solution()
    input_list = [4,-57,-57,None,67,67,None,None,-97,-97]
    # input_list = [1, 2, 2]
    root = build_tree(input_list, 0)
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # # root.left.left = TreeNode(None)
    # root.left.right = TreeNode(3)
    # root.right = TreeNode(2)
    # # root.right.left = TreeNode(None)
    # root.right.right = TreeNode(3)
    # visit_node_bfs(root)
    print(s.isSymmetric(root))