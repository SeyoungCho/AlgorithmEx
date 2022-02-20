import time
from itertools import permutations

start_time = time.time()
def solution(n, weak, dist):
  dist.sort(reverse=True)
  answer = -1
  #check every case from only 1 friend to all the friends
  for i in range(1, len(dist)+1):
    #pick the starting points for each of i friends
    testCase = list(permutations(weak, i))
    #check every possible cases of permutations of starting points
    for case in testCase:
      #set of points that the friends covers
      coverset = set([])
      #make all the sets of points that each individual friend covers
      for j in range(len(case)):
        s = []
        for k in range(dist[j]+1):
          s.append((case[j]+k)%n)
        coverset.update(s)
      #check if weakset is a partial set of coverset
      #which means all the weak points have been covered in current case
      weakset = set(weak)
      if weakset == weakset.intersection(coverset):
        return i

  return answer 
end_time = time.time() 
print("time :",end_time-start_time)