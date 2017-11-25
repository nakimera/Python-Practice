#get 2 numbers from the user
dividend,divisor=eval(input('Please enter 2 numbers to be divided: '))
#if posiible divide them and get results
if divisor!=0:
    quotient=dividend/divisor
    print(dividend,'/',divisor,'=',quotient)
else:
    print('Division by zero is not allowed')

