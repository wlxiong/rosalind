kmn = raw_input("k, m, n: ")
kmn_list = kmn.split()
k, m, n = tuple(map(int, kmn_list))
s = k + m + n
C = lambda b: b * (b - 1) / 2
p = C(k) + k * m + C(m) * .75 + k * n + m * n * .5
p /= C(s)
print p
