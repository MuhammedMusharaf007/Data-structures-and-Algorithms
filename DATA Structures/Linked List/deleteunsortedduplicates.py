class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def deleteduplicate(self):
        temp = self.head
        hash = set()
        hash.add(temp.data)
        while temp.next:
            if temp.next.data in hash:
                temp.next = temp.next.next
            else:
                hash.add(temp.next.data)
                temp = temp.next
        return self.head