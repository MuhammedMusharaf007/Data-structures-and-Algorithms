class Node:

    def __init__(self):
        self.data = 0
        self.next = None
        self.flag = 0

class Linkedlist:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node()
        new_node.data = new_data
        new_node.flag = 0
        new_node.next = self.head
        self.head = new_node

    def detectLoop(self):
        temp = self.head
        while temp:
            if temp.flag == 1:
                return True
            temp.flag = 1
            temp = temp.next