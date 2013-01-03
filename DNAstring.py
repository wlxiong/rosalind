DNAstr = raw_input("DNA string: ")
nA = 0
nG = 0
nC = 0
nT = 0
for c in DNAstr:
    if c == 'A':
        nA += 1
    elif c == 'G':
        nG += 1
    elif c == 'C':
        nC += 1
    elif c == 'T':
        nT += 1

print nA, nC, nG, nT
