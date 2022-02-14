import time
start_time = time.time()

def solution(s):
  answer = len(s)
  for i in range(1, len(s)//2 + 1):
    j = 1
    cur = s[0:j*i]
    total_len = len(cur)
    cnt = 1
    #continue till the end of the string
    while True:
      if (j+1) * i > len(s):
        if cnt > 1:
          total_len += 1
        break
      nex = s[j*i:(j+1)*i]
      #if it matches the next string
      if cur == nex:
        cnt += 1
      #if it does not match
      else:
        #add 1 to total length if there are more than one repeated
        if cnt > 1:
          total_len += 1
          #cnt goes back to 1
          cnt = 1
        cur = nex
        total_len += len(cur)
      j += 1      
    total_len += (len(s) - j*i)
    if total_len < answer:
      answer = total_len
  return answer

result = solution("aaaaaaaabcbca")
print(result)
end_time = time.time() 
print("time :",end_time - start_time)