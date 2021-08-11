class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def NthfromEnd(self, n):
        temp = self.head
        len = 0
        while temp:
            len +=1
            temp = temp.next

        if n>len:
            return
        
        temp = self.head
        for _ in range(len-n):
            temp = temp.next
        print(temp.data)
    
    def printNthFromLast(self, n):
        main_ptr = self.head
        ref_ptr = self.head

        count = 0
        if self.head:
            while count<n:
                if ref_ptr is None:
                    print(f"{n} is greater than the number of nodes")
                    return
                ref_ptr = ref_ptr.next
                count += 1

        if ref_ptr is None:
            self.head = self.head.next
            if self.head:
                print(f"Node no. {n} from the last is {main_ptr.data}")
        else:
            while ref_ptr:
                main_ptr = main_ptr.next
                ref_ptr = ref_ptr.next

            print(f"Node no.{n} from the last os")