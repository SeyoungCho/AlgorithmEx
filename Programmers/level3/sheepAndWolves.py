def dfs(sheep, wolf, answer, info, edges, visited):
    if sheep > wolf: #양이 늑대보다 많을 때
        answer.append(sheep) #지금까지 찾은 양의 수를 answer 리스트에 추가
    else:
        return #양, 늑대 수가 같아지면 순회를 끝낸다.
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        if visited[parent] and not visited[child]: #부모노드는 방문했으면서 자식노드는 방문 전일 때만
            visited[child] = True #자식노드 방문처리
            if info[child] == 1: #자식노드가 늑대인 경우
                dfs(sheep, wolf+1, answer, info, edges, visited)
            else:
                dfs(sheep+1, wolf, answer, info, edges, visited)
            visited[child] = False #하나의 dfs가 끝나고 나면 자식 노드를 다시 미방문 처리(부모 입장에서 다음 edge에 대한 dfs를 수행할 때 이전에 했던 dfs의 영향을 받으면 안됨)
            
def solution(info, edges):
    answer = []
    visited = [False] * len(info)
    visited[0] = True
    dfs(1, 0, answer, info, edges, visited)
    return max(answer)