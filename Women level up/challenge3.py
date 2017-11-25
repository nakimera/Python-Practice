def FindMinMax(ls=[ ]):
    maximum=0
    if ls[0]>maximum:
        maximum=ls[0]
    if ls[1]>ls[0]:
        maximum=ls[2]
    if ls[3]>ls[2]:
        maximum=ls[3]

    print('[',maximum,',', end=' ')

    minimum=ls[0]
    if ls[1]<ls[0]:
        minimum=ls[1]
    if ls[2]<ls[1]:
        minimum=ls[2]
    if ls[3]<ls[2]:
        minimum=ls[2]
    print(minimum, ']')
FindMinMax(ls=[1,5,3,7])
