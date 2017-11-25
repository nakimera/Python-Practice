month=eval(input('Please enter the month as a number (1-12): '))
day=eval(input('Please enter the day of the month: '))
#Translate month into English
if month==1:
    print('January',end=' ')
elif month==2:
    print('February',end=' ')
elif month==3:
    print('March',end=' ')
elif month==4:
    print('April',end=' ')
elif month==5:
    print('May',end=' ')
elif month==6:
    print('June',end=' ')
elif month==7:
    print('July',end=' ')
elif month==8:
    print('August',end=' ')
elif month==9:
    print('September',end=' ')
elif month==10:
    print('October',end=' ')
elif month==11:
    print('November',end=' ')
else:
    print('December',end=' ')

#add the day
print(day , 'or' ,day ,end=' ')

#Translate month into Spanish
if month==1:
    print('Enero')
elif month==2:
    print('Febrero')
elif month==3:
    print('Marzo')
elif month==4:
    print('Abril')
elif month==5:
    print('Mayo')
elif month==6:
    print('Junio')
elif month==7:
    print('Julio')
elif month==8:
    print('Agosto')
elif month==9:
    print('Septiembre')
elif month==10:
    print('Octubre')
elif month==11:
    print('Noviembre')
else:
    print('Diciembre')
