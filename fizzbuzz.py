#Question No 8

n=int(input("Enter a number"))
if(n%3==0 and n%5==0):
    print("FizzBuzz")
elif(n%3!=0 and n%5==0):
    print("Buzz")
elif(n%3==0 and n%5!=0):
    print("Fizz")
else:
     print(f"{n}")
