import time
import math
from itertools import permutations
start_time = time.time() 

#returns which points dist can cover starting from sp_th point
def coverPoints(sp, dist, route, n):
  #list of points that dist covered
  cover = [sp]
  #remaining distance
  d = dist
  i = sp
  #until dist cannot cover the next point with remaining distance
  while route[i] <= d:
    cover.append(i+1)
    i = (i + 1) % n
    #if it covered all the points, break
    if len(cover) == len(route):
      break;
  return cover

def solution(n, weak, dist):
  
  weakSize = len(weak)
  minCnt = math.inf
  weak = weak + [w+n for w in weak]
  #start point
  for start in range(weakSize):
    #check all the possible permutations of friends
    for d in permutations(dist, len(dist)):
      #no. of friends used
      cnt = 1
      pos = start
      #for all points that are not visited
      for i in range(1, weakSize):
        nextPos = start + i
        #distance between current point and the next point
        diff = weak[nextPos] - weak[pos]
        #if current friend cannot reach the next point
        if diff > d[cnt - 1]:
          #move the start point to the next point
          pos = nextPos
          #and use a new friend
          cnt += 1
          if cnt > len(dist):
            break
      if cnt <= len(dist):
        minCnt = min(minCnt, cnt)
  if minCnt == math.inf:
    return -1
  else:
    return minCnt
 
end_time = time.time() 
print("time :",end_time-start_time)