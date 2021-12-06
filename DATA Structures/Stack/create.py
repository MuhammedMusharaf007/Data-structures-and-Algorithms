stack = []
for i in range(10):
    stack.append(i)
print("New stack: ", end=" ")
print(stack)

for _ in range(11):
    a = stack.pop()
    print("Element popped : {}".format(a))
    print("stack after popping: ", end=" ")
    print(stack)