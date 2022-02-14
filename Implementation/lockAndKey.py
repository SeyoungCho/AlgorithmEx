import time
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

def solution(key, lock):
  result = False
  return result

print(solution(key, lock))

end_time = time.time()
print("time :",end_time - start_time)