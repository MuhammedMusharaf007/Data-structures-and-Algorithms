class Node:

    def __init__(self, data):
        self.data = data
        self.next = data

class Linkedlist:

    def __init__(self):
        self.head = None

    def countLoopNodes(self):
        if self.head is None:
            return 0
            
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                x = fast
        count = 1
        nex = x.next
        while nex:
            if nex == x:
                return count
            count += 2
            nex = nex.next
