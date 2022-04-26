total_seconds = int(input('Enter the Second For know the minutes: ')
                    )
day=total_seconds//(24*3600)
total_seconds= total_seconds%(24*3600)
hours= total_seconds//3600
total_seconds= total_seconds%3600
minutes= total_seconds//60
seconds = total_seconds% 60


print("{}day {} hours {} minutes {} seconds ".format(day,hours,minutes,seconds))