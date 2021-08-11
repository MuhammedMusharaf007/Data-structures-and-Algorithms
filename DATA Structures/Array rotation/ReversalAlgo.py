def leftRotate(arr, n, d):
    reverseArray(arr,0 , d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)


def reverseArray(arr, start, end):
    while start<end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print("")


t = int(input())
for _ in range(t):
    n,d = map(int, input().split())
    arr = list(map(int, input().split()))
    leftRotate(arr, n, d)
    printArray(arr)