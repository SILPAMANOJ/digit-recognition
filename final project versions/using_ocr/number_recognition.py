import re
l = []
fname = input("Enter file name: ")
 
with open(fname, 'r') as f:
    for line in f:
        for i in re.findall(r'\d+', line):
            l.append(i)

print(l)

