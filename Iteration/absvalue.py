#Acquire a number from user and print its absolute value
n=eval(input('Enter a number: '))
print('|',n,'| =',(-n if n<0 else n), sep='')
