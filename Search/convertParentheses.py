import time
start_time = time.time()
#returns true if the string is balanced
def isBalanced(p):
  return p.count('(') == p.count(')')
      
#returns true if the string is correctly balanced
def isCorrectlyBalanced(expr):
  stack = []
  # Traversing the Expression
  for char in expr:
    if char in ["("]:
      # Push the element in the stack
      stack.append(char)
    else:
      # IF current character is not opening
      # bracket, then it must be closing.
      # So stack cannot be empty at this point.
      if not stack:
        return False
      current_char = stack.pop()
      if current_char == '(':
        if char != ")":
          return False
  # Check Empty Stack
  if stack:
      return False
  return True

#takes in a string and returns its correctly formatted form
def solution(p):
  #if the string is already correct or an empty string
  if isCorrectlyBalanced(p):
    return p
  #divide the string into two parts, u and v
  u = ""
  v = ""
  if len(p) == 2:
    u = p[:2]
    v = ""
  else:
    for i in range(2, len(p)+1):
      if isBalanced(p[:i]):
        u = p[:i]
        v = p[i:]
        break
  result = ""
  #return u + result
  if isCorrectlyBalanced(u):
    result = solution(v)
    return u + result
  #if u is not correctly balanced
  else:
    result += '(' + solution(v) + ')'
    u = u[1:len(u)-1]
    tmp = ""
    for char in u:
      if char == '(':
        tmp += ')'
      else:
        tmp += '('
    result += tmp
    return result

p = ")("
print(solution(p))
end_time = time.time() 
print("time :",end_time - start_time)