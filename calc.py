print ("Python Calculator ")
a=int(input("Enter the first integer:-"))
oper=input("What calculation do you want to perform(+,-,*,/,//,%):-")
b=int(input("Enter the second integer:-"))
answer=0
if oper=="+":
    answer=a+b
elif oper=="-":
    answer=a-b
elif oper=="*":
    answer=a*b
elif oper=="/":
    answer=a/b
elif oper=="//":
    answer=a//b
elif oper=="%":
    answer=a%b
else :
    print("invalid input") 
print ('the answer of your problem is:-' , answer)