fasta = open('rosalind_gc.txt')
DNAstr = {}

for line in fasta:
	if line[0] == '>':
		name = line[1:].strip()
	else:
		DNA = ''.join(line.split())
		if name in DNAstr:
			DNAstr[name] += DNA
		else:
			DNAstr[name] = DNA

def GCpercent(DNA):
	GCcount = 0
	for c in DNA:
		if c == 'C' or c == 'G':
			GCcount += 1
	return float(GCcount) / len(DNA)

DNAperc = {}
GCmax = float('-inf')
GCname = ""
for name, DNA in DNAstr.items():
	DNAperc[name] = GCpercent(DNA)
	if DNAperc[name] > GCmax:
		GCname = name
		GCmax = DNAperc[name]

print GCname
print "%.6f%%" % (GCmax*100.0)
