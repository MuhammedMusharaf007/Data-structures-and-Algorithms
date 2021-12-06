class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linkedlist:

    def __init__(self):
        self.head = None

    def pairwiseSwap(self):
        temp = self.head
        if temp is None:
            return
        while temp and temp.next:
            if temp.data == temp.next.data:
                temp.data, temp.next.data = temp.next.data, temp.data
            temp = temp.next.next
