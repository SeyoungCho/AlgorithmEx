import time

N = int(input())

start_time = time.time()
#3 hour including 3 
#15 minute, and second including 3 
#45 minute, second not including 3
count = 0
if N < 3:
  count = (N+1)*45*15 + (N+1)*15*60
elif N >= 3 and N < 13:
  count = N*45*15 + N*15*60 + 60*60
elif N >= 13 and N < 23:
  count = (N-1)*45*15 + (N-1)*15*60 + 2*60*60
else:
  count = 21*45*15 + 21*15*60 + 3*60*60

end_time = time.time()
print(count)
print("time :", end_time - start_time)