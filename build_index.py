import collections
import relations
import pickle
import os.path

files = [ "testData.txt", "obama.txt", "budget.txt"]

def get_index(filename):
    if os.path.isfile(filename):
        return read_index(filename)

    index = build_index()
    write_index(index, filename)
    return index



def build_index():
    print("no previous index found, building...", end="\n\n")
    index = collections.defaultdict(list)

    for file in files:
        triples = relations.parseFile(file)

        for t in triples:
            index[t.A()].append(t)
            print(t, sep="\n")

    return index


def write_index(index, output_file):
    with open(output_file, 'wb') as output:
        pickle.dump(index, output)

def read_index(filename):
    with open(filename, 'rb') as data:
        index = pickle.load(data)
        return index
