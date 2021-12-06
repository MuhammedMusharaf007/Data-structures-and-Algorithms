
from collections import deque

stack = deque()

for i in range(1, 11):
    stack.append(i)
    print("New stack: {}".format(stack))