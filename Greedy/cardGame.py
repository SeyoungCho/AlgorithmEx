import time

N,M = map(int, input().split())
arr = [[int(x) for x in input().split()] for y in range (N)]

start_time = time.time()
print(arr)
#sort all the rows
for i in range(N):
  arr[i].sort()

#create a new list holding the mininum elements of each row
card = []
for i in range(N):
  card.append(arr[i][0])

#sort the new list and select the maximum element
card.sort()
print(card[N-1])
end_time = time.time()
print("time :", end_time - start_time)