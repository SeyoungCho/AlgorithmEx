#binary search solution
def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return True
    elif arr[mid] > target:
      end = mid - 1
      continue
    else:
      start = mid + 1
      continue
  return False

import time

N = int(input())
parts = list(map(int, input().split()))
M = int(input())
order = list(map(int, input().split()))

start_time = time.time()
#sort the input lists
parts.sort()
order.sort()
#binary search the elements of the order list in the parts list
for i in range(M):
  if binary_search(parts, order[i], 0, N-1):
    print("yes", end=" ")
  else:
    print("no", end=" ")
print()


end_time = time.time() 
print("time :", end_time - start_time)
