def GCD(x, y):
    while y:
        x, y = y, x % y
    return x
def LCM(x, y):
    return (x * y) // GCD(x, y)

def solution(arr):
    answer = LCM(arr[0], arr[1])
    for num in arr[2:]:
        answer = LCM(answer, num)
    return answer