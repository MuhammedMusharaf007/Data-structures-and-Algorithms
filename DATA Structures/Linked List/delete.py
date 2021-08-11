class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
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

    def deleteNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def deleteNodefrom(self, position):
        temp = self.head
        if temp is None:
            return
        
        if position == 0:
            self.head = temp.next
            temp = 0
            return
        
        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next
        temp.next = None
        temp.next = next

    def deleteList(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("")

if __name__=='__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)

    print("Created Linked List:")
    llist.printList()
    llist.deleteNode(3)
    print("After deletion of 3:")
    llist.printList()
    llist.deleteNodefrom(1)
    llist.printList()