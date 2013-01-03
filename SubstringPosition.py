string = raw_input("string: ")
pattern = raw_input("pattern: ")

position = 0
while position >= 0:
	position = string.find(pattern, position+1)
	if position >= 0:
		print position+1,
