class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    def swapnodes(self, x, y):
        if x==y:
            return

        prev_x = None
        curr_x = self.head
        while curr_x and curr_x.data != x:
            prev_x = curr_x
            curr_x = curr_x.next

        prev_y = None
        curr_y = self.head
        while curr_y and curr_y.data != y:
            prev_y = curr_y
            curr_y = curr_y.next

        if prev_x is None:
            self.head = curr_y
        else:
            prev_x.next = curr_y
        
        if prev_y is None:
            self.head = curr_x
        else:
            prev_y.next = curr_x

        temp = curr_x.next
        prev_x.next = curr_y.next
        prev_y.next = temp
