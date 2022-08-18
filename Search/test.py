N = int(input())
words = []
count = 0
for _ in range(N):
    words.append(input())
for word in words:
    stack = []
    for i in range(len(word)):
        if not stack:
            stack.append(word[i])
        else:
            a = stack.pop()
            if a != word[i]:
                stack.append(a)
                stack.append(word[i])
    if not stack:
        count += 1
print(count)
		