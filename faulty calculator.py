print("enter firt number")
num1= int(input())
print("enter second nmbr")
num2= int(input())
print("enter operator")
operation= input()
if operation== "+":
    if num1==56:
        if num2==9:
            print(77)
        else:
            print(num1 + num2)

elif operation== "-":
    print(num1- num2)
elif operation== "*":
    if num1==45:
        if num2==3:
            print(555)
        else:
            print(num1 * num2)
elif operation=="/":
    if num1==56:
        if num2==6:
            print(4)
        else:
            print(num1 / num2)

else:
    print("invalid input")