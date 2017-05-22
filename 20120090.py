def DFS(graph, start, visited):
    stack = [start]
    result = []
    cur_parent = -1
    while stack:
        current = stack.pop()
        if current != start:
            cur_parent = stack[-1]
        if not visited[current]:
            visited[current] = True
            result.append(current)

        cns = [nei for nei in graph[current] if nei != cur_parent and not visited[nei]]
        if not cns:
            continue
        
        cn = cns.pop(0)
        stack.append(current)
        stack.append(cn)
    
    return result

def BFS(graph, start, visited):
    result = []
    q = [start]
    visited[start] = True
    while len(q) > 0:
        current = q.pop(0)
        result.append(current)        
        for v in graph[current]:
            if visited[v] == False:
                visited[v] = True
                q.append(v)

    return result

n, k, v = (int(x) for x in input().split())

graph = list([] for i in range(n+1))

for i in range(k) :
    a, b = (int(x) for x in input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1) :
    graph[i].sort()

visited = [False for x in range(n+1)]
print(*DFS(graph, v, visited))
visited = [False for x in range(n+1)]
print(*BFS(graph, v, visited ))