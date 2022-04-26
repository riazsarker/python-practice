num = int(input('Enter the number:'))


for i in range(2,num):
    if(num%i==0):
        prime = True
        break
if prime:
    
    print('This number is Prime')
else:
    print('the numb is not prime')