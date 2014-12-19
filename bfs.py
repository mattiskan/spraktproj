#!/usr/bin/python3
import collections
import relations
from triple import Triple


def bfs(start, goal, triples):
    result = []
    q = collections.deque()
    q.append(triples[start])

    visited = set()
    
    while len(q) > 0:
        path = q.popleft()
        curr = path[-1].B()

        if curr in visited:
            continue

        if(path[-1].B() == goal):
            result.append(path)
            continue

        visited.add(curr)
        
        for neighbour in triples[curr]:
            if not neighbour.B() in visited:
                nextp = path + [neighbour]
                q.append(nextp)

    return result



def build_index(triples):
    index = collections.defaultdict(list)

    for t in triples:
        index[t.A()].append(t)

    return index



def main():
    triples = relations.parseFile("testData.txt")
    
    index = build_index(triples)

    results = bfs('Ben', 'Jonathan', index)

    for result in results:
        for path in result:
            print(path, end="")
            if path != result[-1]: print(" -> ", end="")
        print()


main()
    



