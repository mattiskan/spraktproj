import collections
import relations

files = [ "testData.txt", "obama.txt", "budget.txt"]


def build_index(triples):
    index = collections.defaultdict(list)

    for t in triples:
        index[t.A()].append(t)

    return index



def get_index(filename):
    index = collections.defaultdict(list)

    for file in files:
        triples = relations.parseFile(file)
        found = build_index(triples)
        print("file:", file)
        for k,v in found.items():
            print(*v, sep="\n")
            index[k].extend(v)
            
    return index
