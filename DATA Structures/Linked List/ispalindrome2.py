class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def isPalindrome(self, head):
        slow = self.head
        fast = self.head
        prev_slow = self.head
        midnode = None
        res = True

        if head and head.next:
            while fast and fast.next:
                fast = fast.next.next
                prev_slow = slow
                slow = slow.next
            
            if fast:   
                midnode = slow
                slow = slow.next
            
            second_half = slow
            prev_slow.next = None
            second_half = self.reverse(second_half)
            res = self.compareLists(head, second_half)
            second_half = self.reverse(second_half)

            if midnode:
                prev_slow.next = midnode
                midnode.next = second_half
            else:
                prev_slow.next = second_half
        return res

    def reverse(self, second_half):
        prev = None
        current = second_half
        next = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        second_half = prev
        return second_half

    def compareLists(self,head1, head2):
        temp1 = head1
        temp2 = head2
        while temp1 and temp2:
            if temp1.data == temp2.data:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return 0
        if temp1 is None and temp2 is None:
            return 1
        return 0