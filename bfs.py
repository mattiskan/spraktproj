#!/usr/bin/python3
import collections
from build_index import get_index
from triple import Triple
from nltk.probability import FreqDist


def bfs(start, goal, triples):
    result = []
    visited = set()
    q = collections.deque()

    for word in triples[start]:
        q.append( [word] )
    
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


def print_results(results):
    print()
    for result in results:
        for path in result:
            print(path.A(), "->", path.B(), end="")
            if path != result[-1]: print("  -->  ", end="")
        print()

    print("done")


def main():
    index = get_index("index.data")

    results = bfs('Obama', 'GAB', index)
    
    print_results(results)
    fdistAB = FreqDist([rel.A() for rel in results] + [rel.B() for rel in results])
    fdistAB.plot(10)


main()


