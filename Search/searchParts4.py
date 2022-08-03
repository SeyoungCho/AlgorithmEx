import time

N = int(input())
parts = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))
start_time = time.time()


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


parts.sort()
for i in range(M):
    if binary_search(parts, targets[i], 0, len(parts) - 1) == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
print()

end_time = time.time()
print("time: ", end_time - start_time)
