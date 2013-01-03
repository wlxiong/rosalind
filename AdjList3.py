fasta = open('rosalind_grph (1).txt')
output = open('rosalind_grph_output.txt', 'w')

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

DNAs = read_fasta(fasta)
# print DNAs

k = 3
prefix_name = {}
suffix_name = {}
for name, DNA in DNAs.items():
	prefix = DNA[:k]
	if prefix in prefix_name:
		prefix_name[prefix].append(name)
	else:
		prefix_name[prefix] = [name]
	suffix = DNA[-k:]
	if suffix in suffix_name:
		suffix_name[suffix].append(name)
	else:
		suffix_name[suffix] = [name]

def print_adjlist(start_nodes, end_nodes):
	# print start_nodes
	# print end_nodes
	for start in start_nodes:
		for end in end_nodes:
			if start != end:
				print >> output, start, end

sorted_prefix = sorted(prefix_name.items())
sorted_suffix = sorted(suffix_name.items())
# print sorted_prefix
# print sorted_suffix

i = 0
j = 0
while i < len(sorted_prefix) and j < len(sorted_suffix):
	# print sorted_prefix[i][0], sorted_suffix[j][0]
	if sorted_prefix[i][0] == sorted_suffix[j][0]:
		print_adjlist(sorted_suffix[j][1], sorted_prefix[i][1])
		i +=1
		j + 1
	elif sorted_prefix[i][0] < sorted_suffix[j][0]:
		i += 1
	else:
		j += 1
