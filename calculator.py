print("calculator by yasir")
num1 = float(input("enter number: "))
operator = input('enter an operation(+-*/):')
num2 = float(input("enter number: "))
if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1-num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
else:
    print("Invalid number or the operator!! try again!")