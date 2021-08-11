class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = None

    def isPalindrome(self):
        temp1 = self.head
        stack = []
        ispalin = True
        while temp1:
            stack.append(temp1.data)
            temp1 = temp1.next
        temp2 = self.head
        while temp2:
            i = stack.pop()
            if temp2.data == i:
                ispalin = True
            else:
                ispalin = False
                break
            temp2 = temp2.next
        return ispalin
        