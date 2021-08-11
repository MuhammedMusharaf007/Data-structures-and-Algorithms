class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def countint(self, x):
        temp = self.head
        count = 0
        while temp:
            if temp.data == x:
                count += 1
            temp = temp.next
        return count

    def countintrec(self, node, x):
        if node is None:
            return
        else:
            if node.data == x:
                return 1+ self.countintrec(node.next,x)
            else:
                return self.countintrec(node.next, x)


    def countintinit(self, x):
        temp = self.head
        return self.countintrec(temp, x)