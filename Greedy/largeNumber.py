import time

N,M,K = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()

#sort the list and reverse it
tmpData = list(sorted(data))
tmpData.reverse()

count = M
sum = 0

while True:
  for i in range(K):  
    if(count == 0): #iterate M times
      break
    sum += tmpData[0] #add tmpData[0](the largest) K times
    count -= 1
  if(count == 0):
    break
  sum += tmpData[1] #add second largest number 
  count -= 1

end_time = time.time()
print(sum)
print("time :", end_time - start_time)   