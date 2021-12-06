from queue import LifoQueue

stack = LifoQueue(maxsize=3)

print("queue size: ", stack.qsize())

stack.put("a")
stack.put("b")
stack.put("c")

print("Full: ", stack.full())
print("Size: ", stack.qsize())

print("Elements popped from the stack")
print(stack.get())
print(stack.get())
print(stack.get())

print("")
print("Empty: ", stack.empty)