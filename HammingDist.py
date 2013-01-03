DNA1 = raw_input("DNA1: ")
DNA2 = raw_input("DNA2: ")
dist = 0
for a, b in zip(DNA1, DNA2):
	if a != b:
		dist += 1

print dist
