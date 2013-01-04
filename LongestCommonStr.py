infile = open("rosalind_lcs.txt")
outfile = open("rosalind_lcs_output.txt", 'w')

DNAs = []
for line in infile:
	DNAs.append(line.strip())

if len(DNAs) == 1:
	print >> outfile, DNAs[0]
	exit()

suffix = []
for k, t in enumerate(DNAs):
	for i in range(len(t)):
		suffix.append((t[i:], k))

sorted_suffix = sorted(suffix)
# print "\n".join(map(str, sorted_suffix))


def len_common_prefix(a, b):
	min_len = min(len(a), len(b))
	for i in range(min_len):
		if a[i] != b[i]:
			return (i, a[:i])
	return (min_len, a[:min_len])

common_prefix = []
for i in range(len(sorted_suffix)-1):
	common_prefix.append(len_common_prefix(sorted_suffix[i][0], sorted_suffix[i+1][0]))


from collections import deque
min_deque = deque()		# define a min queue

def push_deque(elem):
	while len(min_deque) > 0 and min_deque[-1] > elem:
		min_deque.pop()
	min_deque.append(elem)

def top_deque():
	if len(min_deque) == 0:
		raise Exception("deque is empty")
	return min_deque[0]

def pop_deque(elem):
	if elem == top_deque():
		min_deque.popleft()


DNA_in_window = 0
is_in_window = [0] * len(DNAs)

def add_to_window(i):
	global DNA_in_window
	suf, k = sorted_suffix[i]
	if is_in_window[k] == 0:
		DNA_in_window += 1
	is_in_window[k] += 1

def del_from_window(i):
	global DNA_in_window
	suf, k = sorted_suffix[i]
	is_in_window[k] -= 1
	if is_in_window[k] == 0:
		DNA_in_window -=1

start = 0
end = 0
longest_prefix = ""
add_to_window(0)
while end < len(sorted_suffix):
	if DNA_in_window < len(DNAs):
		end += 1
		if end < len(sorted_suffix):
			add_to_window(end)
			push_deque(common_prefix[end-1])
	else:
		prefix = top_deque()
		longest_prefix = max(longest_prefix, prefix)
		del_from_window(start)
		pop_deque(common_prefix[start])
		start += 1

print >> outfile, longest_prefix[1]
