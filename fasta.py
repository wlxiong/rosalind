def read_fasta(fasta):
	DNAs = {}
	for line in fasta:
		if line[0] == '>':
			name = line[1:].strip()
		else:
			DNA = ''.join(line.split())
			if name in DNAs:
				DNAs[name] += DNA
			else:
				DNAs[name] = DNA
	return DNAs
