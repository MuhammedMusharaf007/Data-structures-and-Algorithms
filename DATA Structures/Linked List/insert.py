class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given node should be in LinkedList")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print("")

if __name__=='__main__':
    
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()
    llist.push(5)
    llist.printList()
    llist.insertAfter(second, 9)
    llist.printList()
    llist.append(11)
    llist.printList()