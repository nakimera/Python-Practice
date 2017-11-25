def fizzBuzz(arg):
    for arg in range(0,51,1):
        if type(arg)==int:
            if arg % 3==0 and arg % 5==0:
                print('FizzBuzz')
            elif arg % 3==0:
                print('Fizz')

            elif arg % 5==0:
                print('Buzz')
            
            else:
                print(arg)
        else:
            print('Invalid argument')
        
fizzBuzz(51)
