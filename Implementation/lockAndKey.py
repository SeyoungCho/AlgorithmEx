import time
import copy
start_time = time.time()

key = [[0,0,1],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

#rotates an n * n array clockwise
def rotate_right(arr):
  n = len(arr)
  new_arr = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      new_arr[i][j] = arr[n-j-1][i]
  return new_arr

#match method (adds up lock and key)
def match(arr, key, rot, r, c):
  n = len(key)
  _key = copy.deepcopy(key)
  #rotate the key rot times
  for _ in range(rot):
    _key = rotate_right(_key)
  for i in range(n):
    for j in range(n):
      arr[r+i][c+j] += _key[i][j]  

#checks if all the elements of the lock is 1
def check(arr, offset, n):
  for i in range(n):
    for j in range(n):
      if arr[offset+i][offset+j] != 1:
        return False
  return True


def solution(key, lock):
  #make a big array and locate key and lock in the array
  offset = len(key) - 1
  for r in range(offset + len(lock)):
    for c in range(offset + len(lock)):
      for rot in range(4):
        #big array
        arr = [[0 for _ in range(58)] for _ in range(58)]
        #copy the lock into the big array
        for i in range(len(lock)):
          for j in range(len(lock)):
            arr[offset + i][offset + j] = lock[i][j]
        match(arr, key, rot, r, c)
        if check(arr, offset, len(lock)):
          return True      
  return False

print(solution(key, lock))

end_time = time.time()
print("time :",end_time - start_time)