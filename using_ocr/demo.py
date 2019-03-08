
"""f1 = open("output.txt","r") 
a=(f1.readlines(-3))
print (a[2])
for i in a[2]:
	if i in 0|1|2|3|4|5|6|7|8|9:
		print (i)"""

fname = input("Enter file name: ")
 
with open(fname, 'r') as f:
	for line in f:
		words = line.split()
		for i in words:
			for letter in i:
				if(letter.isdigit()):
					print(letter)
