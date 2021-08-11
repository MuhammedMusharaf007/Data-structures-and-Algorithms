class Node:

    def __init__(self, data):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def search(self, key):
        if self.head is None:
            return False
        
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def searchrec(self, li, key):
        if li is None:
            return False
        
        if li.data == key:
            return True

        return self.searchrec(li.next, key)