def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m= maximum(4,43,42)

print(m)