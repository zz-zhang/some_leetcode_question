class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

    @classmethod
    def build_by_str(cls, string):
        string = string.replace(' ', '')
        if string == '{}' or string == '[]':
            return None
        nodes = [
            None if val == 'null' else cls(int(val))
            for val in string.strip('[]{}').split(',')
        ]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()

        return cls(root.val, root.left, root.right)

    def draw(self):
        def height(root):
            return 1 + max(height(root.left), height(
                root.right)) if root else -1

        def jumpto(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

        def draw(node, x, y, dx):
            if node:
                t.goto(x, y)
                jumpto(x, y - 20)
                t.write(node.val, align='center', font=('Arial', 12, 'normal'))
                draw(node.left, x - dx, y - 60, dx / 2)
                jumpto(x, y - 20)
                draw(node.right, x + dx, y - 60, dx / 2)

        import turtle
        t = turtle.Turtle()
        t.speed(0)
        turtle.delay(0)
        h = height(self)
        jumpto(0, 30 * h)
        draw(self, 0, 30 * h, 40 * h)
        t.hideturtle()
        turtle.mainloop()


class TreeNodeFor116(TreeNode):
    def __init__(self, val, left=None, right=None):
        super(TreeNodeFor116, self).__init__(val, left=left, right=right)
        self.next = None

    def get_next_list(self):
        q = [self]
        res = []
        first_node_in_depth = self
        while len(q) > 0:
            node = q[0]
            res.append(node.val)
            if node.next is None:
                res.append(None)
                if first_node_in_depth.left is not None:
                    q.append(first_node_in_depth.left)
                    first_node_in_depth = first_node_in_depth.left
            else:
                q.append(node.next)
            q = q[1:]
        return res
                

def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(lst):
    if len(lst) > 0:
        head = ListNode(lst[0])
        node = head
        for val in lst[1:]:
            node.next = ListNode(val)
            node = node.next
        return head
    return None


def print_list(head):
    node = head
    print('[', end='')
    while node is not None:
        print(node.val, end=',')
        node = node.next
    print(']')