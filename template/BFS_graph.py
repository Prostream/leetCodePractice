from collections import deque

def BFS(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        count = len(queue)
        for i in range(count):
            cur = queue.popleft()
            if cur not in visited:
                visited.add(cur)
                queue.append(cur)
    return