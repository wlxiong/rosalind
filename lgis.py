fin = open('rosalind_lgis.txt', 'r')
n = int(fin.readline())
s = [int(i) for i in fin.readline().split()]
inc = [(1, None) for i in range(len(s))]
dec = [(1, None) for i in range(len(s))]
for i in range(1, len(s)):
    for j in range(i):
        if s[j] < s[i] and (inc[i][1] is None or inc[j][0] + 1 > inc[i][0]):
            inc[i] = inc[j][0] + 1, j
        if s[j] > s[i] and (dec[i][1] is None or dec[j][0] + 1 > dec[i][0]):
            dec[i] = dec[j][0] + 1, j
ii = 0
for i in range(len(s)):
    if inc[ii][0] < inc[i][0]:
        ii = i
di = 0
for i in range(len(s)):
    if dec[di][0] < dec[i][0]:
        di = i

def print_seq(seq, n):
    if n is None:
        return
    # print seq[n][1]
    print_seq(seq, seq[n][1])
    print s[n],

# print inc, ii
print_seq(inc, ii)
print
# print dec, di
print_seq(dec, di)
