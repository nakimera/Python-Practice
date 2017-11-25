def variable(var):

    if(type(var))==str:
        if  var !=' ':
            print (len(var))
        else: ('no value')
    elif(type(var))==bool:
        print(var)
    elif(type(var))==int:
        if var<100:
            print('less than 100')
        elif var==100:
            print('Equal to 100')
        else:
            print('more than 100')
    elif(type(var))==list:
        if len(var)>=3:
            print(var[2])
        else:
            print('undefined')
variable([1,4,6,4])
