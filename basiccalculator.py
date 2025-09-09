#basic calculator
num1 = float(input("Enter a no. : "))
num2 = float(input("Enter a no. : "))
operator = input("Enter an operator (+,-,*,/) : ")
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    if num2 == 0:
        print("ERROR!!")
    else:
        print(num1/num2)
else:
    print("Enter a Valid operator")

