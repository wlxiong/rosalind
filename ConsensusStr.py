infile = open("rosalind_cons (2).txt")
outfile = open("rosalind_cons_output.txt", 'w') 

profile_matrix = {'A': {}, 'C': {}, 'G': {}, 'T': {}}
for DNA in infile:
	DNA = DNA.strip()
	for i in range(len(DNA)):
		profile_matrix[DNA[i]].setdefault(i, 0)
		profile_matrix[DNA[i]][i]  += 1

consensus_string = ""
for i in range(len(DNA)):
	n, cc = max([(profile_matrix[c].get(i, 0), c) for c in profile_matrix])
	consensus_string += cc

print >> outfile, consensus_string
for (c, v) in sorted(profile_matrix.items()):
	print >> outfile, "%c:" % c,
	# print v
	for i in range(len(DNA)):
		print >> outfile, v.get(i, 0),
	print >> outfile
