class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def GetNth(self, k):
        current = self.head
        count = 1
        while current:
            if count == k:
                return current.data
            count += 1
            current = current.next
        assert(False)
        return 0

    def getNthrec(self, llist, position):
        llist.getNthNode(self.head, position, llist)

    def getNthNode(self, head, position, llist):
        count = 0
        if head:
            if count == position:
                print(head.data)
            else:
                llist.getNthNode(head.next, position-1, llist)
        else:
            print("Index doesn't exist")