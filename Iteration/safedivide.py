#Get diividend and divisor from user
dividend,divisor=eval(input('Please enter the dividend and divisor: '))
#we want to divide only if divisor is not zero
#otherwise, we will print an error message
if divisor!=0:
    print(dividend,'/',divisor,'=',dividend/divisor)
else:
    print('Error: Cannot divide by zero :(')
