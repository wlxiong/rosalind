infile = open("longest_common_substr.txt")
outfile = open("longest_common_substr_out.txt", 'w')

DNAs = []
for line in infile:
	DNAs.append(line.strip())

suffix = []
for k, t in enumerate(DNAs):
	for i in range(len(t)):
		suffix.append((t[i:], k))

sorted_suffix = sorted(suffix)
print "\n".join(map(str, sorted_suffix))

def len_common_prefix(a, b):
	for i in range(min(len(a), len(b))):
		if a[i] != b[i]:
			return i
	return min(len(a), len(b))

len_prefix = []
for i in range(len(sorted_suffix)-1):
	len_prefix = len_common_prefix(sorted_suffix[i], sorted_suffix[i+1])
	

in_window = [0] * len(DNAs)
no_all = 0
start = 0
end = 0
while end < len(sorted_suffix):
	if no_all < len(DNAs):
		end += 1
		suf, k = sorted_suffix[end]
		if in_window[k] == 0:
			no_all += 1
		in_window[k] += 1
