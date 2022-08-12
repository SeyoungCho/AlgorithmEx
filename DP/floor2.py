import time
N = int(input())
start_time = time.time()
D = [0] * 1000
D[1] = 1
D[2] = 3
for i in range(3, N+1):
	D[i] = 2 * D[i-1] - D[i-2]
print(D[N] % 796796)
end_time = time.time()
print("time: ", end_time - start_time)