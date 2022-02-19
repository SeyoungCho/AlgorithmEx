from itertools import combinations

arr = [(1,2), (3,4), (4,5), (1,4), (4,3)]
removeList = list(combinations(range(len(arr)), 2))
print(removeList)