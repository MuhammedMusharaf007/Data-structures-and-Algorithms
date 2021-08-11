def rotateArray(arr, d, n):
    d = d%n
    g_c_d = gcd(d ,n)
    for i in range(g_c_d):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k>=n:
                k  = k-n
            if k==i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)


def printArray(arr):
    for i in arr:
        print(i, end=" ")
    print("")


t = int(input())
for _ in range(t):
    n,d = map(int, input().split())
    arr = list(map(int, input().split()))
    rotateArray(arr, d, n)
    printArray(arr)