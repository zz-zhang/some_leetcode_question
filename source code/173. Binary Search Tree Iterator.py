from typing import Optional
from utils import build_tree, TreeNode

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.recoder = []
        self.in_order(root)
        self.iterator = -1
        # print(len(self.recoder))

    def next(self) -> int:
        self.iterator += 1
        return self.recoder[self.iterator].val

    def hasNext(self) -> bool:
        # print(self.iterator)
        if self.iterator < len(self.recoder) - 1:
            # print(True)
            return True
        else:
            # print(False)
            return False
        
    def in_order(self, node):
        if node.left is not None:
            self.in_order(node.left)
        self.recoder.append(node)
        if node.right is not None:
            self.in_order(node.right)

if __name__ == '__main__':
    root = build_tree('[7,3,15,null,null,9,20]')
    bSTIterator = BSTIterator(root)
    bSTIterator.next();    # return 3
    bSTIterator.next();    # return 7
    bSTIterator.hasNext(); # return True
    bSTIterator.next();    # return 9
    bSTIterator.hasNext(); # return True
    bSTIterator.next();    # return 15
    bSTIterator.hasNext(); # return True
    bSTIterator.next();    # return 20
    bSTIterator.hasNext(); # return False