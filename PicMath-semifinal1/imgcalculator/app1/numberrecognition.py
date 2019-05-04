import re
import math

def operate():
    l = []
    k = []
    c=0
    opp1=0
    opp2=0
    oppr=0
    m = ""
    def solve(calculation):
        precedence = {"^": 4, "/": 3, "÷": 3, "*": 2, "x": 2, "X":2, "+": 1, "-": 1}
        bodmasIndex = []
        calc = ""
        
        for i in range(len(calculation)):
            calc += str(calculation[i])
            if calculation[i] in precedence:
                if len(bodmasIndex) == 0:  # starts off the bodmasIndex list with a value (this is only executed once)
                    bodmasIndex.append(i)
                else:
                    for x in range(len(bodmasIndex)):  # for each of the values stored in bodmasIndex
                        if precedence[calculation[i]] < precedence[calculation[bodmasIndex[-1]]]:
                            bodmasIndex.append(i)
                            break
                        elif precedence[calculation[i]] > precedence[calculation[bodmasIndex[x]]]:
                            bodmasIndex.insert(x, i)  # insert the index value
                            break
                        elif precedence[calculation[i]] == precedence[calculation[bodmasIndex[x]]]:
                            if calculation[i] == "+" or calculation[i] == "-":
                                bodmasIndex.append(i)
                                break
                            else:
                                bodmasIndex.insert(x + 1, i)
                                break
                        else:
                            continue

        while len(bodmasIndex) != 0:
            if calculation[bodmasIndex[0]] == '^':
                currentCalculation = calculation[bodmasIndex[0] - 1] ** calculation[bodmasIndex[0] + 1]
            elif calculation[bodmasIndex[0]] == '/':
                currentCalculation = calculation[bodmasIndex[0] - 1] / calculation[bodmasIndex[0] + 1]
            elif calculation[bodmasIndex[0]] == '*' or calculation[bodmasIndex[0]]=='x' or calculation[bodmasIndex[0]]=='X':
                currentCalculation = calculation[bodmasIndex[0] - 1] * calculation[bodmasIndex[0] + 1]
            elif calculation[bodmasIndex[0]] == '+':
                currentCalculation = calculation[bodmasIndex[0] - 1] + calculation[bodmasIndex[0] + 1]
            else:
                currentCalculation = calculation[bodmasIndex[0] - 1] - calculation[bodmasIndex[0] + 1]

            calculation[bodmasIndex[0]-1] = currentCalculation
            calculation.pop(bodmasIndex[0]+1)
            calculation.pop(bodmasIndex[0])

            for i in range(len(bodmasIndex)):
                if bodmasIndex[i] > bodmasIndex[0]:
                    bodmasIndex.insert(i, bodmasIndex[i] - 2)
                    bodmasIndex.pop(i + 1)

            bodmasIndex.pop(0)

        return calculation[0]


    def bracketSolver(calculation):
        startBracketIndex = []
        endBracketIndex = []
        bracketPairs = {}

        for i in range(len(calculation)):
            if calculation[i] == '(':
                startBracketIndex.append(i)
            elif calculation[i] == ')':
                endBracketIndex.append(i)

        for i in range(len(startBracketIndex) - 1, -1, -1):
            for x in range(len(endBracketIndex)):
                if endBracketIndex[x] < startBracketIndex[i]:
                    continue
                elif endBracketIndex[x] in bracketPairs.values():
                    continue
                else:
                    bracketPairs[startBracketIndex[i]] = endBracketIndex[x]
                    break
            break
        if len(bracketPairs) != 0:
            return bracketPairs


    def calculator(calculation):
        brackets = bracketSolver(calculation)
        ans = []

        if brackets is None:
            return solve(calculation)
        else:
            s = list(brackets.keys())[0]
            e = brackets[s]
            ans.append(solve(calculation[s + 1:e]))
            calculation = calculation[:s] + ans + calculation[e + 1:]
            print("calculation")
            return calculator(calculation)


    def intChecker(value):
        try:
            int(value)
            return True
        except ValueError:
            return False


    def calcInput(expression):
        calcArray = []
    #calculation = input('Enter your calculation: ')
        calculation=expression
        num = ""

        for i in range(len(calculation)):
            if intChecker(calculation[i]):
                num = num + calculation[i]
                if i == len(calculation)-1:
                    calcArray.append(int(num))
            else:
                if num == "":
                    calcArray.append(calculation[i])
                else:
                    calcArray.append(int(num))
                    calcArray.append(calculation[i])
                    num = ""

        return calculator(calcArray)


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


    def factorial(num):
    	if num == 1:
        	return num
    	else:
        	return num * factorial(num - 1)


    with open("/home/silpa/Desktop/PicMath/imgcalculator/output.txt", 'r') as f:
        for line in f:
            for i in re.findall(r'\d+', line):
                l.append(i)
            for j in re.findall(r'\D+',line):
                if j=='\n':
                    continue
                k.append(j)



# fname = input("Enter file name: ")
    with open("/home/silpa/Desktop/PicMath/imgcalculator/output.txt",'r') as nf:
        for i in nf:
            m+=i

 
