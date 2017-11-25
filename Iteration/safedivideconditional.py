#Get diividend and divisor from user
dividend,divisor=eval(input('Please enter the dividend and divisor: '))
#we want to divide only if divisor is not zero
#otherwise, we will print an error message
msg=dividend/divisor if divisor!=0 else 'Error: Cannot divide by zero '
print(msg)
