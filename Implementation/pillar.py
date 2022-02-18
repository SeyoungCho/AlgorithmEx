import time
import deepcopy

#checks if the simulated result is valid
def check(sim):
    #check from sim[0] to sim[len(sim)-1]
    return True


def solution(n, build_frame):
  answer = [[]]
  #start from build_frame[0] to build_frame[len(build_frame)-1]
  for step in build_frame:
      sim = deepcopy(answer)
      #do whatever the step does to the sim
      sim.append(step[:3])
      #check if sim is valid, if so, append i[:3] to answer
      if check(sim):
          answer.append(step[:3])
      #if sim is invalid, just ignore the current step
      else:
          pass
  
  return answer
build_frame = [
  [1,0,0,1],
  [1,1,1,1],
  [2,1,0,1],
  [2,2,1,1],
  [5,0,0,1],
  [5,1,0,1],
  [4,2,1,1],
  [3,2,1,1]
]
answer = solution(build_frame)
print(answer)
start_time = time.time() 
end_time = time.time() 
