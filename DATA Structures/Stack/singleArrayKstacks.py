class KStacks:

    
    def __init__(self, k, n):

        self.k = k
        self.n = n

        self.arr = [0] * self.n
        self.top = [-1] * self.k

        self.free = 0

        self.next = [i + 1 for i in range (self.n - 1)]
        self.next[self.n -1] = -1

    
    def isEmpty(self, sn):
        
        return self.top[sn] == -1

    
    def isFull(self):
        
        return self.free == -1

    
    def push(self, item, sn):
        
        if self.isFull():
            print("Stack Overflow")

            return
        
        insert_at = self.free
        self.free = self.next[self.free]
        self.arr[insert_at] = item
        self.next[insert_at] = self.top[sn]
        self.top[sn] = insert_at
