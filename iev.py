genotypes = [
    ('AA', 'AA', 1.0),
    ('AA', 'Aa', 1.0),
    ('AA', 'aa', 1.0),
    ('Aa', 'Aa', 0.75),
    ('Aa', 'aa', 0.5),
    ('aa', 'aa', 0.0)
]

couples = [17994, 17099, 16306, 18894, 16147, 16189]
E = 0.0
for c, t in zip(couples, genotypes):
    _, _, p = t
    E += c * 2.0 * p

print E
