import time

N,M,K = map(int, input().split())
data = list(map(int, input().split()))

start_time = time.time()
tmpData = list(sorted(data))
tmpData.reverse()
tmpData = [int(x) for x in tmpData]
print(tmpData)
count = M
sum = 0
while True:
  for i in range(K):
    if(count == 0):
      break
    sum += tmpData[0]
    count -= 1
  if(count == 0):
    break
  sum += tmpData[1]
  count -= 1

       
end_time = time.time()
print(sum)
print("time :", end_time - start_time)   