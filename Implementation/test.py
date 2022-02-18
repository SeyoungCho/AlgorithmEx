dirChange = [0] * 10
for i in range(3):
  t, D = input().split()
  dirChange[int(t)] = 1 if D == 'D' else -1

print(dirChange)