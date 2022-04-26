def factorial_recurcive(n):
    if n==1 or n==0:
        return 1
    return n* factorial_recurcive(n-1)

f= factorial_recurcive(4)
print(f)
 