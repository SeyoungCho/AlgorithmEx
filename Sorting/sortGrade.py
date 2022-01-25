import time
N = int(input())
students = []
for i in range(N):
  info = input().split()
  students.append((info[0], int(info[1])))
start_time = time.time()
students = sorted(students, key=lambda student: student[1])
for i in students:
  print(i[0], end=" ")
print()
end_time = time.time() 
print("time :", end_time - start_time)