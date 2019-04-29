import re
def operate():
    c=0
    opp1=0
    opp2=0
    oppr=0
    with open("/home/silpa/Desktop/PicMath/imgcalculator/output.txt", 'r') as f:
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
        #print(opp1,"+",opp2,"=",sum)
        #return(opp1,"+",opp2,"=,sum)
        return(sum)
    elif oppr=='^':
        sum=o1**o2
        #print(opp1,"^",opp2,"= ",sum)
        #return(opp1,"^",opp2,"= ",sum)
        return(sum)
    elif oppr=='-':
        sum=o1-o2
        #print(opp1,"-",opp2,"=",sum)
        #return(opp1,"-",opp2,"=",sum)
        return(sum)
    elif oppr=='*':
        sum=o1*o2
        #print(opp1,"*",opp2,"=",sum)
        #return(opp1,"*",opp2,"=",sum)
        return(sum)
    elif oppr=='/':
        sum=o1/o2
        #print(opp1,"/",opp2,"=",sum)
        #return(opp1,"/",opp2,"=",sum)
        return(sum)
    elif oppr=='%':
        sum=o1%o2
        #print(opp1,"%",opp2,"=",sum)
        #return(opp1,"%",opp2,"=",sum)
        return(sum)
    elif oppr=='<':
        if o1<o2:
            s=opp1+" is less than "+opp2
            return(s)
        else:

            s=opp1+" is greater than "+opp2
            return(s)
    elif oppr=='>':
        if o1>o2:
            s=opp1+" is greater than "+opp2
            return(s)
        else:
            s=opp1+" is less than "+opp2
            return(s)

    else:
        sum=0

#print(sum)
                    
#print(oppr)
#print(opp1)
#print(opp2)
