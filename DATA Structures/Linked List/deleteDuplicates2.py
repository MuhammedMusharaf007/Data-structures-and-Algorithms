class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def deleteDuplicates(self):
        node = self.head
        if node == None:
            return
        if node.next:
            if node.data == node.next.data:
                to_remove = node.next
                node.next = node.next.next
                self.deleteDuplicates(node)
            else:
                self.deleteDuplicates(node.next)

        return node