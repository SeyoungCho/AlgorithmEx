import time

N, M = map(int, input().split())
op = []
for i in range(M):
  a, b, c = map(int, input().split())
  op.append([a,b,c])
start_time = time.time()
#make a list of students, student[i] is the team where ith student is
#belongs to
students = [i for i in range(N+1)]

#returns which team x is with
def find_team(students, x):
  if students[x] != x:
    students[x] = find_team(students, students[x])
  return students[x]
#merges student a's team and student b's find_team
def merge_team(students, a, b):
  a_team = find_team(students, a)
  b_team = find_team(students, b)
  if a_team < b_team:
    students[b] = a_team
  else:
    students[a] = b_team

#compute op list line by line
for i in op:
  #merge case
  if i[0] == 0:
    merge_team(students, i[1], i[2])
  #is same team case
  else:
    if find_team(students, i[1]) == find_team(students, i[2]):
      print('YES')
    else:
      print('NO')

end_time = time.time()
print("time :", end_time-start_time)
