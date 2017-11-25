#allow user to enter a number of non negative numbers
#the user ends the list with a negative number
#at the end the sum of the non-negatives entered is displayed
#The program prints zero if the user provides no non-negative numbers

entry=0
sum=0
print('Enter numbers to sum, negative number ends list')
while entry>=0:
    entry=eval(input())
    if entry>=0:
        sum+=entry
print('sum = ',sum)
