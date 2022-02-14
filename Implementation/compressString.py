import time
start_time = time.time()

def solution(s):
  answer = len(s)
  for i in range(1, len(s)//2):
    total_length = 0
    partial_length = i
    j = 1
    cnt = 1
    cur = s[0:i]
    while (j+1)*i <= len(s):
      if cur == s[j*i:(j+1)*i]:
        cnt += 1
        j += 1
        if partial_length == i:
          partial_length += 1
          total_length += partial_length
      else:
        if cnt > 1:
          partial_length += 1
        total_length += partial_length
        partial_length = i
        cnt = 1
        cur = s[j*i:(j+1)*i]
        j += 1
    if total_length < answer:
      answer = total_length
  return answer

result = solution("aabbaa")
print(result)
end_time = time.time() 
print("time :",end_time - start_time)