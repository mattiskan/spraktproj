#!/usr/bin/python3
import collections



def bfs(start, goal, data):
    result = []
    q = collections.deque([[start]])

    visited = set()

    while len(q) > 0:
        path = q.popleft()
        curr = path[-1]

        if curr in visited:
            continue

        if(curr == goal):
            result.append(path)
            continue

        visited.add(curr)
        
        for neighbour in data[curr]:
            if not neighbour in visited:
                nextp = path + [neighbour]
                q.append(nextp)

    print("found", result)
    return result

        
data = {
    0: {1,6,7},
    1: {4,7},
    2: {5},
    3: {1,2,5},
    4: {1,3,5,7},
    5: {3},
    6: {},
    7: {3,4,6}
}

bfs( 0, 5, data)
bfs( 6, 5, data)
