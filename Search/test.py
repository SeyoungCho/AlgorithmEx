a = [(1,1,1,1), (0,0,0,0), (1,0,1,0), (-1,-1,-1,-1)]
b = (3,4,5,6)
move = [(-1, 0, -1, 0), (1, 0, 1, 0), (0, -1, 0, -1), (0, 1, 0, 1)]
tupSum=tuple(sum(elem) for elem in zip(a[0], b))
print(tupSum)
x1, y1, x2, y2 = 1, 2, 3, 4
_x1, _y1, _x2, _y2 = tuple(sum(elem) for elem in zip(move[0], (x1, y1, x2, y2)))
print(_x1, _y1, _x2, _y2)