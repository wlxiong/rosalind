def perm(A):
	if len(A) == 1:
		return [A]
	AB = []
	for i in A:
		AA = list(A)
		AA.remove(i)
		B = perm(AA)
		for j in B:
			AB.append([i] + j)
	return AB

output = open('permutation.txt', 'w')
PP = perm(list(range(1,8)))
print >> output, len(PP)
for p in PP:
	print >> output, ' '.join([str(i) for i in p])
