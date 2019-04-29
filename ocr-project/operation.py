import re
l = []
k = []

def addList(myList):
	#print(myList)
	result=0
	for i in myList:
		result+=int(i)
	return(result)
def mulList(myList):
	#print(myList)
	result=1
	for i in myList:
		result*=int(i)
	return(result)
def subList(myList):
	#print(myList)
	result=int(myList[0])
	for i in myList[1:]:
		result=result-int(i)
	return(result)
def divList(myList):
	#print(myList)
	result=int(myList[0])
	for i in myList[1:]:
		result=result/int(i)
	return(result)

fname = input("Enter file name: ")
 
with open(fname, 'r') as f:
    for line in f:
        for i in re.findall(r'\d+', line):
            l.append(i)
        for j in re.findall(r'\D+',line):
        	if j=='\n':
        		continue
        	k.append(j)

# sum=addList(l)
# print(sum)

oppr=k[0].strip()
x='% of'
if oppr=='+':
	sum=addList(l)
	print(sum)
elif oppr=='-':
	sum=subList(l)
	print(sum)
elif oppr=='*':
	sum=mulList(l)
	print(sum)
elif oppr=='/':
	sum=divList(l)
	print(sum)
# elif oppr=='%':
    
#     sum=o1%o2
#     print(opp1,"%",opp2,"=",sum)
# elif oppr=='<':
#     if o1<o2:
#         print(opp1,"<",opp2,"is true")
#     else:
#         print(opp1,"<",opp2," is false")
# elif oppr=='>':
#     if o1>o2:
#         print(opp1,">",opp2,"is true")
#     else:
#         print(opp1,">",opp2," is false")

# elif oppr==x :
#     sum=o1*(o2/100)
#     print(sum)


