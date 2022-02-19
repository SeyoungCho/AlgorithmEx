import time
import copy
import heapq

start_time = time.time() 
#checks if the removal is valid
#rem: the one we're trying to remove
def remove_check(arr, x, y, _type):
  tmp_arr = copy.deepcopy(arr)
  tmp_arr.remove([x,y,_type])
  #pillar
  if _type == 0:
    if [x,y+1,0] in tmp_arr:
      if not install_check(tmp_arr, x, y+1, 0):
        return False
    if [x,y+1,1] in tmp_arr:
      if not install_check(tmp_arr,x,y+1,1):
        return False
    if [x-1,y+1,1] in tmp_arr:
      if not install_check(tmp_arr, x-1,y+1,1):
        return False
  #beam
  else:
    if [x-1,y,1] in tmp_arr:
      if not install_check(tmp_arr, x-1,y,1):
        return False
    if [x,y,0] in tmp_arr:
      if not install_check(tmp_arr, x, y, 0):
        return False
    if [x+1,y,0] in tmp_arr:
      if not install_check(tmp_arr, x+1,y,0):
        return False
    if [x+1,y,1] in tmp_arr:
      if not install_check(tmp_arr, x+1, y,1):
        return False   
  return True

#checks if the installation is valid
#ins: the one we're trying to build
def install_check(arr, x, y, _type):
  #pillar
  if _type == 0:
    a = y == 0
    b = x != 0 and ([x-1,y,1] in arr or [x,y,1] in arr)
    c = x == 0 and [x,y,1] in arr
    d = y != 0 and [x,y-1,0] in arr
    if a or b or c or d:
      return True
    else:
      return False
  #beam
  else:
    a = [x,y-1,0] in arr or [x+1,y-1,0] in arr
    b = [x-1,y,1] in arr and [x+1,y,1] in arr
    if a or b:
      return True
    else:
      return False

def solution(n, build_frame):
  answer = []
  #start from build_frame[0] to build_frame[len(build_frame)-1]
  for step in build_frame:
      x, y, _type, action = step
      #install
      if action == 1:
        if install_check(answer, x, y, _type):
          answer.append([x,y,_type])
      else:
        if remove_check(answer, x, y, _type):
          answer.remove([x,y,_type])
  answer.sort(key=lambda x: (x[0],x[1],x[2]))
  return answer

build_frame = [
  [0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]
]
answer = solution(5, build_frame)
print(answer)

end_time = time.time() 
print("time :",end_time - start_time)