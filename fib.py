n = 34
k = 2

F = [1, 1]
for i in range(2, n):
    F.append(F[i-1] + F[i-2]*k)

print F[n-1]
