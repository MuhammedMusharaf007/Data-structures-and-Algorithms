class DLLNode:

    
    def __init__(self, data):
        
        self.prev = None
        self.data = data
        self.next = next

    
class myStack:


    def __init__(self):
        
        self.head = None
        self.mid = None
        self.count = 0


def createMyStack():

    ms = myStack()
    ms.count = 0
    
    return ms


def push(ms, new_data):

    new_DLLNode = DLLNode(new_data)
    new_DLLNode.prev = None
    new_DLLNode.next = ms.head
    ms.count += 1

    if ms.count == 1:
        ms.mid = new_DLLNode

    else:
        ms.head.prev = new_DLLNode

        if ms.count % 2 != 0:
            ms.mid = ms.mid.prev

    ms.head = new_DLLNode


def pop(ms):

    if ms.count == 0:
        print("Stack underflow")

        return -1

    head = ms.head
    item = head.data
    ms.head = head.next

    if ms.head != None:
        ms.head.prev = None
    
    ms.count -= 1

    if ms.count % 2 == 0:
        ms.mid = ms.mid.next
    
    return item


def findMiddle(ms):

    if ms.count == 0:
        print("Stack is empty")
        
        return -1
    
    return ms.mid.data


def deleteMiddle(ms):
    
    if ms.count == 0:
        print("Stack Underflow")

        return -1

    temp = ms.mid.data

    prev = ms.mid.prev
    nxt = ms.mid.next
    prev.next = nxt
    nxt.prev = prev
    ms.count -= 1

    if ms.count % 2 != 0:
        ms.mid = ms.mid.prev

    else:
        ms.mid = ms.mid.next

    return temp


if __name__ == '__main__':
 
    ms = createMyStack()
    push(ms, 11)
    push(ms, 22)
    push(ms, 33)
    push(ms, 44)
    push(ms, 55)
    push(ms, 66)
    push(ms, 77)

    print(ms.count)
    print("Middle Element is " +
          str(findMiddle(ms)))
    print("Item popped is " +
          str(pop(ms)))
    print(ms.count)
    print("Middle Element is " +
          str(findMiddle(ms)))
    print("Item popped is " +
          str(pop(ms)))
    print("Middle Element is " +
          str(findMiddle(ms)))
    print("Item popped is " +
          str(pop(ms)))
    print("Middle Element is " +
          str(findMiddle(ms)))
    print("Deleted Middle Element is " + str(deleteMiddle(ms)))
    print("Middle Element is " +
          str(findMiddle(ms)))