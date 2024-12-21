#Question No 12

a=input("Enter a character")
if(a.isuppercase()):
    print("uppercase")
elif(a.islowercase()):
    print("lowercase")
elif(a.isdigit()):
    print("digit")
else:
    print("Entered char doesnt specify given criterion")
