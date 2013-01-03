DNAstr = raw_input("DNA: ")
DNAreverse = DNAstr[::-1]
DNA2 = ""
for i in range(len(DNAreverse)):
    if DNAreverse[i] == 'A':
        DNA2 += 'T'
    elif DNAreverse[i] == 'G':
        DNA2 += 'C'
    elif DNAreverse[i] == 'C':
        DNA2 += 'G'
    elif DNAreverse[i] == 'T':
        DNA2 += 'A'

print DNA2
