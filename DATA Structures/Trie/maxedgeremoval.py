from typing import List

def dfs(u: int, visit: List[bool]) -> int:
    global res, g
    visit[u] = True
    currComponentNode = 0
    for i in range(len(g[u])):
        v = g[u][i]
        if not visit[v]:
            subtreeNodeCount = dfs(v, visit)
            if subtreeNodeCount%2 == 0:
                res += 1
            else:
                currComponentNode += subtreeNodeCount
    return currComponentNode+1

def maxEdgeRemovalToMakeForestEven(N: int) -> int:
    visit = [False for _ in range(N + 1)]
    dfs(0, visit)
    return res

def addEdge(u:int, v:int) -> None:
    global g
    g[u].append(v)
    g[v].append(u)

if __name__ == "__main__": 
    res = 0
    edges = [ [ 0, 2 ], [ 0, 1 ],
              [ 0, 4 ], [ 2, 3 ],
              [ 4, 5 ], [ 5, 6 ],
              [ 5, 7 ] ]
    N = len(edges)
    g = [[] for _ in range(N + 1)]
    for i in range(N):
        addEdge(edges[i][0], edges[i][1])
    print(maxEdgeRemovalToMakeForestEven(N))