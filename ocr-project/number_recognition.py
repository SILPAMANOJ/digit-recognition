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
                if (ch>=37) and (ch<=94):
                    oppr=i


o1=int(opp1)
o2=int(opp2)
if oppr=='+':
    sum=o1+o2
    print(opp1,"+",opp2,"=",sum)
elif oppr=='**':
    sum=o1**o2
    print(opp1,"^",opp2,"= ",sum)
elif oppr=='-':
    sum=o1-o2
    print(opp1,"-",opp2,"=",sum)
elif oppr=='*':
    sum=o1*o2
    print(opp1,"*",opp2,"=",sum)
elif oppr=='/':
    sum=o1/o2
    print(opp1,"/",opp2,"=",sum)
elif oppr=='%':
    sum=o1%o2
    print(opp1,"%",opp2,"=",sum)
elif oppr=='<':
    if o1<o2:
        print(opp1,"<",opp2,"is true")
    else:
        print(opp1,"<",opp2," is false")
elif oppr=='>':
    if o1>o2:
        print(opp1,">",opp2,"is true")
    else:
        print(opp1,">",opp2," is false")

else:
    sum=0

#print(sum)
                    
#print(oppr)
#print(opp1)
#print(opp2)
