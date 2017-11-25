print('Help, my computer doesnot work')
print('Does the computer make any sound(fans,etc)')
choice=input('or show any lights? (y/n):')

#The troubleshooting control logic
if choice=='n':        #The computer doesnt have power
    choice=input('Is it plugged in? (y/n:)')
    if choice=='n':        #it is not plugged in, plug it in
        print('Plug it in. If the problem persists, ')
        print('Please run this program again')
    else:                  #it is plugged in
        choice=input('Is the switch in the \'on\' position? (y/n:)')
        if choice=='n':        #the switch is off, turn it on
            print('Turn it on. If the problem persists, ')
            print('Please run this program again')
        else:                  #the switch is on
            choice=input('Does the computer have a fuse? (y/n:)')
            if choice=='n':        #No fuse
                choice=input('Is the outlet OK? (y/n:)')
                if choice=='n': #fix outlet
                    print('Check the outlets circuit')
                    print('Breaker or fuse. Move to a')
                    print('new outlet,if necessary')
                    print('If the problem persists')
                    print('Please run this program again')
                else:            #Beats me
                    print('Please consult a service technician')
            else:
                print('Check the fuse and replace if necessary')
                print('if problem persists, then')
                print('Please run this program again')
else:                     #The computer has power
    print('Please consult a service technician')
                    
       
    
    
