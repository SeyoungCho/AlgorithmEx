import time
input_string = list(input())
start_time = time.time()

S = list(map(int, input_string))
result = S[0]

for i in range(1, len(S)):
  if result <= 1 or S[i] <= 1:
    result += S[i]
  else:
    result *= S[i]
print(result)
end_time = time.time()
print("time :",end_time - start_time)