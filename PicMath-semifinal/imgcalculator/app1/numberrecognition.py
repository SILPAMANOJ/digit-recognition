import re


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


def operate():
    l = []
    k = []
    c=0
    opp1=0
    opp2=0
    oppr=0

    def addList(myList):
	    result=0
	    for i in myList:
		    result+=int(i)
	    return(result)
    def mulList(myList):
	    result=1
	    for i in myList:
		    result*=int(i)
	    return(result)
    def subList(myList):
        result=int(myList[0])
        for i in myList[1:]:
            result=result-int(i)
        return(result)
    def divList(myList):
        result=int(myList[0])
        for i in myList[1:]:
            result=result/int(i)
        return(result)

    with open("/home/silpa/Desktop/PicMath/imgcalculator/output.txt", 'r') as f:
        for line in f:
            for i in re.findall(r'\d+', line):
                l.append(i)
            for j in re.findall(r'\D+',line):
        	    if j=='\n':
        		    continue
        	    k.append(j)

    o1=int(l[0])
    o2=int(l[1])
    opp1=o1
    opp2=o2
    oppr=k[0].strip()
    x='% of'
    if oppr=='+':
	    sum=addList(l)
	    return(sum)
    elif oppr=='-':
	    sum=subList(l)
	    return(sum)
    elif oppr=='*':
	    sum=mulList(l)
	    return(sum)
    elif oppr=='/':
	    sum=divList(l)
	    return(sum)
    elif oppr=='%':
        sum=o1%o2
        return(sum)
    elif oppr=='<':
        if o1<o2:
            s=l[0]+" is less than "+l[1]
            return(s)
        else:
            s=l[0]+" is not less than "+l[1]
            return(s)
    elif oppr=='>':
        if o1>o2:
            s=l[0]+" is greater than "+l[1]
            return(s)
        else:
            s=l[0]+" is not greater than "+l[1]
            return(s)
    elif oppr==x :
        sum=o1*(o2/100)
        return(sum)




    # o1=int(l[0])
    # o2=int(l[1])
    # opp1=o1
    # opp2=o2
    # oppr=k[0].strip()
    # x='% of'
    # if oppr=='+':
    #     sum=o1+o2
    #     return(sum)

    # #print(opp1,"+",opp2,"=",sum)
    # elif oppr=='-':
    #     sum=o1-o2
    # #print(opp1,"-",opp2,"=",sum)
    #     return(sum)
    # elif oppr=='*':
    #  #print("hello")
    #     sum=o1*o2
    #  #print(opp1,"*",opp2,"=",sum)
    #     return(sum)
    # elif oppr=='/':
    #     sum=o1/o2
    #  #print(opp1,"/",opp2,"=",sum)
    #     return(sum)
    # elif oppr=='%':
    #     sum=o1%o2
    # #print(opp1,"%",opp2,"=",sum)
    #     return(sum)
    # elif oppr=='<':
    #     if o1<o2:
    #         s=l[0]+" is less than "+l[1]
    #         return(s)
    #     else:
    #         s=l[0]+" is not less than "+l[1]
    #         return(s)
            
    # elif oppr=='>':
    #     if o1>o2:
    #         s=l[0]+" is greater than "+l[1]
    #         return(s)
    #     else:
    #         s=l[0]+" is not greater than "+l[1]
    #         return(s)

    # elif oppr==x :
    #     sum=o1*(o2/100)
    #     return(sum)

# import re
# def operate():
#     c=0
#     opp1=0
#     opp2=0
#     oppr=0
#     with open("/home/silpa/Desktop/PicMath/imgcalculator/output.txt", 'r') as f:
#         for line in f:
#             #for i in re.findall(r'\d+', line):
#             for i in line:
#                 ch=ord(i)
#                 if i.isdigit():
#                     if c==0:
#                         opp1=i
#                         c+=1
#                         continue
#                     if c==1:
#                         opp2=i
#                         c+=1
#                         continue
#                 else:
#                     if (ch>=37) and (ch<=94):
#                         oppr=i
                    


#     o1=int(opp1)
#     o2=int(opp2)
#     if oppr=='+':
#         sum=o1+o2
#         #print(opp1,"+",opp2,"=",sum)
#         #return(opp1,"+",opp2,"=,sum)
#         return(sum)
#     elif oppr=='^':
#         sum=o1**o2
#         #print(opp1,"^",opp2,"= ",sum)
#         #return(opp1,"^",opp2,"= ",sum)
#         return(sum)
#     elif oppr=='-':
#         sum=o1-o2
#         #print(opp1,"-",opp2,"=",sum)
#         #return(opp1,"-",opp2,"=",sum)
#         return(sum)
#     elif oppr=='*':
#         sum=o1*o2
#         #print(opp1,"*",opp2,"=",sum)
#         #return(opp1,"*",opp2,"=",sum)
#         return(sum)
#     elif oppr=='/':
#         sum=o1/o2
#         #print(opp1,"/",opp2,"=",sum)
#         #return(opp1,"/",opp2,"=",sum)
#         return(sum)
#     elif oppr=='%':
#         sum=o1%o2
#         #print(opp1,"%",opp2,"=",sum)
#         #return(opp1,"%",opp2,"=",sum)
#         return(sum)
#     elif oppr=='<':
#         if o1<o2:
#             s=opp1+" is less than "+opp2
#             return(s)
#         else:

#             s=opp1+" is greater than "+opp2
#             return(s)
#     elif oppr=='>':
#         if o1>o2:
#             s=opp1+" is greater than "+opp2
#             return(s)
#         else:
#             s=opp1+" is less than "+opp2
#             return(s)

#     else:
#         sum=0

#print(sum)
                    
#print(oppr)
#print(opp1)
#print(opp2)
