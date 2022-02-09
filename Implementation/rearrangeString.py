import time
import heapq
S = list(input())

start_time = time.time()
#prepare a list to store letters and a sum variable to store sum of the numbers
letter = []
sum = 0
for i in S:
  #if it's an alphabet
  if i >= 'A' and i<= 'Z':
    #push it into the priority queue
    heapq.heappush(letter, i)
  #if it's a number
  else:
    sum += int(i)

#pop from the priority queue and print the letter one by one
while letter:
  l = heapq.heappop(letter)
  print(l,end='')
print(sum)
end_time = time.time()
print("time :",end_time - start_time)