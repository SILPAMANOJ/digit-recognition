fname = input("Enter file name: ")
 
with open(fname, 'r') as f:
	for line in f:
		words = line.split()
		for i in words:
			for letter in i:
				if(letter.isdigit()):
					print(letter)
				if ord(letter)==43:
					print(letter)
				#if ord(letter)==47:
				#	print(letter)
