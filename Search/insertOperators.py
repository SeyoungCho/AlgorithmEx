import time
N = int(input())
numList = list(map(int, input().split()))
opList = list(map(int, input().split()))

start_time = time.time() 
resultList = []
#recursively evaluate the result of operation 
def dfs(a, i, opList):
	#termination condition, when it reached the last index
	if i == len(numList) - 1:
		idx = opList.index(1)
		result = 0
		if idx == 0:
			result = a + numList[i]
		elif idx == 1:
			result = a - numList[i]
		elif idx == 2:
			result = a * numList[i]
		else:
			result = a // numList[i] if a > 0 else -1*(-1*a//numList[i])
		resultList.append(result)
	else:
		if opList[0] > 0:
			dfs(a + numList[i], i+1, [opList[0]-1, opList[1], opList[2], opList[3]])
		if opList[1] > 0:
			dfs(a - numList[i], i+1, [opList[0], opList[1]-1, opList[2], opList[3]])	
		if opList[2] > 0:
			dfs(a * numList[i],i+1,[opList[0], opList[1], opList[2]-1, opList[3]])
		if opList[3] > 0:
			dfs(a // numList[i] if a > 0 else -1*(-1*a//numList[i]), i+1, [opList[0], opList[1], opList[2], opList[3]-1])		

dfs(numList[0], 1, opList)
print(max(resultList))
print(min(resultList))
end_time = time.time() 
print("time :",end_time - start_time)
