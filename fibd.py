n = 88
m = 16

F = [None] * n
for i in range(n):
    F[i] = [0] * m
F[0][0] = 1
F[1][1] = 1
for i in range(2, n):
    for j in range(1, m):
        F[i][j] = F[i-1][j-1]
    F[i][0] = sum(F[i-1][1:m])

print sum(F[n-1][:])
