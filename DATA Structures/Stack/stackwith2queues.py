from queue import Queue

class Stack:

    def __init__(self):

        self.q1 = Queue()
        self.q2 = Queue()

        self.curr_size = 0

    