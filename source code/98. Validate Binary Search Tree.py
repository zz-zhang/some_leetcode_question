# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        valid, _, _ = self.travel(root)
        return valid

    def travel(self, root):
        max_val = root.val
        min_val = root.val
        valid = True
        if root.left is not None:
            valid_left, max_left, min_left = self.travel(root.left)
            if max_left >= root.val:
                valid_left = False 
            valid = valid and valid_left
            max_val = max(max_val, max_left)
            min_val = min(min_val, min_left)
        
        if root.right is not None:
            valid_right, max_right, min_right = self.travel(root.right)
            if min_right <= root.val:
                valid_right = False
            valid = valid and valid_right
            max_val = max(max_val, max_right)
            min_val = min(min_val, min_right)

        print(root.val, valid, max_val, min_val)
        return valid, max_val, min_val

if __name__ == '__main__':
    sol = Solution()