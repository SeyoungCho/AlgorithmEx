import time

N, M = map(int, input().split())
unit = []
for _ in range(N):
  unit.append(int(input()))
start_time = time.time()
unit.sort()
d = [-1] * 10001

for j in unit:
  d[j] = 1

for i in range(unit[0], M+1):
  candidates = []
  if d[i] == 1:
    continue
  #make a list of possible candidates
  #mutiples
  for j in unit:
    if i % j == 0:
      candidates.append(i // j)
  for j in unit:
    if i > j and d[i-j] != -1:
      candidates.append(d[i-j] + 1)
  #take the smallest of the candidates
  if len(candidates)!= 0:
    d[i] = min(candidates)

print(d[M])

end_time = time.time()
print("time :", end_time - start_time)