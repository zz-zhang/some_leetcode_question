from utils import print_list

class MyLinkedList:

    def __init__(self, val=None, _next=None, prev=None):
        self.val = val
        self.next = _next
        self.prev = prev

    def get(self, index: int) -> int:
        fake_head = self
        while fake_head.prev is not None:
            fake_head = fake_head.prev
        
        idx = 0
        node = fake_head
        for idx in range(0, index+1):
            if node.next is not None:
                node = node.next
            else:
                return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        fake_head = self
        while fake_head.prev is not None:
            fake_head = head.prev
        new_head = MyLinkedList(val, fake_head.next, fake_head)
        if fake_head.next is not None:
            fake_head.next.prev = new_head
        fake_head.next = new_head


    def addAtTail(self, val: int) -> None:
        tail = self
        while tail.next is not None:
            tail = tail.next
        new_tail = MyLinkedList(val, None, tail)
        tail.next = new_tail
        

    def addAtIndex(self, index: int, val: int) -> None:
        fake_head = self
        while fake_head.prev is not None:
            fake_head = fake_head.prev
        
        node = fake_head
        for idx in range(0, index):
            if node.next is not None:
                node = node.next
            else:
                return

        # node = node.prev
        # breakpoint()
        new_node = MyLinkedList(val, node.next, node)
        if node.next is not None:
            node.next.prev = new_node
        node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        fake_head = self
        while fake_head.prev is not None:
            fake_head = fake_head.prev
        
        node = fake_head
        for idx in range(0, index+1):
            if node.next is not None:
                node = node.next
            else:
                return
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

if __name__ == '__main__':
    myLinkedList = MyLinkedList()

    # myLinkedList.addAtHead(7)
    # print_list(myLinkedList)

    # myLinkedList.addAtHead(2)
    # print_list(myLinkedList)

    # myLinkedList.addAtHead(1)
    # print_list(myLinkedList)

    myLinkedList.addAtIndex(0, 10)
    print_list(myLinkedList)

    myLinkedList.addAtIndex(0, 20)
    print_list(myLinkedList)

    myLinkedList.addAtIndex(1, 30)
    print_list(myLinkedList)

    print(myLinkedList.get(0))

    myLinkedList.deleteAtIndex(2) 
    print_list(myLinkedList)

    # myLinkedList.addAtHead(6)
    # print_list(myLinkedList)

    # myLinkedList.addAtTail(4)
    # print_list(myLinkedList)
    
    # print(myLinkedList.get(4))

    # myLinkedList.addAtHead(4)
    # print_list(myLinkedList)

    # myLinkedList.addAtIndex(5, 0)
    # print_list(myLinkedList)

    # myLinkedList.addAtHead(4)
    # print_list(myLinkedList)