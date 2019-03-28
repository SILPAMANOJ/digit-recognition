import re
c=0
fname = input("Enter file name: ")
 
with open(fname, 'r') as f:
    for line in f:
        #for i in re.findall(r'\d+', line):
        for i in line:
            ch=ord(i)
            if i.isdigit():
                if c==0:
                    opp1=i
                    c+=1
                    continue
                if c==1:
                    opp2=i
                    c+=1
                    continue
            else:
                if (ch>=42) and (ch<=47):
                    oppr=i


o1=int(opp1)
o2=int(opp2)
if oppr=='+':
    sum=o1+o2
elif oppr=='-':
    sum=o1-o2
elif oppr=='*':
    sum=o1*o2
elif oppr=='/':
    sum=o1/o2
else:
    sum=0
print(opp1 "+" opp2 "=", sum)
#print(sum)
                    
#print(oppr)
#print(opp1)
#print(opp2)
