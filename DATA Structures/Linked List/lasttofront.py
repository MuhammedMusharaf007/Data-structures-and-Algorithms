from typing import NoReturn


class Node:

    def __init__(self, data):
        self.data = data
        self.next = next

class Linkedlist:

    def __init__(self):
        self.head = None

    def lasttoFront(self):
        temp = self.head
        
        if temp is None:
            return
        
        prev = None
        
        while temp.next:
            prev = temp
            temp = temp.next
        
        prev.next = None
        temp.next = self.head
        self.head = temp