# with open(fname, 'r') as f:
#     for line in f:
#         for i in re.findall(r'\d+', line):
#             l.append(i)
#         for j in re.findall(r'\D+',line):
#         	if j=='\n':
#         		continue
#         	k.append(j)

    # print(len(k))
    # print(len(l))
    # print(len(set(k)))
    print(k)
    print(l)
    #print(set(k))

    if len(k)==1 and len(l)==1:
	    oppr=k[0].strip()
	    a=int(l[0])
	    if oppr=='V':
		    sum=math.sqrt(a)
		    return(int(sum))
	    elif oppr=='!':
		    sum=factorial(a)
		    return(sum)
	    elif oppr=='H':
		    sum=a*math.pi
		    return(sum)
	    elif oppr=='Sin' or oppr=='sin':
		    sum=math.sin(a)
		    return(sum)
	    elif oppr=='Cos' or oppr=='cos':
		    sum=math.cos(a)
		    return(sum)
	    elif oppr=='Tan' or oppr=='cos':
		    sum=math.tan(a)
		    return(sum)
    
    elif len(k)==1:
        oppr=k[0].strip()
        x='% of'
        s=""
        o1=int(l[0])
        o2=int(l[1])
        oppr=k[0].strip()
        if oppr=='%':
            sum=o1%o2
            return(sum)
            #return(o1," % ",o2," = ",sum)
        elif oppr=='<':
            if o1<o2:
                s=l[0]+" < "+l[1]+" is true "
                return(s)
                #return(o1,"<",o2,"is true")
            else:
                s=l[0]+" < "+l[1]+" is false"
                return(s)
                #return(o1,"<",o2," is false")
        elif oppr=='>':
            if o1>o2:
                s=l[0]+" > "+l[1]+" is true"
                return(s)
                #return(o1,">",o2,"is true")
            else:
                s=l[0]+" > "+l[1]+" is false"
                return(s)
                #return(o1,">",o2," is false")
        elif oppr==x :
            sum=o1*(o2/100)
            return(sum)
        elif oppr=='A':
                sum=math.pow(o1,o2)
                return(sum)
        
        
        elif oppr=='+':
            sum=addList(l)
            return(sum)
        elif oppr=='-':
            sum=subList(l)
            return(sum)
        elif oppr=='*' or oppr=='x' or oppr=='X':
            sum=mulList(l)
            return(sum)
        elif oppr=='/' or oppr=='÷':
            sum=divList(l)
            return(sum)
        else:
            return(0)
    elif len(set(k))==1:
        oppr=k[0].strip()
        if oppr=='+':
            sum=addList(l)
            return(sum)
        elif oppr=='-':
            sum=subList(l)
            return(sum)
        elif oppr=='*' or oppr=='x' or oppr=='X':
            sum=mulList(l)
            return(sum)
        elif oppr=='/' or oppr=='÷':
            sum=divList(l)
            return(sum)
    else:   
        print("hello")
        ans = calcInput(m)
        return(ans)









#second code#

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





#third code #



# def operate():
#     l = []
#     k = []
#     c=0
#     opp1=0
#     opp2=0
#     oppr=0

#     def addList(myList):
# 	    result=0
# 	    for i in myList:
# 		    result+=int(i)
# 	    return(result)
#     def mulList(myList):
# 	    result=1
# 	    for i in myList:
# 		    result*=int(i)
# 	    return(result)
#     def subList(myList):
#         result=int(myList[0])
#         for i in myList[1:]:
#             result=result-int(i)
#         return(result)
#     def divList(myList):
#         result=int(myList[0])
#         for i in myList[1:]:
#             result=result/int(i)
#         return(result)

#     with open("/home/silpa/Desktop/PicMath/imgcalculator/output.txt", 'r') as f:
#         for line in f:
#             for i in re.findall(r'\d+', line):
#                 l.append(i)
#             for j in re.findall(r'\D+',line):
#         	    if j=='\n':
#         		    continue
#         	    k.append(j)

#     o1=int(l[0])
#     o2=int(l[1])
#     opp1=o1
#     opp2=o2
#     oppr=k[0].strip()
#     x='% of'
#     if oppr=='+':
# 	    sum=addList(l)
# 	    return(sum)
#     elif oppr=='-':
# 	    sum=subList(l)
# 	    return(sum)
#     elif oppr=='*':
# 	    sum=mulList(l)
# 	    return(sum)
#     elif oppr=='/':
# 	    sum=divList(l)
# 	    return(sum)
#     elif oppr=='%':
#         sum=o1%o2
#         return(sum)
#     elif oppr=='<':
#         if o1<o2:
#             s=l[0]+" is less than "+l[1]
#             return(s)
#         else:
#             s=l[0]+" is not less than "+l[1]
#             return(s)
#     elif oppr=='>':
#         if o1>o2:
#             s=l[0]+" is greater than "+l[1]
#             return(s)
#         else:
#             s=l[0]+" is not greater than "+l[1]
#             return(s)
#     elif oppr==x :
#         sum=o1*(o2/100)
#         return(sum)









# first code#


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
