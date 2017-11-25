seconds=eval(input('Please enter the number of seconds:'))
#first compute the number of hours in the given number of seconds
#Note:integer division with posiible trancation
hours=seconds//3600 #3600sec=1hour
#compute the reaining seconds after the hours are accounted for
seconds=seconds%3600 
#next,compute the number of minutes in the remaining number of seconds
minutes=seconds//60 #60 sec = 1 min
#compute the remaining seconds after the minutes have been accounted for
seconds=seconds%60
#report the results
print(hours,'hr', minutes,'min', seconds,'sec')
                   
print(hours,':',sep='',end='')
