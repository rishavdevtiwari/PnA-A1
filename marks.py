#Question No 4

m=int(input("Enter marks"))
if(m>80):
    print("A")
elif(m>60 and m<80):
    print("B")
elif(m>50 and m<60):
    print("C")
elif(m>45 and m<50):
    print("D")
elif(m>25 and m<45):
    print("E")
elif(m<25):
    print("F")
else:
    print("Incorrect marks entered")
