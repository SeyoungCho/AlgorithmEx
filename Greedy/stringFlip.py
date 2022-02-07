import time
S = input()
s = list(map(int, S))
start_time = time.time()
#count array for counting groups of numbers
count = [0, 0]
count[s[0]] += 1
for i in range(len(s)-1):
  # if the next number changes, group count + 1
  if s[i] != s[i+1]:
    count[s[i+1]] += 1
print(min(count[0], count[1]))
end_time = time.time()
print("time :", end_time - start_time)