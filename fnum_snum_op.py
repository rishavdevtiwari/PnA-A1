#Question No 6

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
o=input("Enter Operator:")
if(o=="+"):
    c=a+b
    print(f"Your answer is: {c}")
elif(o=="-"):
    c=a-b
    print(f"Your answer is: {c}")
elif(o=="*"):
    c=a*b
    print(f"Your answer is: {c}")
elif(o=="/"):
    c=a/b
    print(f"Your answer is {c}")
else:
    print("Invalid Operator")
