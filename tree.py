fin = open('rosalind_tree.txt', 'r')
n = int(fin.readline())
nodes = set()
edges = set()
for line in fin:
    a, b = line.split()
    a, b = int(a), int(b)
    edges.add((a, b))
    nodes.add(a)
    nodes.add(b)
print n - 1 - len(edges)
