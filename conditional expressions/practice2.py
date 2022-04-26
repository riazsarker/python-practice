sub1=int(input("Enter 1st Numer\n"))
sub2=int(input("Enter 2nd Numer\n"))
sub3=int(input("Enter 3rd Numer\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33% in one of the subjects")

elif (sub1+sub2+sub3)/3 <40:
    print("you are fail due to total percentage less than 40")
else:
    print("congatulations! you passed the exam")