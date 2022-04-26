def percent(marks ):
    p=(sum(marks)/400)*100
    return p
    
marks1=[33,43,43,64]
percentage1=percent(marks1)

marks2= [45,65,44,76]
percentage2=percent(marks2)

print(f"the number of percentage is {percentage1},{percentage2}")