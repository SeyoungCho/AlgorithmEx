import math
from collections import deque
Board = []
Allcard = {}
Allremoved = 1 
MinCnt = math.inf
D = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(removed, src, dst):
    global D
    visited = [[False for _ in range(4)] for _ in range(4)]
    q = deque([src])
    while q:
        curr = q.popleft()
        if curr[0] == dst[0] and curr[1] == dst[1]:
            return curr[2]
        for i in range(4):
            nr = curr[0] + D[i][0]
            nc = curr[1] + D[i][1]
            if nr < 0 or nr > 3 or nc < 0 or nc > 3:
                continue
            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc, curr[2]+1))
            # 2칸 더 이동 가능여부 체크
            for j in range(2):
                if (removed & 1 << Board[nr][nc]) == 0: # 이동방향 상 카드가 존재하는 경우
                    break
                if nr + D[i][0] < 0 or nr + D[i][0] > 3 \
                or nc + D[i][1] < 0 or nc + D[i][1] > 3:
                    break
                # 더 이동 가능한 경우
                nr += D[i][0]
                nc += D[i][1]
            # 더 이동한 경우에만 새로운 위치를 큐에 push
            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc, curr[2]+1))                    
                

# cnt: 지금까지 수행한 조작 횟수
# removed: 지금까지 제거한 카트 종류들을 비트형태로 받음
# src : 현재 커서의 위치
def permutate(cnt, removed, src):
    global MinCnt
    # 탐색 진행할 때 cnt가 MinCnt보다 커지면 탐색 종료
    if cnt > MinCnt:
        return
    if removed == Allremoved: # 모든 카드를 제거했다면 재귀 종료
        MinCnt = min(MinCnt, cnt)
        return 
    for num, card in Allcard.items(): # num: key, card: value
        if removed & 1 << num: # 카드가 이미 제거되었으면 스킵
            continue
        # num 카드를 제거하기 위한 조작 횟수 1 -> 2
        one = bfs(removed, src, card[0]) + bfs(removed, card[0], card[1]) + 2 # src에서 첫 번째 카드까지 bfs로 최단경로 탐색, 첫 번째 카드부터 두번째 카드까지 최단경로 탐색, 엔터키 2번 더하기
        # num 카드를 제거하기 위한 조작 횟수 2 -> 1
        two = bfs(removed, src, card[1]) + bfs(removed, card[1], card[0]) + 2
        permutate(cnt+one, removed | 1 << num, card[1])
        permutate(cnt+two, removed | 1 << num, card[0])
        
def solution(board, r, c):
    global Board, Allcard, Allremoved
    Board = board
    # dictionary 만들기 
    # 예: Allcard[1] : [(1, 2, 2), (3, 3, 3)]
    # 1번 카드는 (1, 2), (3, 3)에 있고 현 위치에서 각 카드로 가는 조작 횟수는 2, 3번 이다.
    for i in range(4):
        for j in range(4):
            num = Board[i][j]
            if num != 0:
                Allremoved |= 1 << num #1을 카드 종류숫자만큼 left shift : 예: num이 1이면 1번째 비트가 1로 켜짐
                if num in Allcard:
                    Allcard[num].append((i, j, 0)) #(row, col, 조작 횟수)
                else:
                    Allcard[num] = [(i, j, 0)]
    permutate(0, 1, (r, c, 0))
    return MinCnt