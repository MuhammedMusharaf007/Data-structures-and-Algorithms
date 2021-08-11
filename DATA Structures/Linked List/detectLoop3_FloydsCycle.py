class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        temp = self.head
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def detectLoop(self):
        fast_ptr = self.head
        slow_ptr = self.head
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False