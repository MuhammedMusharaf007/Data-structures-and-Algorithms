class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def getCount(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def getcountrec(self, node):
        if not node:
            return 0
        else:
            return 1 + self.getcountrec(node.next)

    def getcount2(self):
        return self.getcountrec(self.head)