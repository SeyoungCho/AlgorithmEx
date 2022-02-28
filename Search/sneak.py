import time 
from itertools import combinations
import copy
N = int(input())
hall = [list(input().split()) for _ in range(N)]

start_time = time.time() 
result = "NO"
teachers = []
students = []
space = []
for i in range(N):
	for j in range(N):
		if hall[i][j] == 'S':
			students.append((i, j))
		elif hall[i][j] == 'T':
			teachers.append((i, j))
		else:
			space.append((i, j))

	
#returns true if all the students don't get caught
def sneak_check(sim_hall):
	#mark danger area covered by all the teachers
	for teacher in teachers:
		tx, ty = teacher[0], teacher[1]
		#check up
		for i in range(tx+1):
			if sim_hall[tx-i][ty] == 'O':
				break
			elif sim_hall[tx-i][ty] == 'S':
				return False
			else:
				continue
		#check down
		for i in range(1, N-tx):
			if sim_hall[tx+i][ty] == 'O':
				break
			elif sim_hall[tx+i][ty] == 'S':
				return False
			else:
				continue
		#check left
		for i in range(ty+1):
			if sim_hall[tx][ty-i] == 'O':
				break
			elif sim_hall[tx][ty-i] == 'S':
				return False
			else:
				continue
		#check right
		for i in range(1, N-ty):
			if sim_hall[tx][ty+i] == 'O':
				break
			elif sim_hall[tx][ty+i] == 'S':
				return False
			else:
				continue
	return True

			
#check every case where the 3 obstacles are added
for obsList in combinations(space, 3):
	#create a simulation board with obstacles 
	sim_hall = copy.deepcopy(hall)
	for obs in obsList:
		x, y = obs[0], obs[1]
		sim_hall[x][y] = 'O'
	if sneak_check(sim_hall):
		result = "YES"
		break
		
print(result)

end_time = time.time() 
print("time :", end_time - start_time)