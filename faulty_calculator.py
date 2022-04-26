"""design a calculator which will correctly solve the problems expect the following ones:
    45*3=555, 56+9=77,56/6 =4
    your program should take operator and the two numbers as input from the user and then return the result
    """
num1=int(input("Enter your first number: "))
num2=int(input("Enter your 2nd number: "))
num3=input("so what you went? +,-,/,%,*: ")
if num1==45 and num2==3 and num3=='*':
    print('555')
elif num1==56 and num2==9 and num3=='+':
    print('77')
elif num1==56 and num2==6 and num3=='/':
    print(['4'])
elif num3=='+':
    print(num1+num2)
elif num3=='-':
    print(num1-num2)
elif num3=='*':
    print(num1*num2)
elif num3=='/':
    print(num1/num2)
elif num3=='%':
    print(num1%num2)
else:
    print('sytenx error')