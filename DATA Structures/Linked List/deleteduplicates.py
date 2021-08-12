class Node:

    def __init__(self, data):
        self.data = data
        self.next = next

class Linkedlist:

    def __init__(self):
        self.head = None

    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next =  None
                temp.next = new
            else:
                temp = temp.next
        return self.head