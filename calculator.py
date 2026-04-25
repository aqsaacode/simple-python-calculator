#calculator building using variables
a=int(input("Enter first number to proceed:"))
b=int(input("Enter second number to proceed:"))
print("Choose from below options")
print("1-I want to substract two numbers")
print("2-I want to add two numbers")
print("3-I want to divide two numbers")
print("4-I want to multiply two numbers")
choice=input("Enter your choice here:")
if choice =="1":
    print(a-b)
elif choice=="2":
    print(a+b)
elif choice=="3":
    print(a/b)
else:
    print(a*b)


