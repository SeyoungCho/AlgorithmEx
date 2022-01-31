#Simple dijkstra algorithm O(V^2)
import sys
input = sys.stdin.readline
INF = int(1e9) #Infinity

#no. of nodes and edges
n, m = map(int, input().split())
#start node number
start = int(input())
#graph information 
graph = [[] for i in range(n+1)]
#visited check list
visited = [False] * (n+1)
#shortest distance table
distance = [INF] * (n+1)

#input all edge info
for _ in range(m):
  a, b, c = map(int, input().split())
  #means nodes a and b are 'c' cost apart
  graph[a].append((b,c))

#returns the nearest node number among the unvisited nodes
def get_smallest_node():
  min_value = INF
  index = 0 #the index of the nearest node
  for i in range(1, n + 1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  #initialize for the start node
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  #iterate for all the nodes except for the start node
  for i in range(n-1):
    #visit the nearest node 
    now = get_smallest_node()
    visited[now] = True
    #check the nodes that are connected to the current node
    for j in graph[now]:
      cost = distance[now] + j[i]
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if distance == INF:
    print("Infinity")
  else:
    print(distance[i])
