#!/usr/bin/python3
import collections
import relations
from triple import Triple


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



def build_index(triples):
    index = collections.defaultdict(list)

    for t in triples:
        index[t.A()].append(t)

    return index


def print_results(results):
    print()
    for result in results:
        for path in result:
            print(path.A(), "->", path.B(), end="")
            if path != result[-1]: print("  -->  ", end="")
        print()

    print("done")


def main():
    files = [ "testData.txt", "obama.txt", "budget.txt"]

    index = collections.defaultdict(list)
    for file in files:
        triples = relations.parseFile(file)
        found = build_index(triples)
        print("file:", file)
        for k,v in found.items():
            print(*v, sep="\n")
            index[k].extend(v)

    results = bfs('Obama', 'GAB', index)
    
    print_results(results)



def test():

    index = collections.defaultdict(list)
    for i in range(3):
        index2 = collections.defaultdict(list)
        index2['a'].append('1')
        index2['a'].append('2')

        for k,v in index2.items():
            index[k].extend(v)

    print(index['a'])



main()


