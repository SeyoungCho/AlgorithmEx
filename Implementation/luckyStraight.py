import time

data = list(input())
start_time = time.time()
#parse input list into integer list
score = list(map(int, data))
#evaluate the sums of the first half and the second half
mid = (len(score)- 1) // 2
sum_1 = sum(score[:mid+1])
sum_2 = sum(score[mid+1:])
if sum_1 == sum_2:
  print("LUCKY")
else:
  print("READY")
end_time = time.time()
print("time :",end_time - start_time)
