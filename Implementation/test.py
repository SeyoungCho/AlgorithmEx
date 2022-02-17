def rotate_right(arr):
  n = len(arr)
  new_arr = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      new_arr[i][j] = arr[n-j-1][i]
  return new_arr

arr = [[1,1,2],[3,4,5],[0,1,9]]

key = rotate_right(arr)
print(key)

